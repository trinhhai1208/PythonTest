# Khai báo cấu trúc dữ liệu môn học và danh sách sinh viên đăng ký
mon_hoc_dict = {}

def nhap_mon_hoc():
    n = int(input("Nhập số môn học: "))
    for i in range(n):
        print(f"\n--- Nhập thông tin môn học thứ {i+1} ---")
        ma_mon = input("Mã môn: ")
        ten_mon = input("Tên môn: ")
        tin_chi = int(input("Số tín chỉ: "))
        hoc_ky = int(input("Học kỳ: "))
        giang_vien = input("Tên giảng viên: ")
        mon_hoc_dict[ma_mon] = {
            "ten_mon": ten_mon,
            "tin_chi": tin_chi,
            "hoc_ky": hoc_ky,
            "giang_vien": giang_vien,
            "sinh_vien": []
        }

def nhap_sinh_vien():
    while True:
        ma_mon = input("\nNhập mã môn cần đăng ký (hoặc 'exit' để dừng): ")
        if ma_mon.lower() == "exit":
            break
        if ma_mon not in mon_hoc_dict:
            print("Mã môn không tồn tại.")
            continue
        sv = {
            "ho_ten": input("Họ tên sinh viên: "),
            "gioi_tinh": input("Giới tính: "),
            "ngay_sinh": input("Ngày sinh (dd/mm/yyyy): "),
            "dia_chi": input("Địa chỉ: ")
        }
        mon_hoc_dict[ma_mon]["sinh_vien"].append(sv)

def tinh_tong_luot_dang_ky():
    return sum(len(mon["sinh_vien"]) for mon in mon_hoc_dict.values())

def in_danh_sach():
    for ma_mon, mon in mon_hoc_dict.items():
        print(f"\n--- Môn học: {mon['ten_mon']} ({ma_mon}) ---")
        print(f"Tín chỉ: {mon['tin_chi']}, Học kỳ: {mon['hoc_ky']}, Giảng viên: {mon['giang_vien']}")
        print("Danh sách sinh viên:")
        for sv in mon["sinh_vien"]:
            print(f" - {sv['ho_ten']}, {sv['gioi_tinh']}, {sv['ngay_sinh']}, {sv['dia_chi']}")

# Chạy chương trình Câu 1
print("=== CÂU 1: QUẢN LÝ MÔN HỌC ===")
nhap_mon_hoc()
nhap_sinh_vien()
print(f"\n>> Tổng số lượt đăng ký: {tinh_tong_luot_dang_ky()}")
in_danh_sach()
