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
**Làm:** dán hội thoại văn bản tiếng Việt, một đơn mỗi lần; tạo phiếu nháp và chỉ ra căn cứ; cảnh báo thiếu/mâu thuẫn; sửa, xác nhận, lưu và xem danh sách đơn; đánh giá chất lượng trích xuất và ghi nhận thời gian xử lý, token, chi phí. Bản thử nghiệm chạy cho một cửa hàng với người vận hành tin cậy trên máy demo.

**Không làm:** kết nối Zalo/Facebook, ảnh hoặc giọng nói, tự trò chuyện với khách, tự xác nhận đơn, thanh toán, vận chuyển, quản lý kho, nhiều chi nhánh, triển khai công khai nhiều tài khoản. Yêu cầu dị ứng chỉ được giữ nguyên để người bán kiểm tra, không được AI kết luận về độ an toàn thực phẩm.

## 4. Kế hoạch qua sáu checkpoint
Lịch dự kiến từ tuần 4 đến tuần 12, cách nhau 1–2 tuần. Cường = Trần Gia Cường; Đại = Nguyễn Ngọc Đại; Đạt = Nguyễn Hà Đạt. Cả ba làm việc ở mỗi mốc; chủ trì tổng hợp đầu ra và theo dõi tiến độ, không làm thay tất cả. CP1–CP6 là checkpoint kế hoạch, chưa gán tương ứng với PA#1–PA#5 khi chưa có lịch chi tiết môn học.

| Mốc / ngày dự kiến | Cường | Đại | Đạt | Đầu ra / chủ trì |
|---|---|---|---|---|
| CP1 · T4 · 07/10/2026 | Rà vấn đề, phạm vi | Rà tính năng, chi phí AI | Kiểm tra repo, gói nộp | PA#1 + tự đánh giá + AI-LOG / Cường |
| CP2 · T5 · 14/10/2026 | Phỏng vấn, gán nhãn 20 mẫu | Thử 20 ca khó mô phỏng | Kiểm tra nhãn, phác thảo luồng | Quy trình, 20 mẫu, bản phác thảo / Cường |
| CP3 · T7 · 28/10/2026 | Mở rộng 40 mẫu phát triển | Xây trích xuất, đo lỗi/token | Làm giao diện nháp và căn cứ | Bản thử LLM, báo cáo lỗi/chi phí / Đại |
| CP4 · T9 · 11/11/2026 | Kiểm tra đơn theo hội thoại | Lưu đơn, kiểm tra dữ liệu API | Tích hợp sửa/xác nhận/danh sách | Demo trọn luồng / Đạt |
| CP5 · T11 · 25/11/2026 | Thử với chủ tiệm, đo thời gian | Chạy đánh giá 20 mẫu giữ riêng | Kiểm tra nhãn, sửa lỗi giao diện | 60 mẫu, báo cáo chất lượng / Cường |
| CP6 · T12 · 02/12/2026 | Tổng hợp giới hạn/thay đổi | Sửa lỗi, hướng dẫn cấu hình | Kiểm tra chạy sạch, chuẩn bị demo | Bản bàn giao, hướng dẫn, kết quả / Đạt |

Phụ thuộc chính: dữ liệu mẫu trước thử LLM; luồng xác nhận trước thử người dùng. Dự kiến hoàn thành công việc chính trước mỗi mốc CP2–CP6 ba ngày để sửa lỗi. Nếu độ chính xác chưa đạt ở CP3, giảm xuống đơn một loại bánh và ưu tiên kích thước, số lượng, lịch nhận; vẫn giữ xác nhận thủ công. Nếu yêu cầu chi tiết từng checkpoint thay đổi, nhóm cập nhật công việc trên repository và ghi lại lý do.

