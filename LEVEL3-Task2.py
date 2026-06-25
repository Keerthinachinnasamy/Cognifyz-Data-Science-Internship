import pandas as pd

data = pd.read_csv("Dataset .csv")

print("Top Cuisines by Count:")
print(data["Cuisines"].value_counts().head(10))

print("\nAverage Rating by Cuisine:")
print(data.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False).head(10))

print("\nMost Voted Cuisines:")
print(data.groupby("Cuisines")["Votes"].sum().sort_values(ascending=False).head(10))
