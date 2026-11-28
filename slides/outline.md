# Dàn slide → lấy số từ file nào

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11. Định dạng nào cũng được (PDF, PPTX, HTML…); hoặc nộp link slide (Drive, Canva, Google Slides…) ở form CP4, để ai có link cũng xem được.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 1 | Người dùng & pain | Ai · việc gì · chỗ đau + số và trích dẫn | `evidence/summary.md` | ☑ |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn + hướng bị loại | `spec.md` §2 | ☑ |
| 3 | Giải pháp | Lát cắt một câu · sơ đồ · AI tự làm đến đâu, vì sao | `spec.md` §4 | ☑ |
| 4 | Demo live | 1 trường hợp thường + 1 trường hợp khó (lấy từ bộ câu thử); mạng hỏng → video dự phòng | `eval/benchmark.csv` | ☑ |
| 5 | **Đánh giá thế nào** | Dataset · bộ câu thử · metric · lượt 1 → lượt 2 so với chuẩn "đạt" (kèm run ID) · lỗi chính | `eval/README.md`, `eval/report.md` | ☑ |
| 6 | **Chi phí khi dùng thật** | Chi phí / task thành công · 3 kịch bản · so với impact | `cost/cost-estimate.md` | ☑ |
| 7 | Kết luận | Go / iterate / stop — dẫn số ở trang 1, 5, 6 | — | ☑ |
| 8 | Nếu có thêm 1 tuần | 2–3 việc, trỏ về lỗi còn lại / phản hồi người dùng | `eval/report.md` mục 4 · `validation/log.md` | ☑ |

**Trước khi lên:** tải repo về một máy khác (hoặc thư mục mới), chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · biết bản chạy thử sẽ làm gì với **1 câu thử lạ** của giám khảo.

Ai nói trang nào (mỗi người ≥1 phần):

| Trang | Người nói |
|---|---|
| 1 Bìa (tên đề tài, nhóm, 3 số chính) | Nguyễn Trọng Lâm |
| 2 Người dùng & pain · 3 Vì sao chọn bài này | Vũ Xuân Hiếu |
| 4 Giải pháp (workflow 6 bước) · 5 Người mua đang làm gì / khác trợ lý AI Shopee | Nguyễn Trọng Lâm |
| 6 Demo live | Nguyễn Đức Hiếu (chạy máy), Nguyễn Trọng Lâm (dẫn) |
| 7 Đánh giá định lượng & cải tiến (slide của Quân) | Nguyễn Mạnh Quân |
| 8 Chi phí khi dùng thật | Vũ Xuân Hiếu |
| 9 Rủi ro & an toàn | Nguyễn Đức Hiếu |
| 10 Kết luận (ITERATE) + nếu có thêm 1 tuần | Nguyễn Trọng Lâm |

File slide: `demo-slides.pdf` (thư mục gốc, **10 trang**) — nguồn HTML `slides/demo-slides.html` (sửa HTML rồi in lại PDF). Trang 7 nhúng nguyên `slides/slide-05-danh-gia.html` của Nguyễn Mạnh Quân (đánh giá định lượng + một lần cải tiến, thay cho trang 5 trong dàn 8 trang ở trên); trang 1 (bìa), 5 (luồng hiện tại + so với trợ lý AI Shopee) và 9 (rủi ro & an toàn) là trang thêm.
