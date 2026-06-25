import pandas as pd

df = pd.read_csv("Dataset .csv")

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

df["Aggregate rating"] = pd.to_numeric(
    df["Aggregate rating"],
    errors="coerce"
)

print("\nAggregate Rating Statistics:")
print(df["Aggregate rating"].describe())

print("\nRating Distribution:")
print(df["Aggregate rating"].value_counts())
