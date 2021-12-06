#Iyanu Olukotun ATCS 2021 Data Science Project Data Visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

import numpy as np

artistTable = pd.read_csv('Data Science Project Music Data.csv')

artistGenre = pd.Series(artistTable['Main Genre'])

#Graphs
#pie chart
df1 = artistTable.groupby("Main Genre").count()
ax = df1.plot.pie(y="Total Songs", labels=df1.index, figsize=(15,9), legend = None)
ax.set_ylabel("Genre")
ax.yaxis.set_label_coords(-0.05, 0.5,)
ax.yaxis.label.set_size(16)
plt.show()

#Bar Graph Low
barGraph = pd.read_csv('Average Emotionalness Bar Graph Low.csv')
ax = sns.barplot(x="Artist", y="Average Emotionalness Bar Graph Low", data=barGraph, palette = "ch:start=.2,rot=-.3");
ax.set(ylim=(-35, 5))
plt.show()

#Bar Graph High
barGraph = pd.read_csv('Average Emotionalness Bar Graph High.csv')
bx = sns.barplot(x="Artist", y="Average Emotionalness Bar Graph High", data=barGraph, palette = "ch:s=-.2,r=.6");
bx.set(ylim=(0, 40))
plt.show()

#scatter plot - Average Loudness vs Average energy
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'pink', 'figure.facecolor':'lavenderblush'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Speechiness", y="Average Danceability", data=scatterPlot, height = 7, aspect = 1.4, markers=["+"], palette="mako").set(title='Average Loudness and Average Energy');
plt.show()

#Best Fit Line
x = artistTable["Average Speechiness"]
y = artistTable["Average Danceability"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Total Followers (Millions) and Average Popularity")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")



#scatter plot - Average Danceability vs Average Popularity
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'paleturquoise', 'figure.facecolor':'lightcyan'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Acousticness", y="Average Energy", data=scatterPlot, height = 7, aspect = 1.4, markers=["+"], palette="mako").set(title='Relationship Between Average Danceability and Average Popularity');
plt.show()

#Best Fit Line
x = artistTable["Average Acousticness"]
y = artistTable["Average Energy"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Average Danceability and Average Popularity")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")


#scatter plot - Average Speechiness vs Average Popularity
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'moccasin', 'figure.facecolor':'cornsilk'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Acousticness", y="Average Energy", data=scatterPlot, height = 7, aspect = 1.4, markers=["d"], palette="mako").set(title='Relationship Between Average Speechiness and Average Popularity');
plt.show()

#Best Fit Line
x = artistTable["Average Acousticness"]
y = artistTable["Average Energy"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Average Speechiness and Average Popularity")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")
#scatter plot - Average Energy vs Average Popularity
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'lightsalmon', 'figure.facecolor':'mistyrose'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Energy", y="Average Popularity", data=scatterPlot, height = 7, aspect = 1.4, markers=["v"], palette="mako").set(title='Relationship Between Average Energy and Average Popularity');
plt.show()

#Best Fit Line
x = artistTable["Average Energy"]
y = artistTable["Average Popularity"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Average Energy and Average Popularity")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")
#scatter plot - Percent Explicit Songs (%) vs Average Popularity
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'paleturquoise', 'figure.facecolor':'lightcyan'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Percent Explicit Songs (%)", y="Average Popularity", data=scatterPlot, height = 7, aspect = 1.4, markers=["^"], palette="mako").set(title='Relationship Between Percent Explicit Songs (%) and Average Popularity');
plt.show()

#Best Fit Line
x = artistTable["Percent Explicit Songs (%)"]
y = artistTable["Average Popularity"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Percent Explicit Songs (%) and Average Popularity")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")

#scatter plot - Average Loudness vs Average Popularity
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'lightgreen', 'figure.facecolor':'honeydew'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Speechiness", y="Average Danceability", data=scatterPlot, height = 7, aspect = 1.4, markers=["+"], palette="mako").set(title='Average Loudness and Average Energy');
plt.show()

#Best Fit Line
x = artistTable["Average Loudness"]
y = artistTable["Average Popularity"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Average Loudness and Average Popularity")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")

#scatter plot - Average Acousticness vs Average Popularity
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'thistle', 'figure.facecolor':'plum'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Acousticness", y="Average Popularity", data=scatterPlot, height = 7, aspect = 1.4, markers=["8"], palette="mako").set(title='Relationship Between Average Acousticness and Average Popularity');
plt.show()

