# AI-LOG — BakeOrder / PA#1

## 2026-10-07 — Soạn đề xuất và kế hoạch
Tool: Codex.
Asked for: chọn ý tưởng theo rubric, soạn đề xuất, phân công, tự đánh giá và chuẩn bị repository/gói nộp.
Kept: ý tưởng BakeOrder và phần lớn bản thảo do AI soạn; ví dụ sai đơn, tính năng LLM, công nghệ và dự toán token.
Changed: người dùng cung cấp tên/MSSV, repo và lịch tuần 4–12 bắt đầu 07/10; yêu cầu chỉ dùng Markdown và phân công cả ba người ở mỗi mốc; AI sửa các file theo phản hồi.
Rejected: PDF/HTML trong gói nộp; lịch thứ Năm ban đầu; bảng chỉ nêu chủ trì nhưng không rõ việc của các thành viên khác.
By hand: người dùng cung cấp thông tin nhóm và phản biện các lựa chọn. Chưa có nội dung file hoặc code sản phẩm được xác nhận là nhóm tự viết tay; chỉnh sửa file do AI thực hiện.

Ghi chú: mục trên được bổ sung từ hội thoại khi nhận quy định AI-LOG, không phải nhật ký ghi liên tục từ đầu. Các giả định, mục tiêu và việc dự kiến chưa được trình bày như kết quả đã đạt.

## 2026-10-07 — Đối chiếu yêu cầu và kiểm tra bản nộp
Tool: Codex, Python, Chrome headless, GitHub Actions.
Asked for: đối chiếu PA#1 với rubric và hai bản xuất slide người dùng cung cấp, rồi kiểm tra tài liệu.
Kept: PA#1 không có spec; kế hoạch học kỳ cần database, đăng nhập, triển khai và một tính năng LLM có eval/giới hạn/xác nhận; repository có rules file và CI.
Changed: bổ sung yêu cầu còn thiếu vào phạm vi/kế hoạch, mô tả dữ liệu gửi tới Gemini; giảm tự đánh giá 100 xuống 96 vì còn giả định và lịch chưa xác thực; kiểm tra bố cục đề xuất hai trang A4 tham chiếu.
Rejected: phạm vi chỉ demo cục bộ không có đăng nhập; yêu cầu spec ở PA#1 từ slide cũ vì hướng dẫn mới hơn phủ định; tuyên bố CI tài liệu là quality gate hoàn chỉnh của sản phẩm.
By hand: người dùng tải và cung cấp slide. AI thực hiện chỉnh sửa, kiểm tra cục bộ và xác minh CI thành công; nhóm chưa phỏng vấn, triển khai sản phẩm hoặc đánh giá mô hình. Ba lỗi kiểm tra trong bản sao tạm không phải bằng chứng chặn merge thực tế.

## 2026-10-07 — Thu gọn repository đúng phạm vi PA#1
Tool: Codex và Git.
Asked for: gỡ các nội dung không phục vụ yêu cầu PA#1 khỏi repository dự án.
Kept: đề xuất, tự đánh giá, nhật ký AI, README và rules/CI ban đầu theo slide.
Changed: gỡ tài nguyên dùng chung cho môn và các liên kết tới chúng; thu gọn nhật ký thành tài khoản công việc liên quan PA#1, bảo toàn bản chi tiết ở máy cục bộ và lịch sử Git.
Rejected: đưa mọi tài nguyên hỗ trợ AI vào repository chỉ vì trước đó người dùng đã cho phép push tài liệu dự án.
By hand: người dùng phát hiện việc mở rộng phạm vi và yêu cầu gỡ; AI thực hiện việc dọn repository và đóng lại ZIP.

## 2026-10-07 — Chỉ giữ tài liệu nộp PA#1
Tool: Codex và Git.
Asked for: chỉ giữ yêu cầu nộp PA#1, không áp dụng thêm phần chuẩn bị repository từ các slide tuần đầu.
Kept: PROPOSAL.md, SELF_ASSESSMENT_REPORT.md, AI-LOG.md và README.md.
Changed: gỡ rules file, workflow CI, script kiểm tra và file cấu hình khỏi nhánh hiện tại; chuyển CI trong kế hoạch sang CP2, bỏ các tham chiếu tới công cụ đã gỡ.
Rejected: giữ rules/CI chỉ vì slide môn học nói tới chúng dù người dùng đã giới hạn phạm vi repository ở PA#1.
By hand: người dùng xác định lại phạm vi; AI thực hiện thay đổi. Các mục trước ghi lịch sử công việc lúc đó, không mô tả danh sách file hiện còn trong repo.
