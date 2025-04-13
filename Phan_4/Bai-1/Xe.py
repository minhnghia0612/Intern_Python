from datetime import datetime

class Xe:
    def __init__(self, soVe="", thoiDiemVao="", thoiDiemRa="", loaiXe=0):
        self.__soVe= soVe;
        self.__thoiDiemVao= thoiDiemVao;
        self.__thoiDiemRa= thoiDiemRa;
        self._loaiXe=loaiXe;

    def get_soVe(self):
        return self.__soVe
    def set_soVe(self,value):
        self.__soVe = value
    def get_thoiDiemVao(self):
        return self.__thoiDiemVao
    def set_thoiDiemVao(self,value):
        self.__thoiDiemVao= value
    def get_thoiDiemRa(self):
        return self.__thoiDiemRa
    def set_thoiDiemRa(self,value):
        self.__thoiDiemRa = value
    def get_loaiXe(self):
        return self._loaiXe
    def set_loaiXe(self,value):
        if value in [0,2,4]:
            self._loaiXe=value
        else:
            raise ValueError("Loại xe không được chấp nhận!")
    def get_tenLoaiXe(self):
        dict_loaiXe={
            0:"Xe đạp",
            2:"Xe máy",
            4:"Xe ô tô"
            }
        return dict_loaiXe.get(self._loaiXe,"Không xác định")
    
    @classmethod
    def from_string(cls, xe_str):
        parts = xe_str.strip().split(';')
        soVe= parts[0]
        thoiDiemVao = datetime.strptime(parts[1], '%d/%m/%Y %H:%M')
        thoiDiemRa = None if parts[2].strip().lower() == "null" else datetime.strptime(parts[2], '%d/%m/%Y %H:%M')
        loaiXe = int(parts[3])

        return cls(soVe,thoiDiemVao,thoiDiemRa,loaiXe)

class fileReader:
    def __init__(self,filepath):
        self.fileReader= filepath

    def readfile(self):
        danhSachXe=[]
        try:
            with open(self.fileReader, 'r',encoding='utf-8') as file:
                for line in file:
                    try:
                        xe= Xe.from_string(line)
                        danhSachXe.append(xe)
                    except ValueError as e:
                        print(f"Có lỗi ở dòng này:{line.strip()}.{e}")
        except FileNotFoundError:
            print(f"Có lỗi khi đọc file {self.fileReader}")
        except Exception as e:
            print(f"Có lỗi:{e}")

        return danhSachXe