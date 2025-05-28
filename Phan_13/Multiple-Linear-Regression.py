import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

#read data
df = pd.read_csv("sale.csv")

x = df[["tv", "radio", "newspaper"]]
y = df["sales"]

model = LinearRegression()

model.fit(x, y)

# sns.scatterplot(
#     data=df,
#     x="tv",
#     y="sales",
#     alpha=0.5
# )
# sns.scatterplot(
#     data=df,
#     x="radio",
#     y="sales",
#     alpha=0.5
# )
# sns.scatterplot(
#     data=df,
#     x="newspaper",
#     y="sales",
#     alpha=0.5
# )

# TV
plt.subplot(1, 3, 1)
sns.scatterplot(data=df, x="tv", y="sales", alpha=0.5)
plt.title("TV vs Sales")

# Radio
plt.subplot(1, 3, 2)
sns.scatterplot(data=df, x="radio", y="sales", alpha=0.5)
plt.title("Radio vs Sales")

# Newspaper
plt.subplot(1, 3, 3)
sns.scatterplot(data=df, x="newspaper", y="sales", alpha=0.5)
plt.title("Newspaper vs Sales")

plt.show()