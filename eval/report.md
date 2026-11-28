# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-222913` | 18/24 | 75% | 7/8 (88%) | 8/13 (62%) | 3/3 (100%) | chưa đạt (<80%; `tu_choi` đạt 100%) |
| 2 | `run-2@20261128-093903` | 19/24 | 79% | 8/8 (100%) | 8/13 (62%) | 3/3 (100%) | chưa đạt (<80%, thiếu 1 câu; `tu_choi` đạt 100%) |

- Model lượt 1 & lượt 2: `openai/gpt-oss-20b` (qua Groq API), 0 lỗi kỹ thuật, 0 `trace_mismatch`.
- Chi tiết theo 3 metric ở lượt 1: `ket_luan_dung` **18/21 (85.7%)** khớp nhãn bề mặt (**17/21 = 81.0%** thực chất nếu trừ `B15` bị lỗi parser ép về fallback trùng nhãn) · `trich_dieu_khoan` **21/21 (100%)** câu có kết luận đều trích ≥1 mã hợp lệ trong `SP-01`..`SP-35` (0 mã bịa) · `tu_choi_dung` **3/3 (100%)** chặn bằng code ở bước ①. Kết hợp đủ `pass_criterion` từng câu đạt **18/24 (75%)** (`B23`, `B24` đúng nhãn nhưng trượt ý cốt lõi `SP-35` và `SP-23`/`SP-30`).
- Chi tiết theo 3 metric ở lượt 2: `ket_luan_dung` **18/21 (85.7%)** thực chất (0 câu bị fallback oan; sai nhãn ở `B15`, `B21`, `B24`) · `trich_dieu_khoan` **21/21 (100%)** trích ≥1 mã hợp lệ trong `SP-01`..`SP-35` (0 mã bịa; lưu ý `B14` gán sai nội dung `SP-27` và `B24` trích nhầm `SP-28` cho `SP-30`) · `tu_choi_dung` **3/3 (100%)**. Cả 3 metric riêng đều vượt ngưỡng, nhưng kết hợp đủ `pass_criterion` từng câu đạt **19/24 (79%)** (`B14` và `B23` đúng nhãn nhưng trượt ý cốt lõi).
- Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Bước ② `tach_thong_tin` bỏ sót từ khoá / chủ đề → thiếu điều khoản quyết định đưa vào model | 3 *(+2 câu đạt nhưng thiếu mã phụ)* | `B18`, `B23`, `B24` *(và thiếu mã phụ ở `B08`, `B16`)* |
| Bước ⑤ `kiem_can_cu` không đọc được dòng `**KẾT LUẬN:**` có Markdown in đậm → hạ oan về fallback | 2 | `B09`, `B15` |
| Bước ② `tach_thong_tin` gán nhầm `bang_chung = "không"` khi câu có phủ định cục bộ | 1 *(cùng ảnh hưởng `B18`)* | `B21` |

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| `B09` | Mình mua chiếc váy trên Shopee mới nhận 3 ngày, đúng mẫu đúng size và không bị rách lỗi gì cả, nhưng mặc lên thấy không hợp màu da và mình lỡ cắt tem mác rồi. Mình chọn lý do Hàng lỗi để được miễn phí trả hàng có được không? | `KẾT LUẬN: Không chắc cần CSKH` — Mình chưa đủ căn cứ để kết luận chắc chắn cho trường hợp này. Các điều khoản liên quan nên đọc: SP-05, SP-10, … | Trong `traces/run-1.jsonl`, model thực ra đã trả lời đúng `**KẾT LUẬN:** Chưa đủ điều kiện`, nhưng vì có dấu in đậm `**` nên bước ⑤ `kiem_can_cu` kiểm `startswith("KẾT LUẬN")` bị trượt và hạ oan toàn bộ câu trả lời về fallback chung chung. |
| `B18` | Mình đặt cái ốp lưng 65k trên Shopee nhận hôm qua (1 ngày), đã thanh toán ShopeePay. Mở bọc ra thấy màu in lệch hẳn so với ảnh shop và viền cao su lem nhem. Mình không quay video mở hộp nhưng đã chụp ảnh rõ lỗi sản phẩm ngay lúc nhận… | `KẾT LUẬN: Không chắc cần CSKH` — điều khoản [SP-05] chỉ áp dụng cho "sản phẩm bị lỗi hoặc hư hại trong quá trình vận chuyển", trong khi màu in lệch không nêu rõ là lỗi do vận chuyển… | Sai `ket_luan_dung` (kỳ vọng `Đủ điều kiện`) và quên trả lời phí ship `SP-28`. Nguyên nhân ở bước ②: không bắt cụm "màu in lệch so với ảnh shop" sang chủ đề `sai_mo_ta` (`SP-07`) nên model thiếu căn cứ `SP-07`. |
| `B21` | Mình mua bàn phím cơ 600k trên Shopee nhận 3 ngày trước, đã quay clip khui vỏ hộp ngoài nhưng tối về cắm test mới thấy liệt một hàng phím số. Mình gửi yêu cầu lý do hàng lỗi thì shop từ chối vì video khui hộp chưa quay lúc test phím… | `KẾT LUẬN: Chưa đủ thông tin cần hỏi thêm` — Theo [SP-25], người mua phải cung cấp video hoặc ảnh khi nhận hàng; hiện tại bạn chưa có bằng chứng này… | Sai `ket_luan_dung` (kỳ vọng `Không chắc cần CSKH`, đang tranh chấp chờ Shopee quyết định `SP-16`). Bước ② bắt cụm "chưa quay lúc test phím" gán nhầm `bang_chung = "không"`, khiến model tưởng khách không có bằng chứng gì. |
| `B23` | Mình nhận áo sơ mi bị rách tay áo trên Shopee cách đây 3 ngày, có đủ video và ảnh lúc nhận hàng. Nhắn cho shop thì shop bảo nhận hoàn tiền không cần trả hàng 30% giá áo, hoặc nhắn Zalo để shop tự gửi áo khác… | `KẾT LUẬN: Đủ điều kiện` — nêu đúng `SP-34` (30% < 50% không hợp lệ), soạn nháp yêu cầu; **không nhắc gì về Zalo / giao dịch ngoài Shopee**. | Trượt `pass_criterion`: bỏ sót hoàn toàn cảnh báo không liên lạc/giao dịch qua Zalo ngoài hệ thống Shopee (`SP-35`) vì bước ② chưa có chủ đề `lien_lac`, gây rủi ro người mua mất bằng chứng khiếu nại. |
| `B24` | Mình nhận ấm siêu tốc bị lỗi không vào điện trên shop thường Shopee cách đây 4 ngày, có video và ảnh lúc nhận hàng. Shop im lặng không trả lời thì có bị treo luôn không, chọn Tự sắp xếp có miễn phí ship không? | `KẾT LUẬN: Đủ điều kiện` — khuyên "nộp khiếu nại tại mục Kê khai khiếu nại" và "đặt phương thức Tự sắp xếp và thanh toán phí vận chuyển". | Bước ② không bắt "shop im lặng" nên thiếu `SP-23` (tự động hoàn sau 02 ngày lịch) khiến model bịa mục "Kê khai khiếu nại"; đồng thời bỏ sót `SP-30` (hỗ trợ một phần Shopee Xu ở shop thường) và khuyên ngược chọn Tự sắp xếp chịu phí thay vì lấy tại nhà/bưu cục miễn phí (`SP-28`). |

