# AI-LOG — BakeOrder / CSC13114

## 2026-10-07 — Đề xuất và kế hoạch PA#1
Tool: Codex (trợ lý AI trong phiên làm việc này).
Asked for: chọn một ý tưởng phù hợp rubric, soạn đề xuất, kế hoạch, tự đánh giá và chuẩn bị repository/gói nộp.
Kept: ý tưởng BakeOrder, phần lớn nội dung đề xuất, ví dụ lỗi LLM, công nghệ và dự toán token do AI soạn; chưa có mã sản phẩm hay kết quả thử nghiệm.
Changed: người dùng cung cấp tên/MSSV và repository, yêu cầu chỉ dùng Markdown, sửa lịch từ sáu tuần liên tiếp sang tuần 4–12 bắt đầu 07/10; AI thực hiện các chỉnh sửa vào file.
Rejected: bỏ bản PDF/HTML khỏi gói nộp theo yêu cầu người dùng; bỏ lịch thứ Năm ban đầu vì người dùng sửa mốc nộp; người dùng phản biện bảng chỉ nêu một chủ trì vì chưa thấy công việc của hai người còn lại.
By hand: người dùng trực tiếp cung cấp thông tin nhóm, lịch, yêu cầu môn học và các phản biện trong hội thoại; chưa có bằng chứng nhóm tự viết nội dung file hay code. Không gán các chỉnh sửa do AI thực hiện thành phần viết tay.

Ghi chú: mục trên được bổ sung khi nhận quy định AI-LOG, dựa trên hội thoại đang có; không phải nhật ký đã ghi liên tục từ đầu. Các mục sau được ghi khi làm việc. Không tự ước lượng tỷ lệ sử dụng AI khi chưa đo.

## 2026-10-07 — Rà soát chính sách AI-first và tạo skill cho môn học
Tool: Codex; công cụ đọc file, truy cập web và Git.
Asked for: đọc tài liệu môn học, xây skill dùng xuyên môn, bổ sung khai báo AI và làm rõ phân công nhóm.
Kept: skill CSC13114 bám rubric và chính sách người dùng dán; yêu cầu khai báo dữ liệu gửi đến nhà cung cấp LLM; công việc riêng cho ba thành viên tại mỗi checkpoint.
Changed: áp dụng chính sách AI-first xuyên các bài, phân biệt sáu checkpoint với PA#1–PA#5; ghi rõ hai liên kết Claude chưa đọc được, không suy diễn nội dung đặc tả. AI sửa lại tự đánh giá từ 100 xuống 96 vì nguồn lịch và giả định chưa xác thực; không phải vì dùng nhiều AI.
Rejected: cách xem việc dùng nhiều AI là vi phạm; tuyên bố đã đọc toàn bộ tài liệu khi công cụ không truy cập được nguồn.
By hand: người dùng cung cấp đoạn chính sách AI và giải thích bối cảnh môn học; skill và thay đổi tài liệu được AI viết, chưa có kiểm chứng khả năng giải thích của từng thành viên.

## 2026-10-07 — Thử đọc trực tiếp hai trang tài liệu Claude
Tool: Codex, HTTP client và Chrome headless với hồ sơ trình duyệt riêng, không đăng nhập.
Asked for: mở hai trang Claude để đọc nội dung môn học thay vì coi chúng là file đính kèm.
Kept: kết quả kiểm tra truy cập: tải được HTML khung; yêu cầu dữ liệu trực tiếp gặp Cloudflare; sau khi chạy JavaScript, cả hai trang hiển thị “Page not found”.
Changed: làm rõ rằng chưa lấy được nội dung bài học bên trong, không phải hai URL là file tải xuống.
Rejected: suy đoán nội dung spec từ HTML khung hoặc kết luận tài liệu đã bị xóa chỉ vì trình duyệt không đăng nhập không đọc được.
By hand: người dùng giải thích đây là hai website và yêu cầu đọc trực tiếp; việc kiểm tra được AI thực hiện. Chưa có nội dung nguồn mới để bổ sung vào skill.

## 2026-10-07 — Đọc hai bản xuất slide và sửa theo yêu cầu học kỳ
Tool: Codex, trình đọc file, Python, Git/GitHub Actions.
Asked for: đọc hai file Markdown vừa tải và hoàn thiện skill dùng xuyên môn cùng các tài liệu liên quan.
Kept: yêu cầu database, authentication, deployability; quy trình Plan–Implement–Validate–Human Gate; template spec tám phần và hướng dẫn IA#1 từ AWAD02.
Changed: bổ sung đăng nhập, database triển khai được, Docker/cloud, spec trước code và kế hoạch harness/eval/red-team/vấn đáp vào PA#1; thêm CI kiểm tra tài liệu ở giai đoạn hiện tại; cập nhật skill từ hai nguồn đã đọc.
Rejected: phạm vi chỉ demo cục bộ không có đăng nhập; câu cũ ở AWAD01 yêu cầu spec ở checkpoint 1 vì AWAD02 và rubric PA#1 mới hơn ghi rõ không cần spec; không đánh đồng IA#1 với tính năng BakeOrder.
By hand: người dùng tải và cung cấp hai bản xuất slide. AI đọc, đối chiếu và chỉnh các file; chưa có bằng chứng nhóm đã tự phỏng vấn, viết code sản phẩm hoặc chạy thử với người dùng. Hai file nguồn được giữ nguyên tại máy, không đưa vào gói nộp.
