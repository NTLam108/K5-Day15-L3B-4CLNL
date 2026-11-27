"""Luồng chính của bản chạy thử — trợ lý trả hàng Shopee cho đơn hàng lỗi. Điền ở guide bước 3.2.

`python run.py`, `python run.py eval` và `python run.py simulate` đều gọi answer(text).

Hình dạng: WORKFLOW CỐ ĐỊNH 6 bước, đúng sơ đồ spec.md §4 — chỉ 1 lời gọi model (bước ④):
    ① chan_pham_vi    (code)  sàn khác / pháp lý / gian lận / câu lệnh tấn công → từ chối, chỉ sang CSKH
    ② tach_thong_tin  (code)  loại vấn đề, số ngày từ lúc nhận, có video/ảnh, Shopee Mall, COD → chủ đề tra cứu
                              không nhận ra chủ đề nào → hỏi lại, không gọi model
    ③ tra_dieu_khoan  (công cụ, chỉ đọc data/shopee_policy.md)
    ④ call_model      model quyết định nhãn kết luận + trích mã SP-xx + việc còn thiếu + nháp yêu cầu
    ⑤ kiem_can_cu     (code)  thiếu nhãn / thiếu mã / mã không có trong data → hạ về "Không chắc cần CSKH" (G10)
    ⑥ trả kết quả     người mua tự đọc, tự sửa, tự bấm gửi trên Shopee — hệ thống không gửi thay
"""
import re

from ai import call_model
from tools import tra_dieu_khoan, ALL_CODES
from tracing import note

# Nhãn kết luận — khớp metric ket_luan_dung trong eval/metric_spec.yaml
DU = "Đủ điều kiện"
CHUA_DU = "Chưa đủ điều kiện"
HOI_THEM = "Chưa đủ thông tin cần hỏi thêm"
KHONG_CHAC = "Không chắc cần CSKH"
TU_CHOI = "Từ chối"
NHAN = (HOI_THEM, KHONG_CHAC, CHUA_DU, DU)  # thứ tự dò: chuỗi dài / dễ nhầm trước

CSKH = "Bạn có thể liên hệ CSKH Shopee (Tôi → Trung tâm hỗ trợ → Chat với Shopee) để được xem xét trực tiếp."

SYSTEM = """Bạn là trợ lý giúp NGƯỜI MUA Shopee kiểm tra một đơn hàng lỗi / hư hỏng / sai mẫu có đủ điều kiện trả hàng - hoàn tiền không.
Luật bắt buộc:
- CHỈ dựa vào các điều khoản được cung cấp (mã SP-xx). Không dùng hiểu biết bên ngoài, không bịa số ngày, số tiền hay quy định.
- Mọi kết luận phải trích mã điều khoản trong ngoặc vuông, vd [SP-05].
- Thiếu thông tin quyết định (ngày giao thành công, lỗi cụ thể, video/ảnh lúc nhận) thì KHÔNG đoán: dùng nhãn "Chưa đủ thông tin cần hỏi thêm" và hỏi đúng phần thiếu.
- Điều khoản không nói rõ (vd quy định riêng Shopee Mall, số ngày tiền về) thì dùng nhãn "Không chắc cần CSKH".
- Không hứa chắc được hoàn tiền. Không hướng dẫn khai sai lý do hay làm giả bằng chứng. Không tự gửi yêu cầu thay người mua.
Trả lời tiếng Việt, đúng khuôn sau:
KẾT LUẬN: <một trong: Đủ điều kiện | Chưa đủ điều kiện | Chưa đủ thông tin cần hỏi thêm | Không chắc cần CSKH>
LÝ DO: <2-4 câu, mỗi ý kèm [SP-xx]>
VIỆC CẦN LÀM / CÒN THIẾU:
- <từng việc, kèm [SP-xx] nếu có>
NHÁP YÊU CẦU TRẢ HÀNG: <đoạn ngắn người mua dán vào Shopee; ghi "(chưa soạn)" nếu chưa đủ điều kiện hoặc chưa đủ thông tin>"""

