from clean_data import db_cafe
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
ct = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(), ['Item', 'Payment Method', 'Location']) 
    ],
    remainder='passthrough'  # Giữ nguyên các cột khác
)

db_cafe = db_cafe.drop(columns=['Transaction ID'])

X = ct.fit_transform(db_cafe)

print(X)
y = db_cafe['Total Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

print(mse)