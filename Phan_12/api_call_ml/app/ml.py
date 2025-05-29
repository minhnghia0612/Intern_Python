import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib

# read data
df = pd.read_csv("Housing.csv")
# area of a house
# number of house bedrooms
# number if bathrooms
# Number of House Stories #floor
df.columns = ["price" ,"area", "bedrooms", "bathrooms", "stories"]
print(df)

# Xử lý dữ liệu
Q1= df["area"].quantile(0.25)
Q3= df["area"].quantile(0.75)
IQR = Q3 - Q1  
df_clean = df[~((df["area"] < (Q1 - 1 * IQR)) | (df["area"] > (Q3 + 1 * IQR)))]

# sns.boxplot(y=df_clean["area"], color="lightblue")
# plt.show()
# print("Số lượng dữ liệu sau khi loại bỏ outliers:", len(df_clean))
# print("Số lượng dữ liệu ban đầu:", len(df))

x = df_clean[["area", "bedrooms", "bathrooms", "stories"]]
y = df_clean["price"]
model = LinearRegression()
model.fit(x, y)

# Lưu mô hình đã huấn luyện
joblib.dump(model, "housing_model.pkl")

# y_pred = model.predict(x)

# sns.scatterplot(
#     data=df_clean,
#     x="area",
#     y="price",
#     alpha=0.5
# )

# sns.lineplot(
#     x = df_clean["area"],
#     y = y_pred,
#     linewidth = 1.5,
#     color = 'red'
# )

# plt.title("Giá nhà theo diện tích")
# plt.xlabel("Area")  
# plt.ylabel("Price")
# plt.show()


# # dữ liệu đã được làm sạch tuy nhiên việc phân bố vẫn chưa được đồng đều để vẽ