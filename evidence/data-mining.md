# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Không đào data thì xoá file này. Script / công thức đếm để trong repo (vd `evidence/count.py` hoặc ghi công thức Sheets ngay dưới), người khác chạy lại phải ra cùng số.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

## 1. Cách đếm — viết TRƯỚC khi chạy

- Data dùng: Các bài báo và phản ánh công khai trên báo chí Việt Nam (Tuổi Trẻ / Người Lao Động, VnExpress, Dân Trí, Doanh Nhân VN) về chính sách và tranh chấp trả hàng/hoàn tiền trên Shopee.
- Đếm gì: Các trường hợp / lý do phổ biến dẫn đến tranh chấp hoặc bị từ chối trả hàng/hoàn tiền trên Shopee · trên tập: bài báo & phản ánh tìm theo từ khóa `"Shopee" "trả hàng hoàn tiền" / "từ chối hoàn tiền" / "video mở hàng"`.
- **Mẫu số là gì:** Tổng số bài phản ánh thu thập được (N = 5 bài báo có link công khai).
- Script / công thức: Tổng hợp thủ công từ tìm kiếm báo chí công khai, lưu kèm URL gốc để kiểm chứng lại.

## 2. Đọc trước, đếm sau

Đã đọc 5 bài báo phản ánh công khai. Các *kiểu* vấn đề thường gặp thấy được:
- Người mua bị từ chối hoàn tiền vì thiếu video mở hộp (unboxing) quay liền mạch từ lúc còn tem niêm phong, hoặc quá hạn báo cáo.
- Shopee liên tục siết/thay đổi điều kiện trả hàng (nhất là nhóm lý do "không còn nhu cầu"), gây tranh cãi và khiến người dùng không rõ trường hợp của mình có được duyệt không.
- Tranh chấp "video đối video" giữa người mua và người bán khiến cả hai phía đều dễ mất quyền lợi nếu thiếu bằng chứng đúng chuẩn.

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| Bài phản ánh nhắc đến yêu cầu bằng chứng video khui/đóng hàng hoặc quy trình khắt khe | 4 / 5 | 80% | VnExpress, Dân Trí, Tuổi Trẻ, Doanh Nhân VN |
| Bài phản ánh việc Shopee siết/thay đổi chính sách gây lúng túng/tranh cãi | 2 / 5 | 40% | Báo Người Lao Động / Tuổi Trẻ |

## 4. ≥5 ví dụ cụ thể (mã dòng / mã đã ẩn danh, không đoán ai là ai)

1. **"Shopee siết chính sách trả hàng, nhà bán và người mua tranh cãi"** — Báo Người Lao Động (Tuổi Trẻ): https://tuoitre.vn/nld/shopee-siet-chinh-sach-tra-hang-nha-ban-va-nguoi-mua-tranh-cai-196251120152348228.htm — *Phản ánh tranh cãi khi sàn siết điều kiện trả hàng/hoàn tiền, người mua lúng túng không rõ trường hợp nào được duyệt.*
2. **"Shopee siết chính sách trả hàng hoàn tiền"** — Báo Người Lao Động (Tuổi Trẻ): https://tuoitre.vn/nld/shopee-siet-chinh-sach-tra-hang-hoan-tien-196251118200238959.htm — *Chi tiết thay đổi điều kiện giữ nguyên trạng và nhóm đối tượng áp dụng.*
3. **"Mua iPhone 14 Pro Max trên Shopee, nhận về cục gỗ"** — Báo VnExpress: https://vnexpress.net/mua-iphone-14-pro-max-tren-shopee-nhan-ve-cuc-go-4558552.html — *Trường hợp nhận sai hoàn toàn sản phẩm; nhấn mạnh vai trò sống còn của video khui hàng và báo cáo đúng hạn.*
4. **"Sơ ý khi mua hàng trên Shopee, nhiều người nhận cú lừa kinh điển"** — Báo Dân Trí: https://dantri.com.vn/cong-nghe/so-y-khi-mua-hang-tren-shopee-nhieu-nguoi-nhan-cu-lua-kinh-dien-20190905134537662.htm — *Người mua mất quyền bảo vệ hoàn tiền do làm sai quy trình/thiếu bằng chứng hoặc quá hạn.*
5. **"Yêu cầu trả hàng, hoàn tiền từ khách hàng gây bức xúc cho người bán trên sàn TMĐT Shopee"** — Doanh Nhân VN: https://doanhnhanvn.vn/yeu-cau-tra-hang-hoan-tien-tu-khach-hang-gay-buc-xuc-cho-nguoi-ban-tren-san-tmdt-shopee.html — *Phản ánh cơ chế "video đối video" khiến cả người mua lẫn người bán dễ bị xử thua nếu thiếu video chuẩn.*

## 5. Giới hạn của data

Data báo chí phản ánh các vụ việc điển hình/nổi cộm, chưa cho biết tỷ lệ chính xác trong nhóm sinh viên/nhân viên văn phòng (18–30 tuổi) khi gặp hàng lỗi thông thường.
→ Kiểm lại bằng: Khảo sát Google Form (`evidence/survey/`, n = 22) và phỏng vấn trực tiếp 3–5 người (`evidence/interviews/`).
