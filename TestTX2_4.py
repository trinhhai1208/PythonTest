class TacGia:
    def __init__(self, ten, quoc_tich):
        self.__ten = ten
        self.__quoc_tich = quoc_tich

    def __str__(self):
        return f"{self.__ten} ({self.__quoc_tich})"

class Sach:
    def __init__(self, ma_sach, ten_sach, nam_xuat_ban, tac_gia: TacGia):
        self._ma_sach = ma_sach
        self._ten_sach = ten_sach
        self._nam_xuat_ban = nam_xuat_ban
        self._tac_gia = tac_gia

    def get_tuoi_sach(self):
        return 2025 - self._nam_xuat_ban

    def __str__(self):
        return f"{self._ten_sach} [{self._ma_sach}] - {self._nam_xuat_ban} ({self.get_tuoi_sach()} năm)\nTác giả: {self._tac_gia}"

    def __add__(self, other):
        return f"Tổng hợp: {self._ten_sach} & {other._ten_sach}"

class GiaoTrinh(Sach):
    def __init__(self, ma_sach, ten_sach, nam_xuat_ban, tac_gia, mon_hoc):
        super().__init__(ma_sach, ten_sach, nam_xuat_ban, tac_gia)
        self.__mon_hoc = mon_hoc

    def __str__(self):
        return super().__str__() + f"\nLoại: Giáo trình - Môn học: {self.__mon_hoc}"

class ThamKhao(Sach):
    def __init__(self, ma_sach, ten_sach, nam_xuat_ban, tac_gia, linh_vuc):
        super().__init__(ma_sach, ten_sach, nam_xuat_ban, tac_gia)
        self.__linh_vuc = linh_vuc

    def __str__(self):
        return super().__str__() + f"\nLoại: Tham khảo - Lĩnh vực: {self.__linh_vuc}"

# Chương trình chính
if __name__ == "__main__":
    tg1 = TacGia("Trần Văn A", "Việt Nam")
    tg2 = TacGia("John Doe", "Mỹ")

    gt = GiaoTrinh("GT01", "Python Cơ Bản", 2021, tg1, "Lập trình")
    tk = ThamKhao("TK01", "AI Cho Người Mới", 2019, tg2, "Trí tuệ nhân tạo")

    print(gt)
    print()
    print(tk)
    print("\nKết quả phép cộng sách:")
    print(gt + tk)
