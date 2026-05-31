import pandas as pd

df = pd.read_csv("emails.csv")

print(df.columns)
print(df.head())
print(df.shape)