# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Chính sách Trả hàng và Hoàn tiền Shopee (`data/shopee_policy.md`)

| | |
|---|---|
| Dùng để làm gì | nguồn cho công cụ `tra_dieu_khoan` (bước ③ trong sơ đồ `spec.md` §4) · căn cứ cho cột `expected` của bộ câu thử (trỏ mã `SP-xx`) |
| Từ đâu | trang công khai Shopee Trung tâm trợ giúp, "CHÍNH SÁCH TRẢ HÀNG VÀ HOÀN TIỀN": https://help.shopee.vn/portal/4/article/77251 |
| Xử lý những bước gì | viết lại ngắn từng điều, giữ nguyên con số và trích nguyên văn cụm quan trọng · chia thành điều khoản có mã `SP-01`…`SP-35` · gắn nhãn chủ đề `[…]` để tra cứu · không có dữ liệu cá nhân nên không cần ẩn danh |
| Số dòng / số đoạn | 35 điều khoản (từ 12 mục của trang gốc) |
| Phiên bản / ngày lấy | bản đăng 30/10/2026, hiệu lực 06/11/2026 · lấy ngày 27/11/2026 |
| Nhãn | thật (viết lại từ nguồn công khai) |
| Giới hạn | Chỉ một trang: thiếu Điều Khoản Dịch Vụ Shopee Mall, bài thời hạn hoàn tiền, bài hoàn tiền không cần trả hàng · trang gốc **không có** chữ "video mở hàng" (chỉ yêu cầu video và/hoặc ảnh khi nhận và khi đóng gói, SP-25) · nội dung được đọc qua công cụ tải trang rồi viết lại — một thành viên cần đối chiếu lại với trang gốc trước CP3 · Shopee có thể sửa chính sách bất cứ lúc nào (SP-01) |

## Dataset 2 · Câu trả lời khảo sát người mua Shopee (nguồn `nguoi_dung` cho bộ câu thử)

| | |
|---|---|
| Dùng để làm gì | lấy tình huống và cách nói thật của người dùng để viết câu thử `source = nguoi_dung` trong `eval/benchmark.csv` · số liệu pain ở `evidence/summary.md` |
| Từ đâu | Google Form nhóm tự làm (bộ câu hỏi: `evidence/survey/questions.md`), gửi nhóm lớp L3B và bạn bè 18–30 tuổi, mở 17:15 – chốt 18:10 ngày 27/11/2026 |
| Xử lý những bước gì | chỉ đưa vào repo **số đã tổng hợp** và **trích dẫn Q7 đã bỏ tên** · **bỏ hẳn câu Q8** (SĐT / Zalo / Discord của người sẵn sàng phỏng vấn — dữ liệu cá nhân, không commit) · không thu email, tên, mã học viên · câu Q7 dùng làm câu thử thì viết lại cho khỏi lộ chi tiết nhận diện được người trả lời |
| Số dòng / số đoạn | 24 phiếu · Q7 (trả lời tự do): 15 câu có nội dung, 5 câu đã trích ở `evidence/summary.md` · bản ẩn danh: `evidence/survey/results.csv` (24 dòng, 8 cột Q1–Q7 + dấu thời gian, không có cột Q8) |
| Phiên bản / ngày lấy | xuất từ Google Form ngày 27/11/2026 · file xuất gốc (có Q8) giữ ngoài repo, người giữ: Vũ Xuân Hiếu |
| Nhãn | thật |
| Giới hạn | lệch về sinh viên (23/24), chỉ 1 nhân viên văn phòng · mẫu thuận tiện (lớp + bạn bè), không đại diện người mua Shopee nói chung · tự khai, không đối chiếu đơn hàng thật · Q3–Q6 bắt buộc nên cả 10 người "chưa từng gặp hàng lỗi" cũng trả lời (14 người gặp, nhưng 22 người chọn lý do ở Q4) — tỉ lệ nên đọc kèm mẫu số |

## Dataset 3 · Bài báo phản ánh tranh chấp trả hàng trên Shopee (nguồn `data_that` cho bộ câu thử)

| | |
|---|---|
| Dùng để làm gì | tình huống thật (nhận sai hàng, thiếu video, quá hạn, "video đối video") để viết câu thử `source = data_that`, nhất là câu `kho` · đối chiếu chéo với khảo sát |
| Từ đâu | 5 bài báo công khai: Tuổi Trẻ / Người Lao Động (2 bài), VnExpress, Dân Trí, Doanh Nhân VN — danh sách link ở `evidence/data-mining.md` mục 4 |
| Xử lý những bước gì | tìm theo từ khoá `"Shopee" "trả hàng hoàn tiền" / "từ chối hoàn tiền" / "video mở hàng"` · đọc và tóm 1 dòng mỗi bài · chỉ lưu link + tóm tắt, không chép bài · đếm thủ công theo 2 tiêu chí (kết quả ở `evidence/data-mining.md` mục 3) |
| Số dòng / số đoạn | 5 bài |
| Phiên bản / ngày lấy | đọc ngày 27/11/2026 · năm đăng trải từ 2019 đến 2025 |
| Nhãn | thật |
| Giới hạn | n nhỏ, chọn theo vụ nổi cộm nên lệch về ca nặng · **phần lớn bài đăng trước chính sách hiện hành (hiệu lực 06/11/2026)** → tình huống dùng được, nhưng quy định nêu trong bài có thể đã cũ; `expected` của câu thử luôn chấm theo `data/shopee_policy.md`, không theo bài báo |

## Data `synthetic` / nhóm tự viết

Tính đến CP2 nhóm **không sinh dữ liệu bằng script hay model**. Câu thử `source = tu_viet` (chủ yếu câu `tu_choi` / tấn công) do Nguyễn Mạnh Quân tự viết, người kiểm: __ · số câu: 5/15 (theo `python run.py check` ngày 27/11). Câu tự viết **không phải bằng chứng pain**.
