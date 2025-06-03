import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

#read data
df = pd.read_csv("dirty_cafe_sales.csv")

#Minh họa trực quan missing data trên biểu đồ
# fix, ax = plt.subplots(figsize=(15,8))
# sns.heatmap(df.isna(), cmap='Blues', cbar=False )
# plt.show()
#Lấy item
# x = df.iloc[:, 1:].values
#Lấy id
# y = df.iloc[:, :1].values

db_cafe = df.copy()

db_cafe['Quantity'] = pd.to_numeric(db_cafe['Quantity'], errors='coerce')
db_cafe['Price Per Unit'] = pd.to_numeric(db_cafe['Price Per Unit'], errors='coerce')
db_cafe['Total Spent'] = pd.to_numeric(db_cafe['Total Spent'], errors='coerce')

#Chuyển lỗi ERROR,UNKNOWN,'' sang nan
db_cafe.replace(['ERROR', 'UNKNOWN', ''], np.nan, inplace=True)
#Xử lý item thiếu
def item_guess(db_cafe):
    if 'Item' in db_cafe.columns and 'Price Per Unit' in db_cafe.columns:
        Item_default = {
            2.0 : 'Coffee',
            1.5: 'Tea',
            4.0: 'Sandwich',
            5.0: 'Salad',
            3.0: 'Cake',
            1.0: 'Cookie' 
        }

        db_cafe['Item'] = db_cafe.apply(
            lambda row: Item_default.get(row['Price Per Unit'], row['Item'])
            if pd.isna(row['Item']) else row['Item'],
            axis = 1 # Giúp hoạt động từng dòng
        )

    return db_cafe

db_cafe = item_guess(db_cafe)
# print(db_cafe.info())
# print(db_cafe[db_cafe['Item'].isna()])
imputer_item = SimpleImputer(missing_values=np.nan, strategy='most_frequent')# Giá trị được nhiều nhất
db_cafe[['Item']] = imputer_item.fit_transform(db_cafe[['Item']])
#Xử lý price thiếu sau khi có item
def item_price(db_cafe):
    if 'Item' in db_cafe.columns and 'Price Per Unit' in db_cafe.columns:
        db_cafe[(db_cafe['Item'] == 'Coffee') & (db_cafe['Price Per Unit'].isna())] = 2.0 
        db_cafe[(db_cafe['Item'] == 'Tea') & (db_cafe['Price Per Unit'].isna())] = 1.5 
        db_cafe[(db_cafe['Item'] == 'Sandwich') & (db_cafe['Price Per Unit'].isna())] = 4.0 
        db_cafe[(db_cafe['Item'] == 'Salad') & (db_cafe['Price Per Unit'].isna())] = 5.0
        db_cafe[(db_cafe['Item'] == 'Cake') & (db_cafe['Price Per Unit'].isna())] = 3.0 
        db_cafe[(db_cafe['Item'] == 'Cookie') & (db_cafe['Price Per Unit'].isna())] = 1.0 
        db_cafe[(db_cafe['Item'] == 'Smoothie') & (db_cafe['Price Per Unit'].isna())] = 4.0 
        db_cafe[(db_cafe['Item'] == 'Juice') & (db_cafe['Price Per Unit'].isna())] = 3.0
    return db_cafe
db_cafe = item_price(db_cafe)
# Xử lý quantity và price thiếu
db_cafe['Quantity'] = db_cafe['Quantity'].fillna(db_cafe['Total Spent'] / db_cafe['Price Per Unit'])
db_cafe['Price Per Unit'] = db_cafe['Price Per Unit'].fillna(db_cafe['Total Spent'] / db_cafe['Quantity'])
# Xử lý quantity thiếu
imputer_total = SimpleImputer(missing_values=np.nan, strategy='median')# Giá trị trung vị
db_cafe[['Quantity']] = imputer_total.fit_transform(db_cafe[['Quantity']])
# Xử lý total thiếu
db_cafe['Total Spent'] = db_cafe['Total Spent'].fillna(db_cafe['Price Per Unit'] * db_cafe['Quantity'])
# print(db_cafe[db_cafe['Total Spent'].isna()])
# print(db_cafe.info())
imputer_payment = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer_location = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

db_cafe[['Payment Method']] = imputer_payment.fit_transform(db_cafe[['Payment Method']])
db_cafe[['Location']] = imputer_location.fit_transform(db_cafe[['Location']])

print(db_cafe.info())

#Chuẩn hóa dữ liệu bằng StandardScaler
scaler_db = StandardScaler()
db_cafe_col = ['Quantity', 'Price Per Unit', 'Total Spent'] 
db_cafe[db_cafe_col] = scaler_db.fit_transform(db_cafe[db_cafe_col])

print(db_cafe[db_cafe_col].describe())

plt.figure(figsize=(12, 6))
sns.boxplot(data=db_cafe[['Quantity', 'Price Per Unit', 'Total Spent']])
plt.title("Boxplot for Outlier Detection")
plt.show()