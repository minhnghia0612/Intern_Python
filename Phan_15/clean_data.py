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
imputer_item = SimpleImputer(missing_values=np.nan, strategy='most_frequent')# Giá trị được nhiều nhất
db_cafe[['Item']] = imputer_item.fit_transform(db_cafe[['Item']])
#Xử lý price thiếu sau khi có item
def item_price(db):
    price_map = {
        'Coffee': 2.0,
        'Tea': 1.5,
        'Sandwich': 4.0,
        'Salad': 5.0,
        'Cake': 3.0,
        'Cookie': 1.0,
        'Smoothie': 4.0,
        'Juice': 3.0
    }
    for item, price in price_map.items():
        db.loc[(db['Item'] == item) & (db['Price Per Unit'].isna()), 'Price Per Unit'] = price
    return db
db_cafe = item_price(db_cafe)
# Xử lý quantity và price thiếu
db_cafe['Quantity'] = db_cafe['Quantity'].fillna(db_cafe['Total Spent'] / db_cafe['Price Per Unit'])
db_cafe['Price Per Unit'] = db_cafe['Price Per Unit'].fillna(db_cafe['Total Spent'] / db_cafe['Quantity'])
# Xử lý quantity thiếu
imputer_total = SimpleImputer(missing_values=np.nan, strategy='median')# Giá trị trung vị
db_cafe[['Quantity']] = imputer_total.fit_transform(db_cafe[['Quantity']])
# Xử lý total thiếu
db_cafe['Total Spent'] = db_cafe['Total Spent'].fillna(db_cafe['Price Per Unit'] * db_cafe['Quantity'])
imputer_payment = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer_location = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

db_cafe[['Payment Method']] = imputer_payment.fit_transform(db_cafe[['Payment Method']])
db_cafe[['Location']] = imputer_location.fit_transform(db_cafe[['Location']])
