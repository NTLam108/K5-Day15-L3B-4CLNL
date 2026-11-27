# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Nối API Groq và chuẩn hóa dấu gạch nối trong mã nguồn trích dẫn | Cần thành viên nhóm kiểm tra và duyệt | Nguyễn Đức Hiếu |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | Antigravity (Gemini) | Chỉ rà câu dẫn dắt, góp ý cấu trúc câu hỏi Mom Test & tạo khung Google Form ẩn danh | Người tự kiểm toàn bộ câu hỏi, tự thu 24 phản hồi thật & tự phỏng vấn 3 người (P1–P3) ngoài nhóm | Vũ Xuân Hiếu |
| Viết câu thử (benchmark) | Gemini (Antigravity) | Hỗ trợ chuẩn hoá cấu trúc `eval/benchmark.csv` (24 câu), đối chiếu mã `SP-01`..`SP-35` và rà nhãn `expected` theo `metric_spec.yaml`; 19/24 câu lấy từ khảo sát/phỏng vấn/chính sách thật (`nguoi_dung`/`data_that`), 5/24 câu `tu_viet` ghi rõ nguồn | Nguyễn Mạnh Quân đọc sửa từng câu, đối chiếu với phỏng vấn P1–P3 & khảo sát `n=24`; Nguyễn Đức Hiếu kiểm 5/5 câu `tu_viet` (`data/DATA_CARD.md`) | Nguyễn Mạnh Quân |
| Sinh data `synthetic` (nếu có) | Không dùng | Không sinh dữ liệu `synthetic` bằng script hay model | — | Nguyễn Mạnh Quân |
| Chấm cột `pass` bằng LLM (nếu có) | Claude (chấm thử 5 output CP2) · Gemini (rà đối chiếu lượt 1) | Claude chấm thử 5 output CP2 (`eval/README.md` mục 3); Gemini hỗ trợ trích xuất đối chiếu output lượt 1 theo `metric_spec.yaml` | Chấm thử CP2: Nguyễn Đức Hiếu kiểm tay 5/5 câu, khớp 5/5; Lượt 1 (`eval/run-1.csv`): Nguyễn Mạnh Quân rà soát tay toàn bộ 24/24 câu trước khi chạy `python run.py score` | Nguyễn Mạnh Quân |
| Slide, văn bản | Antigravity (Gemini) | Hỗ trợ chuẩn hóa định dạng Markdown cho `evidence/data-mining.md`, `evidence/summary.md`, `cost/personas.yaml` | Kiểm tra lại 100% số liệu khớp với `results.csv` (n = 24), link bài báo thật & nội dung phỏng vấn P1–P3 | Vũ Xuân Hiếu |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
