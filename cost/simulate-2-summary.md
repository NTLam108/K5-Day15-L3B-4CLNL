# Tóm tắt mô phỏng simulate-2@20261128-105127

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| don_nho_bo_som | 7 | 1 | 1093 | 178 | 1.0 | 1.0 |
| trung_binh_may_mo | 11 | 2 | 2236 | 352 | 2.0 | 2.0 |
| don_cao_lam_toi_cung | 1 | 3 | 3331 | 518 | 3.0 | 3.0 |

Tỉ lệ đạt dùng để tính: 19/24 (79%) — lượt run-2@20261128-093903

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from). ⚠️ Lượt này chạy bằng openai/gpt-oss-20b, mô phỏng đo trên gpt-4o-mini-2024-07-18 — khác model.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (5.000 người) | Chi phí / tháng — cơ sở (20.000 người) | Chi phí / tháng — cao (50.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.00046 (≈ 12 ₫) | $0.00058 (≈ 15 ₫) | $0.00034 (≈ 9 ₫) | $1.26 (≈ 32.121 ₫) | $5.06 (≈ 128.483 ₫) | $12.65 (≈ 321.208 ₫) | $0.00025 (≈ 6 ₫) |
| openai/gpt-oss-120b (vào 0.15 · ra 0.6 $/1M) | $0.00046 (≈ 12 ₫) | $0.00058 (≈ 15 ₫) | $0.00034 (≈ 9 ₫) | $1.26 (≈ 32.121 ₫) | $5.06 (≈ 128.483 ₫) | $12.65 (≈ 321.208 ₫) | $0.00025 (≈ 6 ₫) |
| openai/gpt-oss-20b (vào 0.075 · ra 0.3 $/1M) | $0.00023 (≈ 6 ₫) | $0.00029 (≈ 7 ₫) | $0.00017 (≈ 4 ₫) | $0.6323 (≈ 16.060 ₫) | $2.53 (≈ 64.242 ₫) | $6.32 (≈ 160.604 ₫) | $0.00013 (≈ 3 ₫) |
| gemini-2.5-flash-lite (vào 0.1 · ra 0.4 $/1M) | $0.00031 (≈ 8 ₫) | $0.00039 (≈ 10 ₫) | $0.00023 (≈ 6 ₫) | $0.8431 (≈ 21.414 ₫) | $3.37 (≈ 85.655 ₫) | $8.43 (≈ 214.139 ₫) | $0.00017 (≈ 4 ₫) |
| gemini-2.5-flash (vào 0.3 · ra 2.5 $/1M) | $0.0013 (≈ 33 ₫) | $0.0016 (≈ 42 ₫) | $0.00098 (≈ 25 ₫) | $3.59 (≈ 91.217 ₫) | $14.36 (≈ 364.868 ₫) | $35.91 (≈ 912.171 ₫) | $0.00072 (≈ 18 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00091 (≈ 23 ₫) | $0.0012 (≈ 29 ₫) | $0.00068 (≈ 17 ₫) | $2.52 (≈ 63.910 ₫) | $10.06 (≈ 255.639 ₫) | $25.16 (≈ 639.098 ₫) | $0.00050 (≈ 13 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0050 (≈ 128 ₫) | $0.0064 (≈ 162 ₫) | $0.0038 (≈ 96 ₫) | $13.87 (≈ 352.333 ₫) | $55.49 (≈ 1.409.334 ₫) | $138.71 (≈ 3.523.335 ₫) | $0.0028 (≈ 70 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.7) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-4o-mini-2024-07-18. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 31/50.
- Tỷ giá: 1 USD = 25.400 ₫ (tỷ giá tham khảo thị trường ~25.400 VND/USD (xem 27/11/2026)).
