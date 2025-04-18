# File Compressor Application

## Giới thiệu
Ứng dụng **File Compressor** cho phép người dùng chọn các tệp tin để nén thành tệp `.zip`. Sau khi nén xong, người dùng có thể mở thư mục chứa tệp nén một cách dễ dàng. Đây là một ứng dụng đơn giản với giao diện người dùng thân thiện, được xây dựng bằng Python và thư viện PySimpleGUI.

## Các tính năng chính
- **Chọn tệp để nén**: Người dùng có thể chọn một hoặc nhiều tệp để nén.
- **Chọn thư mục lưu tệp nén**: Người dùng có thể chọn thư mục đích để lưu tệp `.zip`.
- **Nhập tên tệp nén**: Người dùng nhập tên cho tệp nén (không chứa ký tự đặc biệt).
- **Nén tệp tin**: Sau khi nhập đầy đủ thông tin, người dùng có thể nén tệp tin.
- **Mở thư mục chứa tệp nén**: Sau khi nén thành công, người dùng có thể mở thư mục chứa tệp `.zip` và chọn sẵn tệp đó.

## Cài đặt
Để sử dụng ứng dụng, bạn cần cài đặt Python và một số thư viện cần thiết.

### 1. Cài đặt Python
Ứng dụng yêu cầu Python 3.6 hoặc phiên bản cao hơn. Bạn có thể tải Python tại [python.org](https://www.python.org/downloads/).

### 2. Cài đặt các thư viện cần thiết
Cài đặt các thư viện yêu cầu thông qua `pip`:
- **FreeSimpleGui**: 
    ```bash
    pip install FreeSimpleGui
    ```
### 3. Các thư viện bổ sung
Ứng dụng sử dụng trong ứng dụng: os, platform, re, subprocess, zipfile, pathlib,

## Hướng dẫn sử dụng
### 1. Chọn tệp để nén: Nhấp vào nút "Choose" ở phần "Select files to compress" để chọn các tệp bạn muốn nén.

### 2. Chọn thư mục lưu tệp nén: Nhấp vào nút "Choose" ở phần "Select destination folder" để chọn thư mục đích cho tệp nén.

### 3. Nhập tên tệp nén: Nhập tên cho tệp .zip mà bạn muốn tạo.

### 4. Nén tệp tin: Nhấn nút "Compress" để bắt đầu quá trình nén. Thông báo thành công/ Báo lỗi sẽ được hiển thị bên dưới.

### 5. Mở thư mục chứa tệp nén: Sau khi nén thành công, nhấn nút "Open Folder" để mở thư mục chứa tệp .zip vừa tạo.

## Cấu trúc dự án
    ```css 
    FileCompressor/
    │
    ├── GUI.py              # Tệp Python chính chứa giao diện người dùng
    ├── zip_creator.py      # Tệp Python chứa logic tạo file nén
    ├── function.py          # Tệp Python chứa các chức năng hỗ trợ khác
    └── README.md            # Tệp README này
    ```
## Tính năng bổ sung
### 1. Kiểm tra tên file hợp lệ: Ứng dụng kiểm tra xem tên tệp có hợp lệ hay không (không chứa ký tự đặc biệt).

### 2. Hiển thị thông báo lỗi: Nếu có lỗi trong quá trình nén, ứng dụng sẽ hiển thị thông báo lỗi rõ ràng.


## Cảm ơn bạn đã sử dụng ứng dụng!
Ứng dụng siêu cơ bản, nhằm mục đích ứng dụng và giúp quá trình học của bản thân mình dễ dàng và hiệu quả hơn. 
Nếu bạn có bất kỳ câu hỏi hoặc đề xuất nào, vui lòng liên hệ với tôi qua email hoặc mở vấn đề (issue) trên GitHub.


