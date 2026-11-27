# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Nối API Groq và chuẩn hóa dấu gạch nối trong mã nguồn trích dẫn | Cần thành viên nhóm kiểm tra và duyệt | Nguyễn Đức Hiếu |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | Antigravity (Gemini) | Chỉ rà câu dẫn dắt, góp ý cấu trúc câu hỏi Mom Test & tạo khung Google Form ẩn danh | Người tự kiểm toàn bộ câu hỏi, tự thu 24 phản hồi thật & tự phỏng vấn 3 người (P1–P3) ngoài nhóm | Vũ Xuân Hiếu |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | Antigravity (Gemini) | Hỗ trợ chuẩn hóa định dạng Markdown cho `evidence/data-mining.md`, `evidence/summary.md`, `cost/personas.yaml` | Kiểm tra lại 100% số liệu khớp với `results.csv` (n = 24), link bài báo thật & nội dung phỏng vấn P1–P3 | Vũ Xuân Hiếu |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
