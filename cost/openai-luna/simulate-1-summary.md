# Tóm tắt mô phỏng simulate-1@20261128-110500

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| don_nho_bo_som | 16 | 1 | 1111 | 791 | 1.0 | 1.0 |
| trung_binh_may_mo | 26 | 2 | 2213 | 1617 | 2.0 | 2.0 |
| don_cao_lam_toi_cung | 8 | 3 | 3337 | 2391 | 3.0 | 3.0 |

Tỉ lệ đạt dùng để tính: **chưa có** lượt eval chấm xong chạy bằng gpt-6-luna. Lượt chấm gần nhất (run-2@20261128-093903) chạy bằng openai/gpt-oss-20b — model khác, nên KHÔNG dùng tỉ lệ đạt đó → chưa tính chi phí / task thành công. Chạy `python run.py eval` bằng đúng model này, chấm xong (`python run.py score …`) rồi chạy lại simulate.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (5.000 người) | Chi phí / tháng — cơ sở (20.000 người) | Chi phí / tháng — cao (50.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-6-luna (vào 0.1 · ra 0.5 $/1M) | $0.00094 (≈ 24 ₫) | — | — | $2.38 (≈ 60.432 ₫) | $9.52 (≈ 241.729 ₫) | $23.79 (≈ 604.323 ₫) | $0.00048 (≈ 12 ₫) |
| gemini-2.5-flash-lite (vào 0.1 · ra 0.4 $/1M) | $0.00079 (≈ 20 ₫) | — | — | $2.01 (≈ 50.965 ₫) | $8.03 (≈ 203.861 ₫) | $20.07 (≈ 509.654 ₫) | $0.00040 (≈ 10 ₫) |
| gemini-2.5-flash (vào 0.3 · ra 2.5 $/1M) | $0.0043 (≈ 109 ₫) | — | — | $10.86 (≈ 275.966 ₫) | $43.46 (≈ 1.103.864 ₫) | $108.65 (≈ 2.759.660 ₫) | $0.0022 (≈ 55 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0027 (≈ 69 ₫) | — | — | $6.88 (≈ 174.748 ₫) | $27.52 (≈ 698.992 ₫) | $68.80 (≈ 1.747.480 ₫) | $0.0014 (≈ 35 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0141 (≈ 359 ₫) | — | — | $35.69 (≈ 906.484 ₫) | $142.75 (≈ 3.625.936 ₫) | $356.88 (≈ 9.064.840 ₫) | $0.0071 (≈ 181 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-6-luna. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.400 ₫ (tỷ giá tham khảo thị trường ~25.400 VND/USD (xem 27/11/2026)).
