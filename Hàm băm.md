# Hàm băm
## Khái niệm
- Hàm băm (hash function) là các thuật toán không sử dụng khóa để mã hóa, nó có nhiệm vụ băm thông điệp được đưa vào theo một thuật toán h một chiều nào đó, rồi đưa ra một bản băm – văn bản đại diện – có kích thước cố định. Do đó người nhận không biết được nội dung hay độ dài ban đầu của thông điệp đã được băm bằng hàm băm.
- Giá trị của hàm băm là duy nhất, và không thể suy ngược lại được nội dung thông điệp từ giá trị băm này.
## Đặc trưng
- Hàm băm h là hàm một chiều (one ưay hash) vơi các đặc tính
  - Với thông điệp đầu vào x thu được bản băm z=h(x) là duy nhất
  - Nếu dữ liệu trong thông điệp x thay đổi để thành thông điệp x’ thì h(x’)  h(x) => Hai thông điệp hoàn toàn khác nhau thì giá trị hàm băm cũng khác nhau.
