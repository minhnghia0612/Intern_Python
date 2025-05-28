import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read data
df = pd.read_csv("sale.csv")
df.columns = ["tv", "radio", "newspaper", "sales"]
print(df)

# Dùng scatter plot để vẽ biểu đồ phân tán giữa tv và sales
sns.scatterplot(
    data = df,
    x = "tv",
    y = "sales",
)
# show biểu đồ
#plt.show()

# Tính đường chéo hồi quy tuyến tính
# Get các điểm
x = df["tv"].values
y = df["sales"].values

# Tìm b và m 
N = x.shape[0]
m = (N * np.sum(x*y) - np.sum(x) * np.sum(y)) / (N * np.sum(x**2) - np.sum(x)**2)
b = (np.sum(y) - m*np.sum(x))/N

print(m,b)

# Vẽ đường hồi quy tuyến tính y = b + m * x
# Tìm vị trí đầu tiên 
x_min = np.min(x)
y_min = b + m * x_min
# Tìm vị trí cuối cùng
x_max = np.max(x)
y_max = b + m * x_max

fig, ax = plt.subplots()
#fig: toàn bộ khung hình, ax: trục để vẽ biểu đồ lên.

sns.scatterplot(
    data = df,
    x = "tv",
    y = "sales",
    ax = ax, # vẽ biểu đồ phân tán lên trục ax
    alpha = 0.5 # độ trong suốt của điểm
)
# Vẽ đưuòng hồi quy
sns.lineplot(
    x = [x_min, x_max],
    y = [y_min, y_max],
    linewidth = 1.5,
    color = "red"
)
plt.show()


