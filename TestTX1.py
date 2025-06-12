def nhap_danh_sach_hang():
    danh_sach = []
    so_luong = int(input("Nhập số lượng mặt hàng: "))
    for i in range(so_luong):
        print(f"\nNhập thông tin mặt hàng thứ {i+1}:")
        ma = input("Mã hàng: ")
        ten = input("Tên mặt hàng: ")
        sl = int(input("Số lượng: "))
        gia = int(input("Giá tiền: "))
        tong = sl * gia
        danh_sach.append({
            "ma": ma,
            "ten": ten,
            "so_luong": sl,
            "gia": gia,
            "tong": tong
        })
    return danh_sach

def hien_thi_danh_sach(danh_sach):
    print("\nDanh sách hàng hóa:")
    print("{:<10} {:<20} {:<10} {:<15} {:<15}".format("Mã hàng", "Tên mặt hàng", "Số lượng", "Giá tiền", "Tổng tiền"))
    for hang in danh_sach:
        print("{:<10} {:<20} {:<10} {:<15,} {:<15,}".format(
            hang["ma"], hang["ten"], hang["so_luong"], hang["gia"], hang["tong"]
        ))

def tim_mat_hang_nho_nhat(danh_sach):
    min_tong = min(hang["tong"] for hang in danh_sach)
    return [hang for hang in danh_sach if hang["tong"] == min_tong]

def dem_mat_hang_so_luong_lon_va_gia_thap(danh_sach):
    count = 0
    for hang in danh_sach:
        if hang["so_luong"] > 5 and hang["tong"] < 1_000_000:
            count += 1
    return count

# Chương trình chính
danh_sach_hang = nhap_danh_sach_hang()
hien_thi_danh_sach(danh_sach_hang)

# Tìm mặt hàng có tổng tiền nhỏ nhất
hang_nho_nhat = tim_mat_hang_nho_nhat(danh_sach_hang)
print("\nCác mặt hàng có tổng tiền nhỏ nhất:")
hien_thi_danh_sach(hang_nho_nhat)

# Đếm số lượng mặt hàng thỏa điều kiện
so_mat_hang = dem_mat_hang_so_luong_lon_va_gia_thap(danh_sach_hang)
print(f"\nSố mặt hàng có số lượng > 5 và tổng tiền < 1,000,000 VND là: {so_mat_hang}")
