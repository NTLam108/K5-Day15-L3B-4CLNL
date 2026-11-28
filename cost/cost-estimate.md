# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11.
> Số **không điền tay**: sinh từ `cost/personas.yaml` → `python run.py simulate --rate-from eval/run-2.csv --wait 1` → chép bảng trong `cost/simulate-3-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu khớp `spec.md` §2 (`don_nho_bo_som` 45%, 0.5 lần/tháng, 1 lượt · `trung_binh_may_mo` 40%, 0.6 lần/tháng, 2 lượt · `don_cao_lam_toi_cung` 15%, 0.5 lần/tháng, 3 lượt). Nguồn: khảo sát Q3 (`n = 24`, `evidence/survey/results.csv`) & phỏng vấn `P1–P3` (`evidence/interviews/`).
- **Số người dùng thật** 3 kịch bản: thấp `5.000` · cơ sở `20.000` · cao `50.000` người/tháng. Nguồn: Shopee Mall Việt Nam đạt 28 triệu người mua sắm tích cực ([VnEconomy](https://vneconomy.vn/shopee-tiep-tuc-tang-truong-voi-chien-luoc-nguoi-dung-lam-trung-tam.htm), xem 27/11/2026); 3 mức quy mô nhóm người mua 18–30 tuổi dùng trợ lý đổi trả là *(tự ước tính)*.
- **Giá** 8 mức model (gồm `gpt-6-luna` đang đo 50/50 phiên, `openai/gpt-oss-20b` dùng ở `run-2`, và các mức tham chiếu):
  - `gpt-6-luna`: $0.10 / 1M vào · $0.50 / 1M ra ([OpenAI Docs](https://developers.openai.com/api/docs/models/gpt-6-luna), xem 28/11/2026)
  - `gpt-4o-mini`: $0.15 / 1M vào · $0.60 / 1M ra ([OpenAI Pricing](https://openai.com/api/pricing/), xem 28/11/2026)
  - `openai/gpt-oss-20b`: $0.075 / 1M vào · $0.30 / 1M ra ([Groq Docs](https://console.groq.com/docs/models), xem 28/11/2026)
  - `openai/gpt-oss-120b`: $0.15 / 1M vào · $0.60 / 1M ra ([Groq Docs](https://console.groq.com/docs/models), xem 28/11/2026)
  - `gemini-2.5-flash-lite`: $0.10 / 1M vào · $0.40 / 1M ra ([Google AI Pricing](https://ai.google.dev/gemini-api/docs/pricing), xem 27/11/2026)
  - `gemini-3.1-flash-lite`: $0.25 / 1M vào · $1.50 / 1M ra (`further-reading/model-prices.md`)
  - `gemini-2.5-flash`: $0.30 / 1M vào · $2.50 / 1M ra ([Google AI Pricing](https://ai.google.dev/gemini-api/docs/pricing), xem 27/11/2026)
  - `gemini-4-hydrogen`: $1.50 / 1M vào · $7.50 / 1M ra (`further-reading/model-prices.md`)
- **Tỉ lệ đạt** dùng để tính: **19/24 (79%)** — lượt `run-2@20261128-093903` (`eval/run-2.csv`, chạy trên `openai/gpt-oss-20b`).
- Đo token trên model **`gpt-6-luna`** (50/50 phiên thành công, `0/50` lỗi), tính giá model `gpt-6-luna` (cùng model đo) và các model tham chiếu (lưu ý: `eval/run-2.csv` đo tỉ lệ đạt trên `openai/gpt-oss-20b`, model khác bộ tách token thì số token thật có thể lệch nhẹ; nhóm giữ nguyên kết quả `simulate-1` trên `openai/gpt-oss-20b` trong repo để đối chiếu chéo).

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-3.csv` · run ID `simulate-3@20261128-110615` · `50` phiên (**50/50 thành công, 0 lỗi**; đủ cả 3 persona: `don_nho_bo_som` 16 · `trung_binh_may_mo` 26 · `don_cao_lam_toi_cung` 8) · seed `42` · tỷ giá `1 USD = 25.400 ₫`.

