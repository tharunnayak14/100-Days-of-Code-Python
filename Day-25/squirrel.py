import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(df.head())

print(df.columns)

new_df = df.groupby("Primary Fur Color").count()["X"]

print(new_df)