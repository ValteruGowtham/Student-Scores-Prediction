# -*- coding: utf-8 -*-
"""Predict Student Scores .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gXSops5J4SHEi4w2oUJlk5A5LnE3gxS2
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('student-scores.csv')

df.head()

df.isnull().sum()

df['total_score'] = df['math_score'] + df['history_score'] + df['physics_score'] + df['chemistry_score'] + df['biology_score'] + df['english_score'] + df['geography_score']

def encoding(df, col):
  df[col] = df[col].map({True: 1,False: 0})

col = ['part_time_job', 'extracurricular_activities']
for i in col:
  encoding(df, i)

X = df[['part_time_job', 'absence_days', 'extracurricular_activities','weekly_self_study_hours']]
Y = df['total_score']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(Y_test, y_pred)
r2 = r2_score(Y_test, y_pred)

print("MSE: ", mse)
print("R2: ", r2)

## linear regression drawn based on study hours
x_taken = df[['weekly_self_study_hours']]
y_taken = df['total_score']
model = LinearRegression()
model.fit(x_taken, y_taken)
y_pred = model.predict(x_taken)
plt.scatter(x_taken, y_taken, color = 'blue', label = 'Actual values')
plt.plot(x_taken, y_pred, color = 'red', label = 'Predicted values')
plt.xlabel('Weekly self study hours')
plt.ylabel('Total score')
plt.legend()
plt.show()

## input from user -> study hours
hours = int(input("no.of study hours: "))
predicted_score = model.predict(pd.DataFrame([[hours]], columns = ['weekly_self_study_hours']))
print(f"Predicted score for studying {hours} hours = {predicted_score[0]:.2f}")