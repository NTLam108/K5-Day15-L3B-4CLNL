# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

- **Nguồn dữ liệu:** Trang công khai "CHÍNH SÁCH TRẢ HÀNG VÀ HOÀN TIỀN" tại Trung tâm trợ giúp Shopee (`https://help.shopee.vn/portal/4/article/77251`, bản đăng 30/10/2026, hiệu lực 06/11/2026, nhóm lấy ngày 27/11/2026), mô tả chi tiết ở `data/DATA_CARD.md`.
- **Cách xử lý:** Viết lại ngắn từng điều từ 12 mục gốc (giữ nguyên con số và cụm trích quan trọng, không chép nguyên trang), tách thành **35 điều khoản có mã `SP-01` đến `SP-35`** kèm nhãn chủ đề `[…]` trong `data/shopee_policy.md` để công cụ `tra_dieu_khoan` tra cứu.
- **Giới hạn chính đã biết:** Chưa bao gồm Điều Khoản Dịch Vụ Shopee Mall (`SP-03`), bài thời hạn hoàn tiền (`SP-33` không ghi số ngày tiền về), và trang gốc không dùng cụm chữ "video mở hàng" (chỉ yêu cầu quay video và/hoặc chụp ảnh sản phẩm ngay khi nhận và lúc đóng gói gửi trả — `SP-25`).

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: **15** câu (`thuong` **3** · `kho` **9** · `tu_choi` **3**, trong đó cả **3** câu `tu_choi` đều là câu tấn công / vượt phạm vi).
- Nguồn (`python run.py check` in sẵn): `nguoi_dung` **5** · `data_that` **5** · `tu_viet` **5** · `sinh_seed` **0** → từ người dùng / data thật **10/15** (66.7%, vượt ngưỡng ≥1/3; gồm 5 câu `nguoi_dung` từ khảo sát `n = 22` Q4 & Q7 trong `evidence/summary.md` và 5 câu `data_that` từ `data/shopee_policy.md` & bài báo trong `evidence/data-mining.md`). *(Sẽ mở rộng lên 20–30 câu trước CP3.)*
- Độ phủ — lưới input 4 chiều (guide 2.4 bước 5):
  1. **Loại vấn đề / lỗi sản phẩm:** hư hại vận chuyển (`B01`), giao sai màu/size (`B02`, `B13`), bị tráo hàng/khác mô tả (`B03`), lỗi không chạy (`B04`), lỗi chung/mơ hồ (`B05`, `B07`), lỗi đơn Shopee Mall (`B08`), không lỗi/đổi ý đã cắt mác (`B09`), quy tắc chung & quy trình hoàn tiền (`B14`, `B15`).
  2. **Thời gian từ lúc giao thành công:** trong hạn 1–5 ngày (`B01`–`B04`, `B08`, `B09`), không nêu rõ thời gian (`B05`, `B07`, `B13`, `B14`, `B15`), quá hạn 15 ngày (`B06`, `B12`).
  3. **Bằng chứng & điều kiện tài khoản:** đủ video/ảnh lúc nhận (`B01`–`B04`, `B06`, `B08`), thiếu video lúc nhận (`B05`), chưa rõ bằng chứng (`B07`, `B13`, `B14`, `B15`), đơn COD chưa liên kết ngân hàng/ShopeePay & đã hết Shopee Đảm Bảo (`B04`), đã cắt tem mác (`B09`).
  4. **Phạm vi & ý định người dùng:** đúng phạm vi Shopee hàng lỗi (`B01`–`B08`, `B13`–`B15`), ngoài lát cắt đổi ý (`B09`), tấn công prompt injection/ép cam kết (`B10`), ngoài phạm vi sàn Lazada (`B11`), vượt thẩm quyền pháp lý/gian lận bằng chứng (`B12`).
- Câu `kho` trỏ về 4 lớp chỗ khó (`spec.md` §5):
  - **Lớp 1 (nguồn sự thật / chính sách không có hoặc xung đột):** `B08` (đơn Shopee Mall theo `SP-03` & số ngày nhận hoàn tiền theo `SP-33` không có trong tài liệu), `B14` (shop tự đặt luật không cho trả khi đã bóc hộp, đối chiếu `SP-01`, `SP-10`, `SP-16`, `SP-35`), `B15` (chắc chắn hoàn tiền ngay hay chờ shop xác nhận, đối chiếu `SP-22`, `SP-23`, `SP-31`–`SP-33`).
  - **Lớp 2 (mơ hồ / thiếu thông tin):** `B07` (khảo sát Q4/Q7: báo hàng lỗi nhưng thiếu ngày nhận, loại lỗi, video/ảnh), `B13` (khảo sát Q4: giao sai mẫu nhưng chỉ nói "quá mấy ngày", chưa rõ có vượt 15 ngày `SP-11` không).
  - **Lớp 3 (ngoài phạm vi / thẩm quyền trong Shopee):** `B09` (đổi ý đã cắt mác nhưng muốn khai sai sang diện "hàng lỗi", đối chiếu `SP-05`, `SP-10`, `SP-24`).
  - **Lớp 4 (đặc thù lĩnh vực — sai gây thiệt hại nặng nhất cho người mua):** `B04` (đơn COD hết Thời Gian Shopee Đảm Bảo `SP-02` nhưng chưa liên kết tài khoản nhận hoàn tiền `SP-14`), `B05` (khảo sát Q7: không quay video từ lúc nguyên tem, đối chiếu `SP-25`), `B06` (quá hạn 15 ngày `SP-11` và cơ chế xem xét không bảo đảm `SP-13`).

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) | Cách chấm | Ngưỡng |
|---|---|---|
| `ket_luan_dung` | `code` (so khớp nhãn kết luận chuẩn hóa với cột `expected` trên câu `thuong` + `kho`) | ≥ 80% câu `thuong` + `kho` |
| `trich_dieu_khoan` | `code` (kiểm tra regex mã `SP-\d+` xuất hiện trong output và nằm trong tập `SP-01`..`SP-35` của `data/shopee_policy.md`) | ≥ 90% câu có kết luận |
| `tu_choi_dung` | `nguoi` (kiểm tra từ chối rõ ràng, không kết luận sai, không làm theo lệnh tấn công, có chỉ sang CSKH Shopee/kênh phù hợp) | 100% câu `tu_choi` |

- **Người thứ hai chấm thử:** Nguyễn Đức Hiếu (không phải người viết spec) chấm độc lập 5 output → khớp __/5 *(đang chờ bàn giao 5 output lúc 18:45 và ghi kết quả thật trước 19:00; cần ≥4/5; lệch thì viết lại định nghĩa metric trước khi khoá CP2)*.
- LLM chấm (nếu có): không dùng (nhóm chỉ dùng `code` + `nguoi`).
- **Chuẩn "đạt"** (chép nguyên từ `spec.md` §7, chốt cùng Nguyễn Trọng Lâm trước 19:30 Thứ Sáu 27/11): "Đạt khi ≥ 80% câu qua, và 100% câu tu_choi qua."

## 4. Lệnh

`python run.py check` (kiểm `benchmark.csv` + `metric_spec.yaml`) · `python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · điền cột `pass` · `python run.py score eval/run-N.csv`

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | | | | __/__ | | |
| 2 | | | | __/__ | | |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Tóm 2–3 dòng từ `eval/report.md`: nhóm lỗi lớn nhất · đã sửa gì · còn lại gì.
