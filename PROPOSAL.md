# PA#1 — Đề xuất và kế hoạch dự án BakeOrder
CSC13114 · Nhóm tối đa 3 thành viên · Nhóm 23120225–23120226–23120229

**Thành viên:** Trần Gia Cường — 23120225; Nguyễn Ngọc Đại — 23120226; Nguyễn Hà Đạt — 23120229.
**Repository:** https://github.com/datkrb/BakeOrder

## 1. Vấn đề và người dùng
BakeOrder là ứng dụng web hỗ trợ cửa hàng bánh nhỏ chuyển hội thoại đặt bánh tiếng Việt thành phiếu đơn để kiểm tra. Người dùng đại diện là **chị Mai, chủ một tiệm bánh sinh nhật nhận đặt trước**, vừa tư vấn khách vừa tổng hợp đơn cuối ngày. Đây là persona giả định cần xác thực, không phải người đã được phỏng vấn. Hiện tại, chị đọc lại tin nhắn rồi chép yêu cầu vào sổ hoặc bảng tính.

**Vấn đề:** Khi khách sửa yêu cầu qua nhiều tin nhắn, chị Mai dễ chép nhầm phiên bản cuối của đơn, dẫn đến làm sai bánh hoặc giao sai giờ. Dự án tập trung vào bước tổng hợp và kiểm tra đơn trước khi sản xuất, không thay thế toàn bộ hoạt động của cửa hàng.

## 2. Tính năng LLM và chi phí khi sai
**Một tính năng cốt lõi:** từ một hội thoại của một đơn, LLM tạo phiếu nháp gồm loại bánh, kích thước, số lượng, chữ trên bánh, ngày/giờ nhận và hình thức nhận. Mỗi thông tin đi kèm câu tin nhắn làm căn cứ; yêu cầu thiếu hoặc mâu thuẫn được đánh dấu để người dùng kiểm tra. Không đủ căn cứ thì để trống và hỏi lại, không tự đoán.

Ví dụ: khách nhắn “bánh 16 cm, lấy 18h ngày 20/11”, sau đó “đổi 20 cm nhé”. Phiếu phải ghi 20 cm và giữ lịch nhận cũ; nếu khách chỉ nhắn “đổi sang thứ Bảy” mà thiếu ngữ cảnh ngày, hệ thống yêu cầu xác nhận ngày cụ thể. Chủ cửa hàng xem hội thoại cạnh phiếu, sửa và xác nhận rồi mới lưu thành đơn chính thức.

**Ai chịu thiệt và bao nhiêu:** giả định đơn bán 350.000 đồng, chi phí làm bánh 180.000 đồng. Sai kích thước sau sản xuất có thể tốn thêm 180.000 đồng làm lại. Nếu hủy và hoàn 350.000 đồng, cửa hàng mất doanh thu dự kiến và chịu 180.000 đồng chi phí bánh bỏ đi; tiền hoàn không phải khoản lỗ cộng thêm vào doanh thu đã mất. Khách mất thời gian hoặc lỡ tiệc; sửa sau giờ tiệc không bù lại được sự kiện. Trước sản xuất, thường sửa được phiếu; sau giao hàng, sửa dữ liệu không hoàn tác thiệt hại. Đây là giả định cần xác thực ở CP2.

**Làm sao biết sai:** dự kiến đánh giá bằng 60 hội thoại có đáp án do Cường gán nhãn và Đạt kiểm tra, bất đồng được đối chiếu lại với hội thoại, gồm đổi yêu cầu, thiếu thông tin, mâu thuẫn và cách viết tắt. Dùng 40 hội thoại phát triển, giữ riêng 20 hội thoại đánh giá cuối. Trường quan trọng gồm loại bánh, kích thước, số lượng và lịch nhận; sai một trường là một đơn có nguy cơ gây thiệt hại. Theo dõi độ đúng từng trường, số đơn sai và số trường người dùng sửa; so sánh thời gian chép tay với kiểm tra phiếu trên cùng tình huống. Mục tiêu ban đầu: đúng ít nhất 95% trường quan trọng đã có thông tin và không tự điền các trường cố ý thiếu trong bộ đánh giá; đây là mục tiêu, chưa phải kết quả đạt được.

