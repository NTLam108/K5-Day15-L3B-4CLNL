# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11.
> Số **không điền tay**: sinh từ `cost/personas.yaml` → `python run.py simulate --rate-from eval/run-2.csv --wait 15` → chép bảng trong `cost/simulate-1-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu khớp `spec.md` §2 (`don_nho_bo_som` 45%, 0.5 lần/tháng, 1 lượt · `trung_binh_may_mo` 40%, 0.6 lần/tháng, 2 lượt · `don_cao_lam_toi_cung` 15%, 0.5 lần/tháng, 3 lượt). Nguồn: khảo sát Q3 (`n = 24`, `evidence/survey/results.csv`) & phỏng vấn `P1–P3` (`evidence/interviews/`).
- **Số người dùng thật** 3 kịch bản: thấp `5.000` · cơ sở `20.000` · cao `50.000` người/tháng. Nguồn: Shopee Mall Việt Nam đạt 28 triệu người mua sắm tích cực ([VnEconomy](https://vneconomy.vn/shopee-tiep-tuc-tang-truong-voi-chien-luoc-nguoi-dung-lam-trung-tam.htm), xem 27/11/2026); 3 mức quy mô nhóm người mua 18–30 tuổi dùng trợ lý đổi trả là *(tự ước tính)*.
- **Giá** 5 mức model (gồm chính model đang đo `openai/gpt-oss-20b` và 4 mức tham chiếu, xem 27–28/11/2026):
  - `openai/gpt-oss-20b`: $0.075 / 1M vào · $0.30 / 1M ra ([Groq Docs](https://console.groq.com/docs/models), xem 28/11/2026)
  - `gemini-2.5-flash-lite`: $0.10 / 1M vào · $0.40 / 1M ra ([Google AI Pricing](https://ai.google.dev/gemini-api/docs/pricing), xem 27/11/2026)
  - `gemini-3.1-flash-lite`: $0.25 / 1M vào · $1.50 / 1M ra (`further-reading/model-prices.md`)
  - `gemini-2.5-flash`: $0.30 / 1M vào · $2.50 / 1M ra ([Google AI Pricing](https://ai.google.dev/gemini-api/docs/pricing), xem 27/11/2026)
  - `gemini-4-hydrogen`: $1.50 / 1M vào · $7.50 / 1M ra (`further-reading/model-prices.md`)
- **Tỉ lệ đạt** dùng để tính: **19/24 (79%)** — lượt `run-2@20261128-093903` (`eval/run-2.csv`).
- Đo token trên model `openai/gpt-oss-20b` (Groq), tính giá model `openai/gpt-oss-20b` (đo và tính cùng model) và các model tham chiếu `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3.1-flash-lite`, `gemini-4-hydrogen` (lưu ý: model khác bộ tách token thì số token thật có thể lệch).

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-101751` · `50` phiên (38 phiên thành công, 12 phiên cuối hết quota ngày Groq, không sửa tay; đủ cả 3 persona: `don_nho_bo_som` 12 · `trung_binh_may_mo` 22 · `don_cao_lam_toi_cung` 4) · seed `42` · tỷ giá `1 USD = 25.400 ₫`.

*(Chép nguyên bảng từ `cost/simulate-1-summary.md`)*

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (5.000 người) | Chi phí / tháng — cơ sở (20.000 người) | Chi phí / tháng — cao (50.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **openai/gpt-oss-20b** (vào 0.075 · ra 0.3 $/1M — *cùng model đo*) | $0.00061 (≈ 16 ₫) | $0.00077 (≈ 20 ₫) | $0.00043 (≈ 11 ₫) | $1.60 (≈ 40.619 ₫) | $6.40 (≈ 162.478 ₫) | $15.99 (≈ 406.194 ₫) | $0.00032 (≈ 8 ₫) |
| gemini-2.5-flash-lite (vào 0.1 · ra 0.4 $/1M) | $0.00082 (≈ 21 ₫) | $0.0010 (≈ 26 ₫) | $0.00058 (≈ 15 ₫) | $2.13 (≈ 54.159 ₫) | $8.53 (≈ 216.637 ₫) | $21.32 (≈ 541.592 ₫) | $0.00043 (≈ 11 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0028 (≈ 71 ₫) | $0.0035 (≈ 90 ₫) | $0.0020 (≈ 50 ₫) | $7.31 (≈ 185.795 ₫) | $29.26 (≈ 743.180 ₫) | $73.15 (≈ 1.857.951 ₫) | $0.0015 (≈ 37 ₫) |
| gemini-2.5-flash (vào 0.3 · ra 2.5 $/1M) | $0.0044 (≈ 113 ₫) | $0.0056 (≈ 142 ₫) | $0.0031 (≈ 79 ₫) | $11.56 (≈ 293.510 ₫) | $46.22 (≈ 1.174.040 ₫) | $115.56 (≈ 2.935.100 ₫) | $0.0023 (≈ 59 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0145 (≈ 369 ₫) | $0.0184 (≈ 467 ₫) | $0.0103 (≈ 261 ₫) | $37.94 (≈ 963.579 ₫) | $151.74 (≈ 3.854.316 ₫) | $379.36 (≈ 9.635.790 ₫) | $0.0076 (≈ 193 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (79%) — **không coi như đạt 100%**.

## 3. So với impact

- **Impact / người / tháng (`spec.md` §2):** Mỗi người mua gặp hàng lỗi (~0.5 lần/tháng) đang tốn trung bình **~21 phút/lần** (tức ~10.5 phút/tháng; người làm tới cùng mất 35–50 phút) để đọc chính sách, tìm mẹo và chuẩn bị bằng chứng, chưa kể rủi ro bỏ cuộc mất tiền (7/24 người khảo sát).
- **Chi phí / người / tháng (cơ sở, model `openai/gpt-oss-20b`):** **$0.00032 (≈ 8 ₫) / người / tháng** (chỉ **20 ₫ / task thành công**); tổng chi phí vận hành 20.000 người dùng/tháng chỉ **$6.40 (≈ 162.478 ₫)**. Ngay cả khi dùng model mạnh `gemini-4-hydrogen`, chi phí cũng chỉ **193 ₫ / người / tháng** (~3.85 triệu ₫/tháng cho 20.000 người).
- **Kết luận một dòng — đáng làm không:** **Rất đáng làm** — chỉ tốn khoảng **8 ₫ / người / tháng** (hoặc **20 ₫ cho mỗi ca tư vấn thành công**) để tiết kiệm ~10–20 phút tìm hiểu chính sách và giảm nguy cơ mất tiền oan trên các đơn hàng hàng chục đến hàng trăm nghìn đồng.
