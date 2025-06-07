class CauThu:
    def __init__(self, ho_ten, vi_tri, quoc_tich):
        self.__ho_ten = ho_ten
        self.__vi_tri = vi_tri
        self.__quoc_tich = quoc_tich

    def __str__(self):
        return f"{self.__ho_ten} - {self.__vi_tri} ({self.__quoc_tich})"

class DoiBong:
    def __init__(self, ten_doi, hlv):
        self.__ten_doi = ten_doi
        self.__hlv = hlv
        self.__ds_cau_thu = []

    def them_cau_thu(self, cau_thu):
        if isinstance(cau_thu, CauThu):
            self.__ds_cau_thu.append(cau_thu)

    def get_danh_sach(self):
        return self.__ds_cau_thu

    def __add__(self, other):
        doi_moi = DoiBong(f"{self.__ten_doi} + {other.__ten_doi}", f"{self.__hlv} & {other.__hlv}")
        for ct in self.__ds_cau_thu + other.__ds_cau_thu:
            doi_moi.them_cau_thu(ct)
        return doi_moi

    def __str__(self):
        danh_sach = "\n".join(str(ct) for ct in self.__ds_cau_thu)
        return f"Đội: {self.__ten_doi} | HLV: {self.__hlv}\nCầu thủ:\n{danh_sach}"

class DoiTuyenQuocGia(DoiBong):
    def __init__(self, ten_doi, hlv, quoc_gia):
        super().__init__(ten_doi, hlv)
        self.__quoc_gia = quoc_gia

    def __str__(self):
        return f"[ĐTQG - {self.__quoc_gia}]\n" + super().__str__()

# Chương trình chính
if __name__ == "__main__":
    dt1 = DoiTuyenQuocGia("Việt Nam A", "Park Hang Seo", "Việt Nam")
    dt1.them_cau_thu(CauThu("Quang Hải", "Tiền vệ", "Việt Nam"))
    dt1.them_cau_thu(CauThu("Tiến Linh", "Tiền đạo", "Việt Nam"))

    dt2 = DoiTuyenQuocGia("Nhật Bản B", "Moriyasu", "Nhật Bản")
    dt2.them_cau_thu(CauThu("Kubo", "Tiền đạo", "Nhật Bản"))
    dt2.them_cau_thu(CauThu("Endo", "Hậu vệ", "Nhật Bản"))

    print(dt1)
    print()
    print(dt2)
    print("\nĐội sau khi gộp:\n")
    dt_moi = dt1 + dt2
    print(dt_moi)
