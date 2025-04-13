from Xe import fileReader

def main():
    file = fileReader('D:\\HDT_PY/Phan_4/Bai-1/xe.txt')
    danhSachXe = file.readfile()

    print(f'{"STT":<5} {"Số vé":<10} {"Thời điểm vào":<20} {"Thời điểm ra":<20} {"Loại xe":<10}')
    print("=" * 65)
    
    stt = 1
    for xe in danhSachXe:
        print(f"{stt:<5} {xe.get_soVe():<10} "
                f"{xe.get_thoiDiemVao().strftime('%d/%m/%Y %H:%M'):<20} "
                f"{xe.get_thoiDiemRa().strftime('%d/%m/%Y %H:%M') if xe.get_thoiDiemRa() else 'Chưa lấy':<20} "
                f"{xe.get_tenLoaiXe():<10}")
        stt += 1

if __name__== "__main__":
    main()