## 3. Phạm vi học kỳ
**Làm:** web React cho một cửa hàng, có đăng nhập chủ tiệm và database; dán hội thoại tiếng Việt, tạo nháp có căn cứ/cảnh báo, sửa và xác nhận trước khi chuyển sang đơn dùng để sản xuất; lưu/xem danh sách đơn. Đo lỗi LLM, thời gian và chi phí; có rules file, CI, Docker và bản triển khai thử nghiệm dùng dữ liệu mô phỏng. Người chưa đăng nhập không được xem/sửa đơn; quyền và giới hạn được kiểm tra ở server.

**Không làm:** tích hợp Zalo/Facebook, ảnh/giọng nói, tự trò chuyện hoặc tự xác nhận đơn, thanh toán, vận chuyển, kho, nhiều chi nhánh, đăng ký tài khoản công khai. Không cho AI kết luận về an toàn thực phẩm. Bản cloud giới hạn tài khoản demo, không xử lý đơn khách thật.

## 4. Kế hoạch qua sáu checkpoint
Lịch dự kiến từ tuần 4 đến tuần 12, cách nhau 1–2 tuần. Cường = Trần Gia Cường; Đại = Nguyễn Ngọc Đại; Đạt = Nguyễn Hà Đạt. Cả ba làm việc ở mỗi mốc; chủ trì tổng hợp đầu ra và theo dõi tiến độ, không làm thay tất cả. CP1–CP6 là checkpoint kế hoạch, chưa gán tương ứng với PA#1–PA#5 khi chưa có lịch chi tiết môn học.

| Mốc / ngày dự kiến | Cường | Đại | Đạt | Đầu ra / chủ trì |
|---|---|---|---|---|
| CP1 · T4 · 07/10/2026 | Rà vấn đề, phạm vi | Rà LLM, chi phí | Rà repo, tài liệu và gói nộp | PA#1 + tự đánh giá + AI-LOG / Cường |
| CP2 · T5 · 14/10/2026 | Phỏng vấn, 20 mẫu; spec lõi trước code | Contract/quyền; thử mô hình riêng | Rà spec, giao diện; CI kiểm tra AC | Spec lõi, 20 mẫu, harness ban đầu / Cường |
| CP3 · T7 · 28/10/2026 | 40 mẫu phát triển, phân loại lỗi | Trích xuất, đăng nhập/API, đo token | Giao diện nháp/căn cứ, kiểm tra quyền | Prototype LLM có giới hạn / Đại |
| CP4 · T9 · 11/11/2026 | Kiểm tra lỗi nghiệp vụ, vị trí xác nhận | Database, lưu đơn; REST/GraphQL | Tích hợp trọn luồng, Docker/cloud demo | Bản tích hợp có đăng nhập / Đạt |
| CP5 · T11 · 25/11/2026 | Thử người dùng; phối hợp red-team được giao | Eval 20 mẫu giữ riêng; sửa guardrails | Rà nhãn, latency; kiểm chứng quality gate | 60 mẫu, eval và báo cáo red-team / Cường |
| CP6 · T12 · 02/12/2026 | Báo cáo, giới hạn; ôn quyết định nghiệp vụ | Cấu hình/chạy lại; ôn API/LLM | Kiểm tra deploy; ôn UI/tích hợp | Final build; cả ba tập vấn đáp / Đạt |

Phụ thuộc chính: dữ liệu mẫu trước thử LLM; luồng xác nhận trước thử người dùng. Dự kiến hoàn thành công việc chính trước mỗi mốc CP2–CP6 ba ngày để sửa lỗi. Nếu độ chính xác chưa đạt ở CP3, giảm xuống đơn một loại bánh và ưu tiên kích thước, số lượng, lịch nhận; vẫn giữ xác nhận thủ công. Nếu yêu cầu chi tiết từng checkpoint thay đổi, nhóm cập nhật công việc trên repository và ghi lại lý do.

