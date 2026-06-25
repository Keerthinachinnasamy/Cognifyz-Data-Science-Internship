import pandas as pd

df = pd.read_csv("Dataset .csv")

print("Statistical Summary:")
print(df.describe())

print("\nTop Countries:")
print(df["Country Code"].value_counts())

print("\nTop Cities:")
print(df["City"].value_counts().head(10))

print("\nTop Cuisines:")
print(df["Cuisines"].value_counts().head(10))