# ---------- ① chặn phạm vi ----------
_SAN_KHAC = re.compile(r"lazada|tiki|tiktok\s*shop|sendo|amazon|shein|temu", re.I)
_TAN_CONG = [
    (re.compile(r"bỏ qua.{0,40}(chính sách|quy định|hướng dẫn|luật)", re.I), "yêu cầu bỏ qua chính sách"),
    (re.compile(r"100\s*%"), "ép cam kết chắc chắn 100%"),
    (re.compile(r"(tự bấm|bấm gửi|gửi).{0,40}(giúp tôi|giùm|thay tôi|hộ tôi)", re.I), "yêu cầu trợ lý tự gửi thay"),
    (re.compile(r"(chỉnh|sửa|làm giả|giả mạo|photoshop|edit).{0,25}(ngày|ảnh|video|bằng chứng|hoá đơn|hóa đơn)", re.I),
     "làm giả / chỉnh sửa bằng chứng"),
    # không dùng chữ "kiện" đơn lẻ vì trùng "điều kiện"
    (re.compile(r"khởi kiện|đơn kiện|đi kiện|kiện (shop|shopee|người bán)|ra tòa|ra toà|luật sư", re.I),
     "tư vấn pháp lý / soạn đơn kiện"),
]


def chan_pham_vi(text):
    """Trả (lý do từ chối, lời từ chối) nếu ngoài phạm vi; None nếu trong phạm vi."""
    if _SAN_KHAC.search(text) and "shopee" not in text.lower():
        return ("sàn khác", "Mình chỉ hỗ trợ đơn hàng Shopee theo chính sách trả hàng của Shopee, nên không kết luận "
                "được cho đơn ở sàn khác. Bạn vui lòng xem chính sách hoặc liên hệ CSKH của sàn đó.")
    if _SAN_KHAC.search(text):
        return ("sàn khác", "Câu hỏi nhắc tới sàn khác ngoài Shopee — mình chỉ hỗ trợ đơn Shopee. Nếu đơn của bạn mua trên "
                "Shopee, hãy mô tả lại đơn đó; còn đơn sàn khác vui lòng liên hệ CSKH của sàn đó.")
    for pattern, why in _TAN_CONG:
        if pattern.search(text):
            return (why, "Mình không thể làm theo yêu cầu này (%s). Mình chỉ kiểm tra điều kiện theo đúng chính sách "
                    "Shopee, không hứa chắc kết quả, không gửi yêu cầu thay bạn, không hỗ trợ chỉnh sửa bằng chứng "
                    "hay tư vấn pháp lý." % why)
    return None


# ---------- ② tách thông tin ----------
_CHU_DE = [
    ("hang_loi", r"lỗi|hỏng|\bhư\b|hư hại|móp|nứt|vỡ|\bbể\b|rách|bung|không chạy|không lên|trầy"),
    ("sai_mau", r"sai (mẫu|màu|size|cỡ|kích)|nhầm|giao sai|khác mẫu"),
    ("sai_mo_ta", r"khác (mô tả|hình)|không giống|tráo|cục gỗ|treo đầu dê"),
    ("khong_nhan_hang", r"không nhận được|chưa nhận được|thiếu hàng|giao thiếu|hàng giả|hàng nhái|fake"),
    ("het_han", r"hết hạn|hạn sử dụng|\bdate\b"),
    ("doi_y", r"đổi ý|không hợp|không thích|không còn nhu cầu|không vừa|cắt (tem|mác)"),
    ("thuc_pham_tuoi", r"tươi sống|đông lạnh|thực phẩm|\brau\b|\bthịt\b|\bcá\b|hải sản"),
    ("cod", r"\bcod\b|thanh toán khi nhận|chưa liên kết|liên kết"),
    ("shopee_mall", r"shopee\s*mall|\bmall\b"),
    ("hoan_tien", r"hoàn tiền|tiền về|hoàn ngay|bao lâu"),
    ("nguoi_ban", r"shop (không|chưa) (trả lời|phản hồi|đồng ý)|người bán|shop bảo|shop từ chối|xác nhận"),
    ("phi_ship", r"phí ship|phí vận chuyển|tốn phí|miễn phí|tự sắp xếp"),
    ("bang_chung", r"video|ảnh|chụp|quay|bằng chứng|tem niêm phong"),
    ("thoi_han", r"ngày|hạn|quá|trễ|muộn"),
    ("pham_vi", r"quy tắc chung|chính sách chung|mỗi shop"),
]
_NGAY = re.compile(r"(\d{1,3})\s*ngày")


