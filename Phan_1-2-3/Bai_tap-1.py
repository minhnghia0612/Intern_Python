#Problem:
# Nhận 1 danh sách các số từ người dùng
# Tính trung bình của các số trong danh sách
# Tìm giá trị lớn nhất và nhỏ nhất trong danh sách.
# In ra kết quả.
#Solution
# Danh sách từ người dùng có thể nhập liên tiếp ngăn cách bằng dấu space hoặc ";" hoặc ","
# Giá trị tb = sum / len, max , min
from functools import reduce

try:
    a= input("\nNhập các số: ").split(" ")
    b= [float(i) for i in a]
    #C1
    avg= sum(b) / len(b)
    maxDanhSach= max(b)
    minDanhSach= min(b)
    #C2
    # avg = reduce(lambda x,y: x+y, b) / len(b)
    # maxDanhSach = reduce(lambda x,y: x if x>y else y, b)
    # minDanhSach = reduce(lambda x,y: x if x<y else y, b)

    print(f"Trung bình các số trong danh sách:{avg}")
    print(f"Giá trị lớn nhất: {maxDanhSach}")
    print(f"Giá trị bé nhất: {minDanhSach}")
except ValueError:
    print("ops")
