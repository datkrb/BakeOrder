# BakeOrder

Đề xuất dự án CSC13114: ứng dụng hỗ trợ chủ cửa hàng bánh chuyển hội thoại đặt hàng tiếng Việt thành phiếu đơn nháp có căn cứ, cảnh báo thiếu/mâu thuẫn để người dùng kiểm tra trước khi xác nhận.

## Thành viên
| Họ tên | MSSV | Trách nhiệm chính |
|---|---|---|
| Trần Gia Cường | 23120225 | Nhu cầu, dữ liệu và đánh giá |
| Nguyễn Ngọc Đại | 23120226 | LLM và backend |
| Nguyễn Hà Đạt | 23120229 | Giao diện và tích hợp |

## Tài liệu PA#1
- [Đề xuất và kế hoạch — PDF 2 trang](PROPOSAL.pdf)
- [Bản nguồn Markdown](PROPOSAL.md)
- [Báo cáo tự đánh giá — 92/100](SELF_ASSESSMENT_REPORT.md)

Repository: https://github.com/datkrb/BakeOrder

## Trạng thái và phạm vi
PA#1 — Proposal and planning. Chưa triển khai sản phẩm; chỉ số đánh giá và chi phí sử dụng là mục tiêu/ước tính. Đặc tả sẽ thực hiện ở giai đoạn môn học yêu cầu.

Phạm vi dự kiến: dán hội thoại, trích xuất một đơn, hiển thị căn cứ, sửa/xác nhận và lưu đơn. Không kết nối mạng xã hội, tự trả lời khách, thanh toán hoặc quản lý kho.

## Lịch checkpoint
| Mốc | Ngày (thứ Năm) | Chủ trì |
|---|---|---|
| CP1 | 15/10/2026 | Trần Gia Cường |
| CP2 | 22/10/2026 | Trần Gia Cường |
| CP3 | 29/10/2026 | Nguyễn Ngọc Đại |
| CP4 | 05/11/2026 | Nguyễn Hà Đạt |
| CP5 | 12/11/2026 | Trần Gia Cường |
| CP6 | 19/11/2026 | Nguyễn Hà Đạt |

Chi tiết đầu ra và phụ thuộc ở mục 4 của đề xuất. Lịch dựa trên thông tin nhóm; cập nhật nếu môn học điều chỉnh.

## Xuất tài liệu
Chạy `node build.cjs`, mở `PROPOSAL.html` và in PDF khổ A4, tỉ lệ 100%, tắt header/footer trình duyệt. Kiểm tra tối đa 2 trang. Không cần cài thư viện Node bổ sung.
