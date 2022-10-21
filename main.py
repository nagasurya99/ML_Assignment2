import numpy as np
array1 = np.random.randint(1, 20, 15)  # declaring array of size 15 and declaring range
print(array1)  # printing array
array2 = np.reshape(array1, (3, 5))  # reshape function used to change the shape of the output
print(array2)  # printing second array
print(array2.shape)  # printing second array shape
max = np.amax(array2, axis=1)  # delcaring index position of max element
max = max[:, None]
array3 = np.where(array2 == max, 0, array2)  # replacing max element with zero
print(array3)  # printing final array

import pandas as pd

data = pd.read_csv("C:/Users/nagas/Downloads/data.csv")  # reading csv file
data.head()
data.describe()
data = data.fillna(data.mean())
print(data[['Maxpulse', 'Calories']].agg(['min', 'max', 'mean', 'count']))
print(data[(data.Calories < 1000) & (data.Calories > 500)])
print(data[(data.Calories > 500) & (data.Pulse < 100)])
df_modified = pd.DataFrame(data, columns=['Duration', 'Pulse', 'Calories'])
print(df_modified.head())
del data['Maxpulse']
print(data.head())
data['Calories'] = data['Calories'].astype("int")
print(data['Calories'].dtypes)
data.plot.scatter(x='Duration', y='Calories')  # printing plot

import matplotlib.pyplot as plt

languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'  # declared languages
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]  # declaring popularities
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]  # declaring colors
explode = (0.1, 0, 0, 0, 0, 0)
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)  # defining pie chart
plt.axis('equal')
plt.show()  # printing plot