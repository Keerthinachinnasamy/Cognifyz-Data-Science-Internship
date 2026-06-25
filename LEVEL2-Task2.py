import pandas as pd

df = pd.read_csv("Dataset .csv")

print("Most Common Price Range:")
print(df["Price range"].mode()[0])

print("\nAverage Rating by Price Range:")
avg_rating = df.groupby("Price range")["Aggregate rating"].mean()
print(avg_rating)

color_rating = df.groupby("Rating color")["Aggregate rating"].mean()

print("\nHighest Rated Color:")
print(color_rating.idxmax())

print("\nAverage Ratings by Color:")
print(color_rating)
