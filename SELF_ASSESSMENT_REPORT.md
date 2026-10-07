# SELF_ASSESSMENT_REPORT — PA#1 / BakeOrder

Thành viên: Trần Gia Cường — 23120225; Nguyễn Ngọc Đại — 23120226; Nguyễn Hà Đạt — 23120229.

Repository: https://github.com/datkrb/BakeOrder

Nhóm tự đánh giá bản đề xuất và kế hoạch PA#1 theo bằng chứng hiện có; chưa mặc định đầy đủ điều kiện nhận điểm tuyệt đối. Đây không phải điểm bảo đảm của giảng viên. Bằng chứng là nội dung đề xuất, không phải tính năng đã triển khai. Việc AI hỗ trợ được khai báo trong [AI-LOG.md](AI-LOG.md).

| # | Tiêu chí | Tối đa | Điểm tự đánh giá | Bằng chứng và giới hạn |
|---|---|---:|---:|---|
| 1 | Vấn đề và người dùng | 20 | 19 | PROPOSAL.md §1: persona chị Mai, tình huống tổng hợp đơn, cách làm hiện tại và câu vấn đề. Persona được ghi rõ là giả định; phỏng vấn là công việc dự kiến. |
| 2 | Tính năng LLM và hậu quả khi sai | 25 | 24 | PROPOSAL.md §2: một tính năng trích xuất, ví dụ đổi yêu cầu, người chịu thiệt, chi phí giả định, khả năng khắc phục và cách phát hiện lỗi. Số tiền là giả định có ghi rõ; đo lỗi và thời gian kiểm tra là kế hoạch, không khẳng định đã thử nghiệm. |
| 3 | Phạm vi | 15 | 15 | PROPOSAL.md §3: làm/không làm rõ ràng, có database, đăng nhập, Docker/deploy, một LLM feature và xác nhận ở bước chốt đơn; phù hợp yêu cầu học kỳ trong AWAD01. |
| 4 | Kế hoạch và trách nhiệm | 20 | 18 | PROPOSAL.md §4: sáu checkpoint dự kiến từ 07/10 đến 02/12/2026 (tuần 4–12), có công việc riêng cho cả ba thành viên, đầu ra, chủ trì và ngày; có phụ thuộc và dự phòng. Chưa đối chiếu lịch chính thức hoặc ánh xạ CP1–CP6 với PA#1–PA#5. |
| 5 | Rủi ro | 10 | 10 | PROPOSAL.md §5: hai rủi ro về độ đúng và dữ liệu/người dùng, hành động có thể bắt đầu tuần này và phương án dự phòng. |
| 6 | Công nghệ | 10 | 10 | PROPOSAL.md §6: lý do từng lựa chọn, nhà cung cấp/mô hình, nguồn giá và dự toán theo token. Chưa đo chi phí thực tế. |
| | **Tổng** | **100** | **96** | 19 + 24 + 15 + 18 + 10 + 10 = 96. |

## Những gì chưa làm được
- Chưa có mô tả chi tiết chính thức của từng checkpoint; nội dung công việc được phân bổ theo lịch dự kiến tuần 4–12, lấy ngày nộp PA#1 07/10/2026 do nhóm cung cấp làm mốc.
- Chưa phỏng vấn chủ cửa hàng, thu dữ liệu thực tế hoặc xác thực giả định thiệt hại.
- Chưa triển khai sản phẩm hay đánh giá mô hình; các chỉ số là mục tiêu. Đặc tả không thuộc phạm vi PA#1 nên chưa viết.
- Chưa có mẫu báo cáo trên Classroom; bảng này bám sáu tiêu chí được cung cấp và cần đối chiếu nếu mẫu có trường bổ sung.
- Đã đọc bản Markdown xuất từ AWAD01 và AWAD02; chưa có syllabus cập nhật, lịch milestone và rubric các bài sau trên Classroom. Đã kiểm tra đề xuất là 2 trang A4 theo bố cục tham chiếu ghi trong README; chưa có quy định trình bày cụ thể của giảng viên.

## Tên gói nộp
`23120225-23120226-23120229_96.zip` — MSSV tăng dần, tổng điểm trong tên trùng bảng tự đánh giá. Điểm này phản ánh phần chưa xác thực, không phải khấu trừ vì dùng AI hoặc chưa triển khai ở giai đoạn đề xuất.