## 5. Hai rủi ro có thể khiến dự án thất bại
**R1 — Trích xuất sai nhưng người dùng tin phiếu nháp:** đặc biệt khi khách đổi ý hoặc dùng ngày tương đối; nếu lỗi thường xuyên, sản phẩm không tiết kiệm công kiểm tra. **Bắt đầu tuần này:** Nguyễn Ngọc Đại tạo 20 ca khó có đáp án, thử mô hình và phân loại lỗi; Nguyễn Hà Đạt phác thảo hiển thị căn cứ cạnh từng trường và bước xác nhận bắt buộc. Sau đó mở rộng bộ đánh giá, không dùng điểm “tự tin” của mô hình thay cho đối chiếu căn cứ.

**R2 — Không tiếp cận được người dùng/dữ liệu thực tế:** dữ liệu tự viết quá sạch có thể khiến kết quả thử không phản ánh nhu cầu. **Bắt đầu tuần này:** Trần Gia Cường liên hệ ba cửa hàng để xin một buổi trao đổi và ví dụ đã ẩn thông tin cá nhân, có sự đồng ý. Nếu sau bảy ngày chưa có người tham gia, nhờ một người từng nhận đơn bánh đánh giá 20 tình huống mô phỏng; ghi rõ giới hạn, không trình bày dữ liệu mô phỏng như dữ liệu thật. Không đưa tin nhắn nhận diện khách hàng vào repository.

## 6. Công nghệ và chi phí
- **Next.js + TypeScript:** React và API chung dự án; REST cho thao tác đơn, GraphQL đọc danh sách; kiểu dữ liệu hỗ trợ luồng nháp → xác nhận.
- **PostgreSQL:** lưu đơn, tài khoản và lịch sử sửa; transaction bảo đảm đơn và lịch sử được lưu cùng nhau khi triển khai.
- **Auth.js:** tích hợp đăng nhập/session với Next.js; kiểm tra quyền ở server để chặn truy cập đơn trái phép, không chỉ ẩn nút ở giao diện.
- **Google Gemini Developer API, `gemini-2.5-flash-lite`:** chi phí thấp phù hợp thử lặp trên hội thoại ngắn để trích xuất phiếu đơn; kiểm tra chất lượng tiếng Việt ở CP3. Giá Standard trả phí: 0,10 USD/triệu token đầu vào, 0,40 USD/triệu token đầu ra [1].
- **Zod:** kiểm tra cấu trúc và kiểu dữ liệu mô hình trả về trước khi hiển thị/lưu; không coi cấu trúc hợp lệ là bằng chứng nội dung đúng.
- **GitHub Actions (dự kiến CP2):** kiểm tra lint/types/test theo AC khi có code; lưu bằng chứng lần gate phát hiện lỗi thật.
- **Docker:** đóng gói web và database để chạy lại được trên máy nhóm/cloud; log lỗi, token và latency phục vụ quan sát demo.

**Dự toán:** 2.000 token vào + 500 token ra/lượt ≈ 0,0004 USD; 5.000 lượt ≈ 2 USD. Ngân sách mô hình 5 USD gồm thử lại; ứng dụng giới hạn token/lượt, số lượt và dừng ở ngân sách. Hosting/database cloud chưa chốt nhà cung cấp; dự trù tối đa 10 USD/tháng (ngân sách, không phải báo giá), ưu tiên tài nguyên môn học; chốt ở CP2 trước triển khai CP4. Chưa gồm thuế/tỷ giá.

**Dữ liệu ra ngoài:** bản demo chỉ gửi hội thoại mô phỏng, chỉ dẫn trích xuất và cấu trúc phiếu từ server tới Google Gemini để tạo nháp. Không gửi tên, số điện thoại, địa chỉ thật, dữ liệu khách thật hay bí mật vào prompt; API key chỉ dùng xác thực từ server. Phỏng vấn chỉ cung cấp quy trình để viết tình huống tổng hợp. Cách này đủ thử tính năng mà không chuyển dữ liệu nhận diện khách sang nhà cung cấp; chưa cam kết chính sách lưu giữ của Google. Nhóm khai báo AI hỗ trợ phát triển trong `AI-LOG.md` ở mỗi PA#1–PA#5 và chịu trách nhiệm giải thích sản phẩm.

[1] Google, Gemini Developer API pricing, mục Gemini 2.5 Flash-Lite / Standard, kiểm tra 07/10/2026: https://ai.google.dev/gemini-api/docs/pricing — cần kiểm tra lại trước triển khai.
