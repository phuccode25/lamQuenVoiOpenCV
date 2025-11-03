# 👁️ Nhận diện khuôn mặt với OpenCV và Học máy

# 📘 Giới thiệu
Dự án Face Recognition using OpenCV  được phát triển nhằm tìm hiểu và thực hành các bước cơ bản của xử lý ảnh và học máy.  
Chương trình không sử dụng webcam, mà hoạt động hoàn toàn dựa trên bộ dữ liệu ảnh có sẵn .  
Thuật toán chính được sử dụng là LBPH (Local Binary Patterns Histograms) – một kỹ thuật phổ biến trong nhận diện khuôn mặt với OpenCV.

---

## 🚀 Chức năng chính
- Phát hiện khuôn mặt trong ảnh bằng mô hình Haar Cascade  
- Huấn luyện mô hình nhận diện từ dữ liệu khuôn mặt nhiều người  
- Nhận diện khuôn mặt mới dựa trên mô hình đã huấn luyện (`face_trained.yml`) lấy trên trang github của open cv
- Hiển thị tên người và độ tin cậy của kết quả nhận diện  
- Lưu mô hình học máy để tái sử dụng mà không cần huấn luyện lại  

---

## 🧠 Công nghệ sử dụng
- Python   
- OpenCV (cv2)  
- NumPy
- Haar Cascade Classifier  
- LBPH Face Recognizer

---

## 🗂️ Cấu trúc thư mục
- Mỗi file là một dạng bài tập của open cv.