# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-222913` | 18/24 | 75% | 7/8 (88%) | 8/13 (62%) | 3/3 (100%) | chưa đạt (<80%; `tu_choi` đạt 100%) |
| 2 | | __/__ | | __/__ | __/__ | __/__ | đạt / chưa |

- Model lượt 1: `openai/gpt-oss-20b` (qua Groq API), 0 lỗi kỹ thuật, 0 `trace_mismatch`.
- Chi tiết theo 3 metric ở lượt 1: `ket_luan_dung` **18/21 (85.7%)** khớp nhãn bề mặt (**17/21 = 81.0%** thực chất nếu trừ `B15` bị lỗi parser ép về fallback trùng nhãn) · `trich_dieu_khoan` **21/21 (100%)** câu có kết luận đều trích ≥1 mã hợp lệ trong `SP-01`..`SP-35` (0 mã bịa) · `tu_choi_dung` **3/3 (100%)** chặn bằng code ở bước ①. Kết hợp đủ `pass_criterion` từng câu đạt **18/24 (75%)** (`B23`, `B24` đúng nhãn nhưng trượt ý cốt lõi `SP-35` và `SP-23`/`SP-30`).
- Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Bước ② `tach_thong_tin` bỏ sót từ khoá / chủ đề → thiếu điều khoản quyết định đưa vào model | 3 *(+2 câu đạt nhưng thiếu mã phụ)* | `B18`, `B23`, `B24` *(và thiếu mã phụ ở `B08`, `B16`)* |
| Bước ⑤ `kiem_can_cu` không đọc được dòng `**KẾT LUẬN:**` có Markdown in đậm → hạ oan về fallback | 2 | `B09`, `B15` |
| Bước ② `tach_thong_tin` gán nhầm `bang_chung = "không"` khi câu có phủ định cục bộ | 1 *(cùng ảnh hưởng `B18`)* | `B21` |

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| `B09` | Mình mua chiếc váy trên Shopee mới nhận 3 ngày, đúng mẫu đúng size và không bị rách lỗi gì cả, nhưng mặc lên thấy không hợp màu da và mình lỡ cắt tem mác rồi. Mình chọn lý do Hàng lỗi để được miễn phí trả hàng có được không? | `KẾT LUẬN: Không chắc cần CSKH` — Mình chưa đủ căn cứ để kết luận chắc chắn cho trường hợp này. Các điều khoản liên quan nên đọc: SP-05, SP-10, … | Trong `traces/run-1.jsonl`, model thực ra đã trả lời đúng `**KẾT LUẬN:** Chưa đủ điều kiện`, nhưng vì có dấu in đậm `**` nên bước ⑤ `kiem_can_cu` kiểm `startswith("KẾT LUẬN")` bị trượt và hạ oan toàn bộ câu trả lời về fallback chung chung. |
| `B18` | Mình đặt cái ốp lưng 65k trên Shopee nhận hôm qua (1 ngày), đã thanh toán ShopeePay. Mở bọc ra thấy màu in lệch hẳn so với ảnh shop và viền cao su lem nhem. Mình không quay video mở hộp nhưng đã chụp ảnh rõ lỗi sản phẩm ngay lúc nhận… | `KẾT LUẬN: Không chắc cần CSKH` — điều khoản [SP-05] chỉ áp dụng cho "sản phẩm bị lỗi hoặc hư hại trong quá trình vận chuyển", trong khi màu in lệch không nêu rõ là lỗi do vận chuyển… | Sai `ket_luan_dung` (kỳ vọng `Đủ điều kiện`) và quên trả lời phí ship `SP-28`. Nguyên nhân ở bước ②: không bắt cụm "màu in lệch so với ảnh shop" sang chủ đề `sai_mo_ta` (`SP-07`) nên model thiếu căn cứ `SP-07`. |
| `B21` | Mình mua bàn phím cơ 600k trên Shopee nhận 3 ngày trước, đã quay clip khui vỏ hộp ngoài nhưng tối về cắm test mới thấy liệt một hàng phím số. Mình gửi yêu cầu lý do hàng lỗi thì shop từ chối vì video khui hộp chưa quay lúc test phím… | `KẾT LUẬN: Chưa đủ thông tin cần hỏi thêm` — Theo [SP-25], người mua phải cung cấp video hoặc ảnh khi nhận hàng; hiện tại bạn chưa có bằng chứng này… | Sai `ket_luan_dung` (kỳ vọng `Không chắc cần CSKH`, đang tranh chấp chờ Shopee quyết định `SP-16`). Bước ② bắt cụm "chưa quay lúc test phím" gán nhầm `bang_chung = "không"`, khiến model tưởng khách không có bằng chứng gì. |
| `B23` | Mình nhận áo sơ mi bị rách tay áo trên Shopee cách đây 3 ngày, có đủ video và ảnh lúc nhận hàng. Nhắn cho shop thì shop bảo nhận hoàn tiền không cần trả hàng 30% giá áo, hoặc nhắn Zalo để shop tự gửi áo khác… | `KẾT LUẬN: Đủ điều kiện` — nêu đúng `SP-34` (30% < 50% không hợp lệ), soạn nháp yêu cầu; **không nhắc gì về Zalo / giao dịch ngoài Shopee**. | Trượt `pass_criterion`: bỏ sót hoàn toàn cảnh báo không liên lạc/giao dịch qua Zalo ngoài hệ thống Shopee (`SP-35`) vì bước ② chưa có chủ đề `lien_lac`, gây rủi ro người mua mất bằng chứng khiếu nại. |
| `B24` | Mình nhận ấm siêu tốc bị lỗi không vào điện trên shop thường Shopee cách đây 4 ngày, có video và ảnh lúc nhận hàng. Shop im lặng không trả lời thì có bị treo luôn không, chọn Tự sắp xếp có miễn phí ship không? | `KẾT LUẬN: Đủ điều kiện` — khuyên "nộp khiếu nại tại mục Kê khai khiếu nại" và "đặt phương thức Tự sắp xếp và thanh toán phí vận chuyển". | Bước ② không bắt "shop im lặng" nên thiếu `SP-23` (tự động hoàn sau 02 ngày lịch) khiến model bịa mục "Kê khai khiếu nại"; đồng thời bỏ sót `SP-30` (hỗ trợ một phần Shopee Xu ở shop thường) và khuyên ngược chọn Tự sắp xếp chịu phí thay vì lấy tại nhà/bưu cục miễn phí (`SP-28`). |

## 3. Một lần cải tiến

*(Điền sau khi chạy lượt 2 trước CP4 14:30 Thứ Bảy 28/11.)*

- Nhắm vào nhóm lỗi: __ — vì sao là nhóm **đau nhất với người dùng**: __
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): __
- Kết quả: nhóm lỗi đó __/__ → __/__ · tổng __% → __%
- Câu nào **tệ đi** sau khi sửa: __

## 4. Còn lại

*(Điền sau lượt 2 trước CP4.)*

- Lỗi chưa sửa + nguy hiểm thế nào: __
- Nếu có thêm 1 tuần: __
