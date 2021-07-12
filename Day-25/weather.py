# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

import csv

import numpy as np

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    # print(data)
    temperatures = []
    for row in data:
        # print(row)
        # noinspection PyBroadException
        try:
            temperatures.append(int(row[1]))
        except:
            pass
    # print(temperatures)

# pandas can do this very simply

import pandas as pd

df = pd.read_csv("weather_data.csv")

# print(df.head())
#
# print(df["temp"])

print(df['temp'].mean())

