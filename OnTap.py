#Bai1 file on tap
import itertools

# 1. Tìm tất cả hoán vị của ba số
a, b, c = 1, 2, 3
perms = list(itertools.permutations([a, b, c]))
print("Các hoán vị:", perms)

# 2. Đếm số phần tử bằng nhau liên tiếp nhiều nhất
lst = [1, 2, 2, 2, 3, 3, 1]
max_count = count = 1
for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print("Số lượng phần tử giống nhau liên tiếp nhiều nhất:", max_count)

# 3. Kiểm tra tính tăng/giảm của danh sách
def check_order(lst):
    if all(lst[i] <= lst[i+1] for i in range(len(lst)-1)):
        return "Tăng"
    elif all(lst[i] < lst[i+1] for i in range(len(lst)-1)):
        return "Tăng tuyệt đối"
    elif all(lst[i] >= lst[i+1] for i in range(len(lst)-1)):
        return "Giảm"
    elif all(lst[i] > lst[i+1] for i in range(len(lst)-1)):
        return "Giảm tuyệt đối"
    else:
        return "Không được sắp xếp"

print("Kiểu sắp xếp:", check_order(lst))

#bai 2file on tap
import string
from collections import Counter

text = input("Nhập chuỗi: ")
text = text.lower()  # Không phân biệt hoa thường
for punct in string.punctuation:
    text = text.replace(punct, "")  # Loại bỏ dấu câu

words = text.split()
word_counts = Counter(words)
sorted_words = sorted(word_counts.items(), key=lambda x: -x[1])

print("Tần suất từ giảm dần:")
for word, count in sorted_words:
    print(f"{word}: {count}")

#bai 3 file on tap
import pandas as pd

# Giả sử dữ liệu từ CSV:
data = {
    "OrderID": [1001, 1002, 1003],
    "CustomerID": ["C001", "C002", "C003"],
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Quantity": [1, 2, 1],
    "Price": [800, 20, 50],
    "OrderYear": [2023, 2021, 2022]
}

df = pd.DataFrame(data)

# Lọc các đơn hàng năm 2023
df_2023 = df[df["OrderYear"] == 2023]

# Thống kê
so_don = df_2023.shape[0]
tong_san_pham = df_2023["Quantity"].sum()
doanh_thu = (df_2023["Quantity"] * df_2023["Price"]).sum()

print("Số đơn hàng năm 2023:", so_don)
print("Tổng số sản phẩm bán:", tong_san_pham)
print("Tổng doanh thu:", doanh_thu)

# Sản phẩm bán chạy nhất
best_seller = df.groupby("Product")["Quantity"].sum().idxmax()
print("Sản phẩm bán chạy nhất:", best_seller)


#Bai 4file on tap
class NhanVien:
    def __init__(self, ho_ten, ma_nhan_vien):
        self.ho_ten = ho_ten
        self.ma_nhan_vien = ma_nhan_vien

    def tinh_luong(self):
        return 0

    def __eq__(self, other):
        return self.tinh_luong() == other.tinh_luong()

class NVVP(NhanVien):
    def __init__(self, ho_ten, ma_nhan_vien, so_gio_lam, luong_gio):
        super().__init__(ho_ten, ma_nhan_vien)
        self.so_gio_lam = so_gio_lam
        self.luong_gio = luong_gio

    def tinh_luong(self):
        return self.so_gio_lam * self.luong_gio

    def __str__(self):
        return f"{self.ho_ten} - NVVP - Lương: {self.tinh_luong()}"

class NVSX(NhanVien):
    def __init__(self, ho_ten, ma_nhan_vien, so_san_pham, tien_cong):
        super().__init__(ho_ten, ma_nhan_vien)
        self.so_san_pham = so_san_pham
        self.tien_cong = tien_cong

    def tinh_luong(self):
        return self.so_san_pham * self.tien_cong

    def __str__(self):
        return f"{self.ho_ten} - NVSX - Lương: {self.tinh_luong()}"

# Tạo đối tượng và so sánh
nv1 = NVVP("Nguyen Van A", "001", 160, 50)
nv2 = NVSX("Tran Thi B", "002", 800, 10)

print(nv1)
print(nv2)
print("Lương bằng nhau?", nv1 == nv2)

