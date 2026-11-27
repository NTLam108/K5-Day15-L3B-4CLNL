# AI SPEC — [Tên lát cắt] · Nhóm [tên nhóm] · Phòng [XXX] · Zone [X]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: [đề gợi ý trong file track, hoặc bài toán nhóm tự mở rộng] __
Data BTC cấp đã dùng (nếu có — không commit nguyên file): __

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- **Luồng hiện tại trên app Shopee** khi người mua nhận hàng lỗi / hư hỏng / sai mẫu *(viết theo trải nghiệm của nhóm — cần chụp ảnh từ tài khoản thành viên, che mã đơn và địa chỉ, chèn vào đây để xác nhận)*:
  1. Mở Shopee → **Tôi → Đơn mua** → mở đơn vừa nhận.
  2. Bấm **Trả hàng/Hoàn tiền** → chọn sản phẩm và chọn **lý do** trong danh sách có sẵn (hàng lỗi, sai mẫu, thiếu hàng…).
  3. **Tải ảnh / video bằng chứng**, viết mô tả, chọn phương án (hoàn tiền, hoặc trả hàng và hoàn tiền) → gửi yêu cầu.
  4. Người bán phản hồi: đồng ý, hoặc từ chối → người mua có thể khiếu nại để Shopee xem xét.
  5. Nếu được chấp nhận: gửi trả hàng qua đơn vị vận chuyển → nhận hoàn tiền.
  - **Điểm vướng:** người mua chỉ đọc chính sách (hạn trả hàng, có cần video mở hàng không, ảnh thế nào là đủ, chọn lý do nào) **sau khi** đã gặp lỗi, và thường chỉ biết mình thiếu gì khi yêu cầu đã bị từ chối hoặc đã quá hạn.
- **Công cụ đang được dùng cho việc này:**
  - Trang **Chính sách Trả hàng/Hoàn tiền** và **Trung tâm trợ giúp** của Shopee — nguồn: trang công khai của Shopee *(nhóm sẽ ghi link + ngày truy cập vào `data/DATA_CARD.md`)*.
  - **Chat với Shopee / trợ lý ảo trong app** — trả lời có đối chiếu đúng tình huống của từng đơn hay chỉ dẫn link chính sách: **chưa kiểm**.
  - Ngoài Shopee: tìm Google, hỏi bạn bè, hỏi trong group Facebook mua sắm — **chưa kiểm** mức độ phổ biến (sẽ hỏi trong khảo sát).

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- **Người dùng chính:** sinh viên / nhân viên văn phòng 18–30 tuổi, mua hàng trên Shopee vài lần mỗi tháng, **vừa nhận một đơn bị lỗi, hư hỏng hoặc sai mẫu**, chưa từng (hoặc hiếm khi) tự gửi yêu cầu trả hàng, và không có thời gian đọc hết trang chính sách.
- **Việc họ cố làm xong:** *gửi yêu cầu trả hàng / hoàn tiền được chấp nhận cho một đơn Shopee bị lỗi, trong vài ngày sau khi nhận hàng.*
- **Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ:**
  - *Giải bằng:* tự bấm "Trả hàng/Hoàn tiền" và chọn lý do theo cảm tính; ai cẩn thận thì đọc trang chính sách, hỏi chat Shopee hoặc hỏi bạn bè / group Facebook.
  - *Hỏng ở:* chính sách dài, nằm rải nhiều trang, không trả lời thẳng câu "đơn **của tôi** có đủ điều kiện không, tôi còn thiếu gì"; các yêu cầu quan trọng (video mở hàng, hạn bao nhiêu ngày, ảnh phải thấy rõ lỗi) thường chỉ được biết khi đã muộn.
  - *Vì sao chưa bỏ:* trả hàng ngay trong app vẫn là con đường duy nhất để lấy lại tiền; không có lựa chọn nào khác dễ hơn, nên người mua hoặc cố làm cho xong, hoặc bỏ cuộc.
