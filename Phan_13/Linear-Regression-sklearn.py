import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# read data
df = pd.read_csv("sale.csv")

x = df[["tv"]]
y = df["sales"]

# Mô hình train
model = LinearRegression()
# Fit mô hình với dữ liệu (tìm m và b)
model.fit(x, y)

x_new = np.array([[1000]])  # Dữ liệu mới để dự đoán

print("Dự đoán doanh thu bán hàng khi chi 1000$ cho quảng cáo TV:", model.predict(x_new)[0])
print ("Intercept:(b)", model.intercept_)
print ("Coefficients(m):", model.coef_[0])