## 3. Một lần cải tiến

- **Nhắm vào nhóm lỗi:** 3 nhóm lỗi hệ thống ở bước ② (`tach_thong_tin`) và bước ⑤ (`kiem_can_cu`) trong `codebase/agent.py` (gồm toàn bộ 6/6 câu trượt lượt 1: `B09`, `B15`, `B18`, `B21`, `B23`, `B24`). Đây là nhóm **đau nhất với người dùng** vì theo khảo sát `evidence/summary.md` (`n = 24`), 8/22 (36.4%) người mua không biết mình có đủ điều kiện trả hàng không và 7/24 (29.2%) bỏ cuộc mất trắng: nếu hệ thống hạ oan câu trả lời đúng về "Không chắc" (`B09`), bỏ sót điều kiện lỗi mô tả & bằng chứng ảnh (`B18`), hoặc quên cảnh báo giao dịch ngoài sàn qua Zalo (`B23`) và bẫy phí ship (`B24`), người mua sẽ bỏ quyền hoàn tiền hợp lệ hoặc mất bằng chứng tranh chấp.
- **Đã sửa gì** *(commit `7029863`, ghi trước lượt 2 ở `spec.md` §10, không sửa chuẩn đạt hay `expected`)*:
  1. **Bước ⑤ `kiem_can_cu`:** loại bỏ ký tự Markdown (`*_` `` ` ``) trước khi đọc dòng `KẾT LUẬN:` để không hạ oan output in đậm `**KẾT LUẬN:**` (vẫn giữ kiểm tra mã hợp lệ `SP-01`..`SP-35`).
  2. **Bước ② `tach_thong_tin` — bổ sung từ khóa chủ đề:** mở rộng nhận diện lỗi/khác mô tả (`lem nhem`, `lệch ... ảnh/hình/mô tả`), người bán im lặng (`im lặng`, `không/chưa trả lời/phản hồi`), phí trả hàng (`mất phí`, `phí gửi`, `ship hoàn`) và thêm chủ đề `lien_lac` (`zalo`, `facebook`, `messenger`, `ngoài sàn/shopee/hệ thống`) để bước ③ tra đủ `SP-07`, `SP-23`, `SP-28`, `SP-30`, `SP-35`.
  3. **Bước ② `tach_thong_tin` — tách vế khi nhận diện bằng chứng:** tách câu theo liên từ/dấu câu (`nhưng`, `tuy nhiên`, `còn`, `mà`, `.`, `;`), trả `"có nhưng có phần chưa rõ"` khi có cả vế khẳng định và vế phủ định cục bộ thay vì gán cứng `"không"`.
- **Kết quả:**
  - Nhóm lỗi parser bước ⑤ (`B09`, `B15`): **0/2 → 1/2** (`B09` đạt; **0/24** câu bị hạ oan ở lượt 2, đồng thời cứu `B03`, `B16`, `B20` xuất `**KẾT LUẬN:**`; riêng `B15` không còn bị fallback che khuất nên lộ rõ lỗi gốc là model chọn sai nhãn).
  - Nhóm lỗi thiếu từ khóa & phủ định cục bộ bước ② (`B18`, `B21`, `B23`, `B24`): bước ②+③ đã nạp đủ điều khoản quyết định (`SP-07`, `SP-23`, `SP-28`, `SP-30`, `SP-35`) và tách đúng vế bằng chứng, nhưng kết quả đầu cuối mới tăng **0/4 → 1/4** (`B18` đạt; `B21`, `B23`, `B24` vẫn trượt ở khâu suy luận của model).
  - Tổng 6 câu trượt lượt 1: **0/6 → 2/6** (`B09`, `B18`) · Tổng cả bộ: **18/24 (75%) → 19/24 (79%)** (`thuong` **7/8 = 88% → 8/8 = 100%**, `kho` **8/13 = 62% → 8/13 = 62%**, `tu_choi` **3/3 = 100% → 3/3 = 100%**).
- **Câu nào tệ đi sau khi sửa:**
  - **`B14` (`1 → 0`, tệ đi hoàn toàn):** Lượt 1 trích đúng `SP-01`/`SP-02` và giải thích đúng Shopee có chính sách chung; lượt 2 (dù bước ②+③ vẫn cấp đúng 10 điều khoản gồm `SP-01`..`SP-03`, `SP-27`) model bị dao động sinh, trả lời sai rằng việc trả hàng khi mở hộp "phụ thuộc vào quy định của từng shop" và **gán sai nội dung cho mã `SP-27`** (thực chất `SP-27` quy định phí ship người bán, không phải shop từ chối khi bóc hộp).
  - **`B24` (`0 → 0`, tệ đi ở nhãn kết luận):** Lượt 1 ra đúng nhãn `Đủ điều kiện`; lượt 2 tụt sang `Không chắc cần CSKH` vì model hiểu nhầm câu hỏi "có bị treo luôn không" thành "bị treo tài khoản", đồng thời trích nhầm mã `SP-28` cho nội dung hỗ trợ Xu của `SP-30`.
  - *Nhược điểm định dạng mới (chưa làm trượt câu):* 5 câu (`B03`, `B17`, `B18`, `B20`, `B23`) bị dính chữ thừa `"(chưa soạn)"` ở cuối đoạn nháp đã soạn.

## 4. Còn lại

- **Lỗi chưa sửa + nguy hiểm thế nào** *(cả 5 câu trượt lượt 2 đều thuộc nhóm `kho`: `B14`, `B15`, `B21`, `B23`, `B24`)*:
  1. **Model bỏ sót cảnh báo rủi ro dù bước ③ đã cấp đúng điều khoản (`B23` — 15 điều khoản trong prompt, có `SP-35`):** không cảnh báo tránh giao dịch qua Zalo ngoài hệ thống Shopee. **Mức độ nguy hiểm: cao nhất** — nếu người mua nghe shop chuyển sang Zalo, Shopee không lưu được bằng chứng (`SP-35`) và người mua có nguy cơ mất trắng tiền hàng.
  2. **Gán sai nội dung cho mã điều khoản có thật (`B14` gán nhầm `SP-27`; `B24` trích nhầm `SP-28` cho `SP-30`):** bước ⑤ hiện chỉ kiểm tra mã có tồn tại trong `SP-01`..`SP-35` nên không phát hiện được việc "trích đúng mã nhưng diễn giải sai điều khoản". **Nguy hiểm:** tạo cảm giác có căn cứ chính thức trong khi lời khuyên sai (tin shop không cho trả hàng đã bóc hộp ở `B14`).
  3. **Chọn nhầm nhãn `Chưa đủ thông tin cần hỏi thêm` thay vì `Không chắc cần CSKH` ở câu hỏi cơ chế chung / tranh chấp đang treo (`B15`, `B21`) và hiểu nhầm tiếng Việt đời thường (`B24`):** ở `B21`, model không cản người mua chuyển sai sang diện Đổi ý (`SP-10`), còn khuyên ngược "yêu cầu shop gửi video test phím" và bịa tên chức năng "Khách hàng khiếu nại" — dễ khiến người mua khai sai lý do và bị từ chối tranh chấp.
  4. **Thiếu mã phụ ở bước ② (`B08` thiếu `SP-33`, `B16` thiếu `SP-04`):** chưa làm sai kết luận nhưng còn lỗ hổng nhận diện từ khóa (`"tiền hoàn"`, `"thiếu mất 1 hộp"`).
- **Nếu có thêm 1 tuần:**
  1. **Thu gọn ngữ cảnh tra cứu (bước ③) & siết `SYSTEM` prompt (bước ④):** tách tag `nguoi_ban` khỏi nhóm phí ship người bán (`SP-26`, `SP-27`) để giảm số điều khoản gây nhiễu từ 10–17 xuống đúng phần liên quan; bổ sung luật bắt buộc trả lời đủ từng câu hỏi phụ (cảnh báo giao dịch ngoài sàn `SP-35`, không chuyển hàng lỗi sang Đổi ý `SP-10`, quy tắc rạch ròi giữa `Không chắc cần CSKH` vs `Chưa đủ thông tin cần hỏi thêm`) và sửa câu mẫu nháp để bỏ lỗi dính chữ `"(chưa soạn)"`.
  2. **Nâng cấp kiểm tra bước ⑤ hoặc định tuyến câu `kho` sang model suy luận tốt hơn:** bổ sung bước đối chiếu xem mã trích dẫn có khớp ý điều khoản trong `data/shopee_policy.md` (chặn lỗi như `B14`/`B24`) và thử nghiệm model lớn hơn riêng cho câu nhiều chủ đề (`len(chu_de) >= 4`) rồi đối chiếu chi phí trong `cost/cost-estimate.md`.
  3. **Bổ sung nguồn dữ liệu chính thức (`data/shopee_policy.md`):** cập nhật Điều Khoản Dịch Vụ Shopee Mall (`SP-03`) và bài thời hạn hoàn tiền (`SP-33`) từ Shopee để xử lý đầy đủ nhóm câu `B08`, `B15`, rồi chạy đánh giá lượt 3 xác nhận vượt chuẩn ≥ 80% và 0 câu tụt hạng.