*(Chép nguyên bảng từ `cost/simulate-3-summary.md`)*

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (5.000 người) | Chi phí / tháng — cơ sở (20.000 người) | Chi phí / tháng — cao (50.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **gpt-6-luna** (vào 0.1 · ra 0.5 $/1M — *cùng model đo*) | $0.00096 (≈ 24 ₫) | $0.0012 (≈ 31 ₫) | $0.00066 (≈ 17 ₫) | $2.41 (≈ 61.116 ₫) | $9.62 (≈ 244.464 ₫) | $24.06 (≈ 611.160 ₫) | $0.00048 (≈ 12 ₫) |
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.0012 (≈ 31 ₫) | $0.0015 (≈ 39 ₫) | $0.00083 (≈ 21 ₫) | $3.04 (≈ 77.268 ₫) | $12.17 (≈ 309.074 ₫) | $30.42 (≈ 772.685 ₫) | $0.00061 (≈ 15 ₫) |
| openai/gpt-oss-120b (vào 0.15 · ra 0.6 $/1M) | $0.0012 (≈ 31 ₫) | $0.0015 (≈ 39 ₫) | $0.00083 (≈ 21 ₫) | $3.04 (≈ 77.268 ₫) | $12.17 (≈ 309.074 ₫) | $30.42 (≈ 772.685 ₫) | $0.00061 (≈ 15 ₫) |
| openai/gpt-oss-20b (vào 0.075 · ra 0.3 $/1M) | $0.00060 (≈ 15 ₫) | $0.00076 (≈ 19 ₫) | $0.00041 (≈ 11 ₫) | $1.52 (≈ 38.634 ₫) | $6.08 (≈ 154.537 ₫) | $15.21 (≈ 386.342 ₫) | $0.00030 (≈ 8 ₫) |
| gemini-2.5-flash-lite (vào 0.1 · ra 0.4 $/1M) | $0.00081 (≈ 20 ₫) | $0.0010 (≈ 26 ₫) | $0.00055 (≈ 14 ₫) | $2.03 (≈ 51.512 ₫) | $8.11 (≈ 206.049 ₫) | $20.28 (≈ 515.123 ₫) | $0.00041 (≈ 10 ₫) |
| gemini-2.5-flash (vào 0.3 · ra 2.5 $/1M) | $0.0044 (≈ 111 ₫) | $0.0055 (≈ 140 ₫) | $0.0030 (≈ 76 ₫) | $11.00 (≈ 279.384 ₫) | $44.00 (≈ 1.117.538 ₫) | $109.99 (≈ 2.793.845 ₫) | $0.0022 (≈ 56 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0028 (≈ 70 ₫) | $0.0035 (≈ 89 ₫) | $0.0019 (≈ 48 ₫) | $6.96 (≈ 176.799 ₫) | $27.84 (≈ 707.196 ₫) | $69.61 (≈ 1.767.991 ₫) | $0.0014 (≈ 35 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0143 (≈ 364 ₫) | $0.0181 (≈ 460 ₫) | $0.0098 (≈ 250 ₫) | $36.09 (≈ 916.740 ₫) | $144.37 (≈ 3.666.958 ₫) | $360.92 (≈ 9.167.396 ₫) | $0.0072 (≈ 183 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (79%) — **không coi như đạt 100%**.

## 3. So với impact

- **Impact / người / tháng (`spec.md` §2):** Mỗi người mua gặp hàng lỗi (~0.5 lần/tháng) đang tốn trung bình **~21 phút/lần** (tức ~10.5 phút/tháng; người làm tới cùng mất 35–50 phút) để đọc chính sách, tìm mẹo và chuẩn bị bằng chứng, chưa kể rủi ro bỏ cuộc mất tiền (7/24 người khảo sát).
- **Chi phí / người / tháng (cơ sở, model `gpt-6-luna`):** **$0.00048 (≈ 12 ₫) / người / tháng** (chỉ **31 ₫ / task thành công**); tổng chi phí vận hành 20.000 người dùng/tháng chỉ **$9.62 (≈ 244.464 ₫)**. Nếu dùng model rẻ hơn (`openai/gpt-oss-20b`), chi phí chỉ **8 ₫ / người / tháng** (~154.537 ₫/tháng cho 20.000 người); ngay cả khi dùng model mạnh `gemini-4-hydrogen` cũng chỉ **183 ₫ / người / tháng**.
- **Kết luận một dòng — đáng làm không:** **Rất đáng làm** — chỉ tốn khoảng **12 ₫ / người / tháng** (hoặc **31 ₫ cho mỗi ca tư vấn thành công** trên `gpt-6-luna`) để tiết kiệm ~10–20 phút tìm hiểu chính sách và giảm nguy cơ mất tiền oan trên các đơn hàng hàng chục đến hàng trăm nghìn đồng.
