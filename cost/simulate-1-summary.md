# Tóm tắt mô phỏng simulate-1@20261128-101751

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| don_nho_bo_som | 12 | 1 | 1162 | 876 | 1.0 | 1.0 |
| trung_binh_may_mo | 22 | 2 | 2334 | 1679 | 2.0 | 2.0 |
| don_cao_lam_toi_cung | 4 | 3 | 3577 | 2582 | 3.0 | 3.0 |

Tỉ lệ đạt dùng để tính: 19/24 (79%) — lượt run-2@20261128-093903

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (5.000 người) | Chi phí / tháng — cơ sở (20.000 người) | Chi phí / tháng — cao (50.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| openai/gpt-oss-20b (vào 0.075 · ra 0.3 $/1M) | $0.00061 (≈ 16 ₫) | $0.00077 (≈ 20 ₫) | $0.00043 (≈ 11 ₫) | $1.60 (≈ 40.619 ₫) | $6.40 (≈ 162.478 ₫) | $15.99 (≈ 406.194 ₫) | $0.00032 (≈ 8 ₫) |
| gemini-2.5-flash-lite (vào 0.1 · ra 0.4 $/1M) | $0.00082 (≈ 21 ₫) | $0.0010 (≈ 26 ₫) | $0.00058 (≈ 15 ₫) | $2.13 (≈ 54.159 ₫) | $8.53 (≈ 216.637 ₫) | $21.32 (≈ 541.592 ₫) | $0.00043 (≈ 11 ₫) |
| gemini-2.5-flash (vào 0.3 · ra 2.5 $/1M) | $0.0044 (≈ 113 ₫) | $0.0056 (≈ 142 ₫) | $0.0031 (≈ 79 ₫) | $11.56 (≈ 293.510 ₫) | $46.22 (≈ 1.174.040 ₫) | $115.56 (≈ 2.935.100 ₫) | $0.0023 (≈ 59 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0028 (≈ 71 ₫) | $0.0035 (≈ 90 ₫) | $0.0020 (≈ 50 ₫) | $7.31 (≈ 185.795 ₫) | $29.26 (≈ 743.180 ₫) | $73.15 (≈ 1.857.951 ₫) | $0.0015 (≈ 37 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0145 (≈ 369 ₫) | $0.0184 (≈ 467 ₫) | $0.0103 (≈ 261 ₫) | $37.94 (≈ 963.579 ₫) | $151.74 (≈ 3.854.316 ₫) | $379.36 (≈ 9.635.790 ₫) | $0.0076 (≈ 193 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: openai/gpt-oss-20b. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 12/50.
- Tỷ giá: 1 USD = 25.400 ₫ (tỷ giá tham khảo thị trường ~25.400 VND/USD (xem 27/11/2026)).
