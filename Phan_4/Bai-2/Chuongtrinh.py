from Sach import fileReader, sach


def menu():
    print("\n----- MENU QUẢN LÝ SÁCH -----")
    print("1. Thêm sách mới")
    print("2. Tìm kiếm sách")
    print("3. Xóa sách")
    print("4. Hiển thị danh sách sách")
    print("5. Thoát")
    choice = input("Chọn chức năng (1-5): ")
    return choice


def main():
    file = fileReader('D:\\HDT_PY/Phan_4/Bai-2/Sach.txt')
    danhSach = file.readFile()

    while True:
        choice = menu()

        if choice == '1':
            ma=input("Nhập mã sách: ")
            tenSach=input("Nhập tên sách: ")
            tacGia=input("Nhập tên tác giả:")
            try:
                namXuatBan=int(input("Nhập năm xuất bản: "))
            except ValueError:
                print("Năm không hợp lệ")
                namXuatBan=0
            s = sach(ma,tenSach,tacGia,namXuatBan)
            danhSach.append(s)
            print("Đã thêm sách mới.")

        elif choice == '2':
            maCanTim = input("Nhập mã sách cần tìm: ")
            found = False
            for s in danhSach:
                if s.getmaSach() == maCanTim:
                    print("Tìm thấy sách:")
                    s.hienThi()
                    found = True
                    break
            if not found:
                print("Không tìm thấy sách.")

        elif choice == '3':
            maXoa = input("Nhập mã sách cần xóa: ")
            for i, s in enumerate(danhSach):
                if s.getmaSach() == maXoa:
                    del danhSach[i]
                    print("✅ Đã xóa sách.")
                    break
            else:
                print("Không tìm thấy sách để xóa.")

        elif choice == '4':
            print(f'\n{"STT":<5} {"Mã sách":<10} {"Tên sách":<15} {"Tác giả":<20} {"Năm xuất bản":<20}')
            print("=" * 70)
            for i, s in enumerate(danhSach, start=1):
                print(f'{i:<5}', end=" ")
                s.hienThi()

        elif choice == '5':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == '__main__':
    main()
