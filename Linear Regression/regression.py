import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("oldFaithful.csv")

x = df["wait_time"]
y = df["eruption_time"]

correlation = y.corr(x)
print("Correlation: ", correlation)
plt.scatter(x,y)

#Creating the Model
model = np.polyfit(x, y, 1)
x_lin_reg = range(x.min(), x.max())
predict = np.poly1d(model)
y_lin_reg = predict(x_lin_reg)
plt.plot(x_lin_reg, y_lin_reg, color="orange")
print(model)
plt.show()

ax = sns.regplot(data=df, x="wait_time", y="eruption_time")
plt.show()