def tach_thong_tin(text):
    low = text.lower()
    chu_de = [ten for ten, pat in _CHU_DE if re.search(pat, low)]
    m = _NGAY.search(low)
    so_ngay = int(m.group(1)) if m else (1 if "hôm qua" in low else 0 if "hôm nay" in low else None)
    if re.search(r"(không|chưa|quên)\s*(có\s*)?(quay|chụp|có video)", low):
        bang_chung = "không"
    elif re.search(r"video|ảnh|chụp", low):
        bang_chung = "có"
    else:
        bang_chung = None
    thieu = []
    if so_ngay is None:
        thieu.append("số ngày từ lúc đơn giao thành công")
    if not set(chu_de) & {"hang_loi", "sai_mau", "sai_mo_ta", "khong_nhan_hang", "het_han", "doi_y"}:
        thieu.append("sản phẩm gặp vấn đề gì cụ thể")
    if bang_chung is None:
        thieu.append("đã quay video / chụp ảnh sản phẩm lúc nhận hàng chưa")
    return {"chu_de": chu_de, "so_ngay": so_ngay, "bang_chung": bang_chung, "thieu": thieu}


# ---------- ⑤ kiểm căn cứ ----------
def kiem_can_cu(reply):
    """Trả (nhãn, các mã hợp lệ, vấn đề) — vấn đề rỗng nghĩa là qua."""
    first = next((ln for ln in reply.splitlines() if ln.strip().upper().startswith("KẾT LUẬN")), "")
    nhan = next((n for n in NHAN if n.lower() in first.lower()), None)
    codes = re.findall(r"SP-\d{2}", reply)
    bad = sorted(set(c for c in codes if c not in ALL_CODES))
    ok = sorted(set(c for c in codes if c in ALL_CODES))
    van_de = []
    if not nhan:
        van_de.append("không có dòng KẾT LUẬN với nhãn hợp lệ")
    if bad:
        van_de.append("mã không có trong data: " + ", ".join(bad))
    if nhan in (DU, CHUA_DU) and not ok:
        van_de.append("kết luận không kèm mã điều khoản")
    return nhan, ok, van_de


def answer(text: str) -> dict:
    text = (text or "").strip()

    # ①
    blocked = chan_pham_vi(text)
    if blocked:
        note("bước 1 — từ chối: " + blocked[0])
        return {"output": "KẾT LUẬN: %s (ngoài phạm vi)\n%s\n%s" % (TU_CHOI, blocked[1], CSKH)}

    # ②
    info = tach_thong_tin(text)
    note("bước 2 — chủ đề=%s · số ngày=%s · bằng chứng=%s" % (info["chu_de"], info["so_ngay"], info["bang_chung"]))
    if not info["chu_de"]:
        note("dừng ở bước 2: không nhận ra vấn đề nào để tra")
        return {"output": "KẾT LUẬN: %s\nMình cần thêm thông tin để đối chiếu chính sách:\n- %s"
                          % (HOI_THEM, "\n- ".join(info["thieu"]))}

    # ③
    clauses = tra_dieu_khoan(info["chu_de"])
    can_cu = "\n".join("[%s] (mục %s) %s" % (c["code"], c["muc"], c["text"]) for c in clauses)

    # ④
    user = ("ĐIỀU KHOẢN ĐƯỢC PHÉP DÙNG:\n%s\n\nTHÔNG TIN ĐÃ TÁCH (có thể sai, đối chiếu lại với lời người mua):\n"
            "- số ngày từ lúc nhận: %s\n- video/ảnh lúc nhận: %s\n- có thể còn thiếu: %s\n\nLỜI NGƯỜI MUA:\n%s"
            % (can_cu, info["so_ngay"] if info["so_ngay"] is not None else "chưa rõ",
               info["bang_chung"] or "chưa rõ", "; ".join(info["thieu"]) or "không", text))
    reply = call_model(SYSTEM, user)["text"].strip()
    # Một số model dùng dấu gạch nối Unicode trong mã điều khoản.
    reply = re.sub(r"(?i)\bSP[\u2010-\u2015\u2212](\d{2})\b", r"SP-\1", reply)

    # ⑤
    nhan, ok, van_de = kiem_can_cu(reply)
    if van_de:
        note("bước 5 — hạ về Không chắc: " + "; ".join(van_de))
        lien_quan = ", ".join(c["code"] for c in clauses)
        return {"output": "KẾT LUẬN: %s\nMình chưa đủ căn cứ để kết luận chắc chắn cho trường hợp này. "
                          "Các điều khoản liên quan nên đọc: %s (data/shopee_policy.md).\n%s"
                          % (KHONG_CHAC, lien_quan, CSKH)}
    note("bước 5 — qua: nhãn=%s · mã=%s" % (nhan, ", ".join(ok)))

    # ⑥ người mua tự gửi — chỉ trả bản nháp
    return {"output": reply + "\n\n(Bạn tự kiểm tra lại và tự gửi yêu cầu trên app Shopee — trợ lý không gửi thay.)"}