#Best Fit Line
x = artistTable["Average Acousticness"]
y = artistTable["Average Popularity"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Average Acousticness and Average Popularity")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")


#Followers Relationship Scatterplots
#scatter plot - Average Danceability vs Total Followers (Millions)
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'moccasin', 'figure.facecolor':'bisque'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Danceability", y="Total Followers (Millions)", data=scatterPlot, height = 7, aspect = 1.4, markers=["+"], palette="mako").set(title='Relationship Between Average Danceability and Total Followers (Millions)');
plt.show()

#Best Fit Line
x = artistTable["Average Danceability"]
y = artistTable["Total Followers (Millions)"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Average Danceability and Total Followers (Millions)")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")

#scatter plot - Average Speechiness vs Total Followers (Millions)
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'plum', 'figure.facecolor':'thistle'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Speechiness", y="Total Followers (Millions)", data=scatterPlot, height = 7, aspect = 1.4, markers=["d"], palette="mako").set(title='Relationship Between Average Speechiness and Total Followers (Millions)');
plt.show()

#Best Fit Line
x = artistTable["Average Speechiness"]
y = artistTable["Total Followers (Millions)"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Average Speechiness and Total Followers (Millions)")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")

#scatter plot - Average Energy vs Total Followers (Millions)
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'palegoldenrod', 'figure.facecolor':'mintcream'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Energy", y="Total Followers (Millions)", data=scatterPlot, height = 7, aspect = 1.4, markers=["v"], palette="mako").set(title='Relationship Between Average Energy and Total Followers (Millions)');
plt.show()

#Best Fit Line
x = artistTable["Average Energy"]
y = artistTable["Total Followers (Millions)"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Average Energy and Total Followers (Millions)")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)
y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")

#scatter plot - Percent Explicit Songs (%) vs Total Followers (Millions)
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'lightcyan', 'figure.facecolor':'azure'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Percent Explicit Songs (%)", y="Total Followers (Millions)", data=scatterPlot, height = 7, aspect = 1.4, markers=["^"], palette="mako").set(title='Relationship Between Percent Explicit Songs (%) and Total Followers (Millions)');
plt.show()

#Best Fit Line
x = artistTable["Percent Explicit Songs (%)"]
y = artistTable["Total Followers (Millions)"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Percent Explicit Songs (%) and Total Followers (Millions)")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)
y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")

#scatter plot - Average Loudness vs Total Followers (Millions)
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'navajowhite', 'figure.facecolor':'burlywood'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Loudness", y="Total Followers (Millions)", data=scatterPlot, height = 7, aspect = 1.4, markers=["1"], palette="mako").set(title='Relationship Between Average Loudness and Total Followers (Millions)');
plt.show()

#Best Fit Line
x = artistTable["Average Loudness"]
y = artistTable["Total Followers (Millions)"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Average Loudness and Total Followers (Millions)")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")

#scatter plot - Average Acousticness vs Total Followers (Millions)
sns.set_theme(color_codes=True)
sns.set(rc={'axes.facecolor':'lightyellow', 'figure.facecolor':'lightgoldenrodyellow'})
scatterPlot = pd.read_csv('Data Science Project Music Data.csv')
sns.lmplot(x="Average Acousticness", y="Total Followers (Millions)", data=scatterPlot, height = 7, aspect = 1.4, markers=["8"], palette="mako").set(title='Relationship Between Average Acousticness and Total Followers (Millions)');
plt.show()

#Best Fit Line
x = artistTable["Average Acousticness"]
y = artistTable["Total Followers (Millions)"]
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_mean, y_mean
Sxy = sum(x * y) - n * x_mean * y_mean
Sxx = sum(x * x) - n * x_mean * x_mean
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("Relationship Between Average Acousticness and Total Followers (Millions)")
print('slope b1 is', f'{b1:.20f}')
print('intercept b0 is', b0)

y_pred = b1 * x + b0
error = y - y_pred
se = np.sum(error ** 2)
mse = se / n
rmse = np.sqrt(mse)
SSt = np.sum((y - y_mean) ** 2)
R2 = 1 - (se / SSt)
print('R square is', R2)
print(" ")



