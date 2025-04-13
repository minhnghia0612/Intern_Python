class sach():
    def __init__(self,maSach="",tenSach="",tacGia="",namXuatBan=0):
        self.__maSach=maSach
        self.__tenSach=tenSach
        self.__tacGia=tacGia
        self.__namXuatBan=namXuatBan

    def getmaSach(self):
        return self.__maSach
    def gettenSach(self):
        return self.__tenSach
    def gettacGia(self):
        return self.__tacGia
    def getnamXuatBan(self):
        return self.__namXuatBan
    def setmaSach(self,maSach):
        self.__maSach=maSach
    def settenSach(self,tenSach):
        self.__tenSach=tenSach
    def settacGia(self,tacGia):
        self.__tacGia=tacGia
    def setnamXuatBan(self,namXuatBan):
        self.__namXuatBan=namXuatBan

    # def themSachMoi(self):
    #     self.__maSach=input("Nhập id sach: ")
    #     self.__tenSach=input("Nhập tên sách: ")
    #     self.__tacGia=input("Nhập tên tác giả: ")
    #     try:
    #         self.__namXuatBan=int(input("Nhập nam xuất bản: "))
    #     except ValueError:
    #         print("Năm phải là số nguyên")
    #         self.__namXuatBan = 0
    #
    # def timKiemSach(self):
    #     maSachCanTim=input("Nhập mã sách cần tim: ")
    #     if maSachCanTim == self.getmaSach():
    #         print(f"Đã tìm thấy sách:{self.gettenSach()}, Tác giả:{self.gettacGia()}, Năm xuất bản:{self.getnamXuatBan()}")
    #     else:
    #         print("Không tìm thấy sách")
    #
    # def xoaSach(self):
    #     maSachXoa=input("Nhập mã sách cần xóa: ")
    #     if maSachXoa == self.getmaSach():
    #         self.__maSach=""
    #         self.__tenSach=""
    #         self.__tacGia=""
    #         self.__namXuatBan=0
    #         print("Sách đã được xóa")
    #     else:
    #         print("Không tìm thấy sách để xóa")

    def hienThi(self):
        print(f"{self.getmaSach():<10} "
              f"{self.gettenSach():<15} "
              f"{self.gettacGia():<20} "
              f"{self.getnamXuatBan():<15}")

    @classmethod
    def fromstring(cls,sach_str):
        parts= sach_str.strip().split(" ")
        maSach=parts[0]
        tenSach=parts[1]
        tacGia=parts[2]
        namXuatBan=int(parts[3])

        return cls(maSach, tenSach, tacGia, namXuatBan)

class fileReader:
    def __init__(self,filepath):
        self.filepath=filepath
    def readFile(self):
        danhSach=[]
        try:
            with open(self.filepath,"r",encoding="utf-8") as f:
                for line in f:
                    try:
                        sachobj=sach.fromstring(line)
                        danhSach.append(sachobj)
                    except Exception as e:
                        print("WR",e)
        except FileNotFoundError:
            print("Lỗi khi đọc file")
        except Exception as e:
            print("WR",e)

        return danhSach
