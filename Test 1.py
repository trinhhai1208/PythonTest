# Hàm nhập dữ liệu từ bàn phím cho từ điển sinh viên
def nhap_thong_tin_sinh_vien():
    n = int(input("Nhập số lượng sinh viên: "))
    sinh_vien = {}
    for _ in range(n):
        ma_sinh_vien = input("Nhập mã sinh viên: ")
        so_tin_chi = int(input(f"Nhập số tín chỉ đã học của sinh viên {ma_sinh_vien}: "))
        sinh_vien[ma_sinh_vien] = so_tin_chi
    return sinh_vien


# Hàm khởi tạo từ điển lớp học phần
def khoi_tao_lop_hoc():
    lop_hoc = {
        "CS101": "Lập trình C",
        "MA202": "Toán cao cấp",
        "PH303": "Vật lý học",
        "EN404": "Tiếng Anh chuyên ngành"
    }
    return lop_hoc


# Hàm kiểm tra sinh viên "2024123456"
def kiem_tra_sinh_vien(sinh_vien):
    if "2024123456" in sinh_vien:
        print("Sinh viên 2024123456 có trong từ điển.")
        if sinh_vien["2024123456"] < 100:
            print("Số tín chỉ đã học của sinh viên này dưới 100, bổ sung đủ 100 tín chỉ.")
            sinh_vien["2024123456"] = 100
    else:
        print("Sinh viên 2024123456 không có trong từ điển.")
    return sinh_vien


# Hàm xóa sinh viên có số tín chỉ = 0
def xoa_sinh_vien_tin_chi_0(sinh_vien):
    sinh_vien = {k: v for k, v in sinh_vien.items() if v != 0}
    return sinh_vien


# Hàm chuyển đổi từ điển sang hai list
def chuyen_sang_list(sinh_vien):
    list_ma_sinh_vien = list(sinh_vien.keys())
    list_so_tin_chi = list(sinh_vien.values())
    return list_ma_sinh_vien, list_so_tin_chi


# Hàm in 3 phần tử đầu tiên của list ma_sinh_vien và 3 phần tử cuối của list so_tin_chi
def in_list(list_ma_sinh_vien, list_so_tin_chi):
    print("3 phần tử đầu tiên của List 1 (Mã sinh viên):", list_ma_sinh_vien[:3])
    print("3 phần tử cuối cùng của List 2 (Số tín chỉ):", list_so_tin_chi[-3:])


# Main function thực hiện toàn bộ các công việc
def main():
    # Nhập dữ liệu sinh viên
    sinh_vien = nhap_thong_tin_sinh_vien()

    # Khởi tạo từ điển lớp học phần
    lop_hoc = khoi_tao_lop_hoc()

    # Kiểm tra sinh viên "2024123456" và bổ sung tín chỉ nếu cần
    sinh_vien = kiem_tra_sinh_vien(sinh_vien)

    # Xóa sinh viên có số tín chỉ bằng 0
    sinh_vien = xoa_sinh_vien_tin_chi_0(sinh_vien)

    # Chuyển dữ liệu sang hai list
    list_ma_sinh_vien, list_so_tin_chi = chuyen_sang_list(sinh_vien)

    # In 3 phần tử đầu tiên của list ma_sinh_vien và 3 phần tử cuối của list so_tin_chi
    in_list(list_ma_sinh_vien, list_so_tin_chi)


# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()