- **Pain:** Người mua Shopee **vừa nhận hàng lỗi** và muốn trả hàng / hoàn tiền, nhưng **không biết mình có đủ điều kiện không và cần chuẩn bị gì** (hạn, video mở hàng, ảnh, lý do chọn) vì chính sách dài và khó hiểu → **yêu cầu bị từ chối hoặc quá hạn**, mất tiền, hoặc bỏ cuộc không đòi nữa.
- **Bằng chứng** (chi tiết: `evidence/summary.md`) — nguồn đạt ngưỡng: **khảo sát n = 22** (21 sinh viên / học viên, 1 nhân viên văn phòng); phỏng vấn và đào bài than phiền đang làm.
  - **Số chính:** **13/22 (59.1%)** từng nhận hàng lỗi / sai mẫu trong 6 tháng qua · **12/22 (54.5%)** không được hoàn tiền đầy đủ, trong đó **7/22 (31.8%)** bỏ qua không trả hàng và **3/22 (13.6%)** gửi nhưng bị từ chối / gặp rắc rối · **12/22 (54.5%)** mất **≥15 phút** để tìm hiểu / xử lý (6 người >30 phút).
  - **Lý do** (câu hỏi nhiều lựa chọn, n = 20): **8/20 (40%)** không biết mình đủ điều kiện không / ngại đọc chính sách dài · **8/20 (40%)** giá trị nhỏ nên ngại làm · **7/20 (35%)** thiếu video khui hàng / ảnh chuẩn · **7/20 (35%)** quy trình rườm rà · **4/20 (20%)** quá hạn.
  - **Trích dẫn:** *"Chính sách hoàn trả khá dài và rắc rối, không rõ trường hợp của mình có được duyệt không nên mất nhiều thời gian tìm hiểu, nhắn tin qua lại với shop và CSKH."* — phiếu khảo sát, Q7
  - **Kết luận (tạm, chờ phỏng vấn):** giả thuyết **đúng một phần** — pain "không biết đủ điều kiện không, cần chuẩn bị gì" là lý do hàng đầu (40%) và thiếu bằng chứng / quá hạn chiếm thêm 35% / 20%; nhưng **"giá trị nhỏ nên ngại làm" cũng 40%**, là cách giải thích khác mà lát cắt này không giải quyết được.
  - **Điều lệch đáng chú ý:** người dùng tin Shopee "bắt buộc phải có video quay liền mạch quá trình mở hộp" (trích dẫn #1 trong `evidence/summary.md`), trong khi chính sách hiện hành chỉ yêu cầu "video và/hoặc ảnh" khi nhận hàng và khi đóng gói (`data/shopee_policy.md` SP-25) → người dùng hiểu sai chính sách, đúng chỗ lát cắt cần trả lời.

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

- **Impact / tháng** của hướng chọn = __ người × __ lần × __ phút = __ — nguồn từng thừa số: __ (không có nguồn thì ghi rõ *(tự ước tính)*)
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8):

## §3. Giải pháp tương tự *(guide 2.1)*
- [sản phẩm / tính năng gần giống]: một điều đáng học · một điều đáng né · mình khác gì

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả):
- Không làm (≥3 điều):
- **Sơ đồ** (Mermaid) — workflow cố định 6 bước, 1 lời gọi model ở quyết định trung tâm (bước 4):

  ```mermaid
  flowchart TD
      U["Người mua Shopee<br/>mô tả lỗi · ngày nhận hàng · có/không video mở hàng"] --> G

      G{"① Chặn phạm vi (code)<br/>sàn khác? tranh chấp pháp lý?<br/>câu lệnh lạ / tấn công?"}
      G -- "ngoài phạm vi" --> R["Từ chối + chỉ sang CSKH Shopee"]
      G -- "trong phạm vi" --> X

      X["② Tách thông tin (code)<br/>loại vấn đề · số ngày từ lúc nhận · có video/ảnh"]
      X -- "thiếu thông tin" --> Q["Hỏi lại đúng phần còn thiếu"]
      X -- "đủ" --> T

      T["③ Công cụ tra_dieu_khoan<br/>tìm điều khoản theo loại vấn đề"] --> D
      DB[("data/shopee_policy.md<br/>điều khoản đã đánh mã SP-01…")] -.-> T

      D["④ MODEL quyết định<br/>đủ / chưa đủ điều kiện + mã điều khoản<br/>+ việc còn thiếu + nháp yêu cầu trả hàng"] --> V

      V{"⑤ Kiểm căn cứ (code)<br/>mã điều khoản có trong data?<br/>kết luận có kèm mã?"}
      V -- "không có căn cứ" --> K["Nói 'không chắc' + chỉ sang CSKH Shopee"]
      V -- "hợp lệ" --> O

      O["⑥ Kết quả cho người mua<br/>kết luận + trích điều khoản<br/>+ danh sách việc còn thiếu + đoạn yêu cầu soạn sẵn"]
      O --> H(["Người mua tự đọc, tự sửa, tự bấm gửi trên Shopee<br/>(hệ thống không gửi thay)"])

      L[["tracing.py: ghi mọi lần gọi model / công cụ + token"]] -.- T
      L -.- D
  ```

  | Bước | Ai làm | Chặn rủi ro gì |
  |---|---|---|
  | ① Chặn phạm vi | code (luật cố định) | câu tấn công, câu hỏi sàn khác / pháp lý không lọt tới model |
  | ② Tách thông tin | code | thiếu ngày nhận / tình trạng video → hỏi lại, không đoán |
  | ③ `tra_dieu_khoan` | công cụ, chỉ đọc, không tác động ra ngoài | model chỉ được dựa trên điều khoản trả về |
  | ④ Quyết định | model (lời gọi duy nhất) | — |
  | ⑤ Kiểm căn cứ | code | kết luận không có mã điều khoản hợp lệ → hạ về "không chắc" (G10) |
  | ⑥ Kết quả | người mua duyệt | quyết định cuối và nút gửi luôn do người mua bấm |
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  |  |  |  |  |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — __ câu (thuong __ · kho __ · tu_choi __) · metric: `eval/metric_spec.yaml` (__ metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ __% câu qua, và __"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
