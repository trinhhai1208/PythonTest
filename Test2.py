def nhap_danh_sach_hang():
    danh_sach = []
    n = int(input("Nhập số lượng mặt hàng: "))
    for i in range(n):
        print(f"\nNhập thông tin mặt hàng thứ {i+1}:")
        ma = input("  Mã hàng: ")
        ten = input("  Tên mặt hàng: ")
        sl = int(input("  Số lượng: "))
        gia = int(input("  Giá tiền: "))
        tong_tien = sl * gia
        danh_sach.append({
            'ma': ma,
            'ten': ten,
            'sl': sl,
            'gia': gia,
            'tong_tien': tong_tien
        })
    return danh_sach

def hien_thi_bang(danh_sach):
    print(f"\n{'Mã hàng':<10} {'Tên mặt hàng':<20} {'Số lượng':<10} {'Giá tiền':<12} {'Tổng tiền':<15}")
    print("-" * 70)
    for item in danh_sach:
        print(f"{item['ma']:<10} {item['ten']:<20} {item['sl']:<10} {item['gia']:<12,} {item['tong_tien']:<15,}")

def tim_tong_tien_nho_nhat(danh_sach):
    return min(item['tong_tien'] for item in danh_sach)

def tim_mat_hang_tong_tien_nho_nhat(danh_sach):
    min_tien = tim_tong_tien_nho_nhat(danh_sach)
    return [item for item in danh_sach if item['tong_tien'] == min_tien]

def dem_mat_hang_so_luong_lon_tong_tien_nho(danh_sach):
    count = 0
    for item in danh_sach:
        if item['sl'] > 5 and item['tong_tien'] < 1_000_000:
            count += 1
    return count

# === Chương trình chính ===
danh_sach = nhap_danh_sach_hang()

# b) Hiển thị danh sách mặt hàng
print("\nDanh sách các mặt hàng:")
hien_thi_bang(danh_sach)

# c) Tìm giá trị tổng tiền nhỏ nhất
min_tong_tien = tim_tong_tien_nho_nhat(danh_sach)
print(f"\n➡ Tổng tiền nhỏ nhất là: {min_tong_tien:,} VNĐ")

# d) Tìm và hiển thị mặt hàng có tổng tiền nhỏ nhất
mat_hang_min = tim_mat_hang_tong_tien_nho_nhat(danh_sach)
print("\n➡ Mặt hàng có tổng tiền nhỏ nhất:")
hien_thi_bang(mat_hang_min)

# e) Đếm mặt hàng có sl > 5 và tổng tiền < 1 triệu
so_luong_dap_ung = dem_mat_hang_so_luong_lon_tong_tien_nho(danh_sach)
print(f"\n➡ Số mặt hàng có SL > 5 và tổng tiền < 1,000,000 VNĐ: {so_luong_dap_ung}")
