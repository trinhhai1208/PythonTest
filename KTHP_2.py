class Nguoi:
    def __init__(self, ho_ten, ngay_sinh, dia_chi):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.dia_chi = dia_chi

    def __str__(self):
        return f"{self.ho_ten}, {self.ngay_sinh}, {self.dia_chi}"

class GiaoVien(Nguoi):
    def __init__(self, ho_ten, ngay_sinh, dia_chi, mon_day, trinh_do, so_nam_ct):
        super().__init__(ho_ten, ngay_sinh, dia_chi)
        self.mon_day = mon_day
        self.trinh_do = trinh_do
        self.so_nam_ct = so_nam_ct

    def __lt__(self, other):
        return self.so_nam_ct < other.so_nam_ct

    def __str__(self):
        return (f"{self.ho_ten}, {self.ngay_sinh}, {self.dia_chi}, "
                f"{self.mon_day}, {self.trinh_do}, {self.so_nam_ct} năm công tác")

def nhap_giao_vien():
    ds_gv = []
    n = int(input("Nhập số lượng giáo viên (n > 3): "))
    if n <= 3:
        print("Số lượng giáo viên phải lớn hơn 3.")
        return ds_gv

    for i in range(n):
        print(f"\n--- Nhập thông tin giáo viên thứ {i+1} ---")
        ho_ten = input("Họ tên: ")
        ngay_sinh = input("Ngày sinh: ")
        dia_chi = input("Địa chỉ: ")
        mon_day = input("Môn dạy: ")
        trinh_do = input("Trình độ (Cử nhân / Thạc sĩ / Tiến sĩ): ")
        so_nam_ct = int(input("Số năm công tác: "))
        gv = GiaoVien(ho_ten, ngay_sinh, dia_chi, mon_day, trinh_do, so_nam_ct)
        ds_gv.append(gv)
    return ds_gv

def in_va_luu_file(ds_gv):
    print("\n=== DANH SÁCH GIÁO VIÊN SAU KHI SẮP XẾP ===")
    with open("GIAOVIEN.TXT", "w", encoding="utf-8") as f:
        for gv in ds_gv:
            print(gv)
            f.write(str(gv) + "\n")

# Chương trình chính
ds_gv = nhap_giao_vien()
ds_gv.sort()
in_va_luu_file(ds_gv)
