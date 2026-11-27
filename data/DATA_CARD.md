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

**Data `synthetic` (nhóm tự sinh):** ghi cách sinh (prompt / script), seed, người kiểm, số dòng đã kiểm tay. Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · [tên]

…
