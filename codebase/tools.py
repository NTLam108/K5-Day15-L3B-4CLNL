"""Công cụ của bài toán — NHÓM VIẾT. Điền ở guide bước 2.2 (thiết kế) và 3.2 (code).

Mỗi công cụ là một hàm Python có @tool. Docstring ghi đúng 4 ý như sơ đồ ở spec.md §4:
    tên · input · output · có tác động ra ngoài không (gửi tin, sửa dữ liệu, chấm điểm…)
Khung tự ghi mỗi lần gọi công cụ vào trace (tên, input, output rút gọn, thời gian, lỗi).

Lát cắt chỉ cần MỘT công cụ chỉ-đọc: tra_dieu_khoan (bước ③ trong sơ đồ spec.md §4).
Dữ liệu: data/shopee_policy.md — mô tả ở data/DATA_CARD.md (Dataset 1).
"""
import os
import re

from tracing import tool, TOOLS  # noqa: F401  (TOOLS: danh sách công cụ đã đăng ký)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POLICY_PATH = os.path.join(ROOT, "data", "shopee_policy.md")

# Một dòng điều khoản: - **SP-05** (mục 3.1.2) [ly_do, hang_loi] — nội dung
_LINE = re.compile(r"^- \*\*(SP-\d{2})\*\* \(mục ([^)]+)\) \[([^\]]+)\] — (.+)$")

# Điều khoản luôn trả kèm vì gần như câu hỏi nào về hàng lỗi cũng cần: hạn 15 ngày, bằng chứng, quyền quyết định của Shopee.
LUON_KEM = ("SP-11", "SP-25", "SP-16")


def load_policy(path=POLICY_PATH):
    """Đọc data/shopee_policy.md → {mã: {"code", "muc", "tags", "text"}}. Không phải công cụ, chỉ là hàm đọc file."""
    clauses = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = _LINE.match(line.strip())
            if m:
                code, muc, tags, text = m.groups()
                clauses[code] = {"code": code, "muc": muc,
                                 "tags": [t.strip() for t in tags.split(",")], "text": text.strip()}
    return clauses


POLICY = load_policy()
ALL_CODES = set(POLICY)


@tool
def tra_dieu_khoan(chu_de: list) -> list:
    """tra_dieu_khoan — tìm điều khoản chính sách trả hàng / hoàn tiền Shopee theo chủ đề.
    Input: danh sách nhãn chủ đề (list[str]), vd ["hang_loi", "thoi_han", "cod"] — nhãn khớp cột [..] trong data/shopee_policy.md.
    Output: danh sách điều khoản {"code", "muc", "text"}, theo thứ tự mã; luôn kèm SP-11, SP-25, SP-16.
    Tác động ra ngoài: KHÔNG — chỉ đọc file data/shopee_policy.md."""
    wanted = set(chu_de or [])
    hits = [c for c in POLICY.values() if wanted & set(c["tags"]) or c["code"] in LUON_KEM]
    hits.sort(key=lambda c: c["code"])
    return [{"code": c["code"], "muc": c["muc"], "text": c["text"]} for c in hits]
