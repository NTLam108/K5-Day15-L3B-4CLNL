# Tóm tắt mô phỏng simulate-3@20261128-110615

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| don_nho_bo_som | 16 | 1 | 1111 | 772 | 1.0 | 1.0 |
| trung_binh_may_mo | 26 | 2 | 2213 | 1702 | 2.0 | 2.0 |
| don_cao_lam_toi_cung | 8 | 3 | 3337 | 2320 | 3.0 | 3.0 |

Tỉ lệ đạt dùng để tính: 19/24 (79%) — lượt run-2@20261128-093903

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from). ⚠️ Lượt này chạy bằng openai/gpt-oss-20b, mô phỏng đo trên gpt-6-luna — khác model.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (5.000 người) | Chi phí / tháng — cơ sở (20.000 người) | Chi phí / tháng — cao (50.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-6-luna (vào 0.1 · ra 0.5 $/1M) | $0.00096 (≈ 24 ₫) | $0.0012 (≈ 31 ₫) | $0.00066 (≈ 17 ₫) | $2.41 (≈ 61.116 ₫) | $9.62 (≈ 244.464 ₫) | $24.06 (≈ 611.160 ₫) | $0.00048 (≈ 12 ₫) |
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.0012 (≈ 31 ₫) | $0.0015 (≈ 39 ₫) | $0.00083 (≈ 21 ₫) | $3.04 (≈ 77.268 ₫) | $12.17 (≈ 309.074 ₫) | $30.42 (≈ 772.685 ₫) | $0.00061 (≈ 15 ₫) |
| openai/gpt-oss-120b (vào 0.15 · ra 0.6 $/1M) | $0.0012 (≈ 31 ₫) | $0.0015 (≈ 39 ₫) | $0.00083 (≈ 21 ₫) | $3.04 (≈ 77.268 ₫) | $12.17 (≈ 309.074 ₫) | $30.42 (≈ 772.685 ₫) | $0.00061 (≈ 15 ₫) |
| openai/gpt-oss-20b (vào 0.075 · ra 0.3 $/1M) | $0.00060 (≈ 15 ₫) | $0.00076 (≈ 19 ₫) | $0.00041 (≈ 11 ₫) | $1.52 (≈ 38.634 ₫) | $6.08 (≈ 154.537 ₫) | $15.21 (≈ 386.342 ₫) | $0.00030 (≈ 8 ₫) |
| gemini-2.5-flash-lite (vào 0.1 · ra 0.4 $/1M) | $0.00081 (≈ 20 ₫) | $0.0010 (≈ 26 ₫) | $0.00055 (≈ 14 ₫) | $2.03 (≈ 51.512 ₫) | $8.11 (≈ 206.049 ₫) | $20.28 (≈ 515.123 ₫) | $0.00041 (≈ 10 ₫) |
| gemini-2.5-flash (vào 0.3 · ra 2.5 $/1M) | $0.0044 (≈ 111 ₫) | $0.0055 (≈ 140 ₫) | $0.0030 (≈ 76 ₫) | $11.00 (≈ 279.384 ₫) | $44.00 (≈ 1.117.538 ₫) | $109.99 (≈ 2.793.845 ₫) | $0.0022 (≈ 56 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0028 (≈ 70 ₫) | $0.0035 (≈ 89 ₫) | $0.0019 (≈ 48 ₫) | $6.96 (≈ 176.799 ₫) | $27.84 (≈ 707.196 ₫) | $69.61 (≈ 1.767.991 ₫) | $0.0014 (≈ 35 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0143 (≈ 364 ₫) | $0.0181 (≈ 460 ₫) | $0.0098 (≈ 250 ₫) | $36.09 (≈ 916.740 ₫) | $144.37 (≈ 3.666.958 ₫) | $360.92 (≈ 9.167.396 ₫) | $0.0072 (≈ 183 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-6-luna. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.400 ₫ (tỷ giá tham khảo thị trường ~25.400 VND/USD (xem 27/11/2026)).