## 5. Hai rủi ro có thể khiến dự án thất bại
**R1 — Trích xuất sai nhưng người dùng tin phiếu nháp:** đặc biệt khi khách đổi ý hoặc dùng ngày tương đối; nếu lỗi thường xuyên, sản phẩm không tiết kiệm công kiểm tra. **Bắt đầu tuần này:** Nguyễn Ngọc Đại tạo 20 ca khó có đáp án, thử mô hình và phân loại lỗi; Nguyễn Hà Đạt phác thảo hiển thị căn cứ cạnh từng trường và bước xác nhận bắt buộc. Sau đó mở rộng bộ đánh giá, không dùng điểm “tự tin” của mô hình thay cho đối chiếu căn cứ.

**R2 — Không tiếp cận được người dùng/dữ liệu thực tế:** dữ liệu tự viết quá sạch có thể khiến kết quả thử không phản ánh nhu cầu. **Bắt đầu tuần này:** Trần Gia Cường liên hệ ba cửa hàng để xin một buổi trao đổi và ví dụ đã ẩn thông tin cá nhân, có sự đồng ý. Nếu sau bảy ngày chưa có người tham gia, nhờ một người từng nhận đơn bánh đánh giá 20 tình huống mô phỏng; ghi rõ giới hạn, không trình bày dữ liệu mô phỏng như dữ liệu thật. Không đưa tin nhắn nhận diện khách hàng vào repository.

## 6. Công nghệ và chi phí
- **Next.js + TypeScript:** giao diện và API trong cùng dự án để tích hợp nhanh luồng phiếu nháp; chỉ gọi mô hình ở server để giữ kín API key.
- **SQLite:** lưu đơn đã xác nhận và các lần chỉnh sửa trong bản demo một cửa hàng, không cần vận hành máy chủ cơ sở dữ liệu riêng.
- **Google Gemini Developer API, `gemini-2.5-flash-lite`:** chi phí thấp phù hợp thử lặp trên hội thoại ngắn để trích xuất phiếu đơn; kiểm tra chất lượng tiếng Việt ở CP3. Giá Standard trả phí: 0,10 USD/triệu token đầu vào, 0,40 USD/triệu token đầu ra [1].
- **Zod:** kiểm tra cấu trúc và kiểu dữ liệu mô hình trả về trước khi hiển thị/lưu; không coi cấu trúc hợp lệ là bằng chứng nội dung đúng.
- **Git + GitHub:** quản lý mã, tài liệu và phân công qua issue, giúp truy vết thay đổi kế hoạch; demo chạy cục bộ để chưa cần chi phí hosting.

**Dự toán:** một lượt giả định 2.000 token vào và 500 token ra tốn 0,0004 USD; 5.000 lượt khoảng 2 USD. Dành tối đa 5 USD cho thử nghiệm, kể cả lượt thử lại; theo dõi token thực tế và dừng gọi khi chạm ngân sách ứng dụng. Ước tính chưa gồm thuế, tỷ giá, hosting và không dùng công cụ tìm kiếm trả phí. Chỉ dùng hội thoại mô phỏng khi gọi mô hình trong bản demo.

**Dữ liệu ra ngoài:** bản demo chỉ gửi hội thoại mô phỏng, chỉ dẫn trích xuất và cấu trúc phiếu từ server tới Google Gemini để tạo nháp. Không gửi tên, số điện thoại, địa chỉ thật, dữ liệu khách thật hay bí mật vào prompt; API key chỉ dùng xác thực từ server. Phỏng vấn chỉ cung cấp quy trình để viết tình huống tổng hợp. Cách này đủ thử tính năng mà không chuyển dữ liệu nhận diện khách sang nhà cung cấp; chưa cam kết chính sách lưu giữ của Google. Nhóm khai báo AI hỗ trợ phát triển trong `AI-LOG.md` ở mỗi PA#1–PA#5 và chịu trách nhiệm giải thích sản phẩm.

[1] Google, Gemini Developer API pricing, mục Gemini 2.5 Flash-Lite / Standard, kiểm tra 07/10/2026: https://ai.google.dev/gemini-api/docs/pricing — cần kiểm tra lại trước triển khai.
