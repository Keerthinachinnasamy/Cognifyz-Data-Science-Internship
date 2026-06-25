import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset .csv")

plt.figure(figsize=(10, 6))
plt.scatter(
    df["Longitude"],
    df["Latitude"],
    alpha=0.5
)

plt.title("Restaurant Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

city_counts = df["City"].value_counts().head(10)

plt.figure(figsize=(10, 6))
city_counts.plot(kind="bar")

plt.title("Top 10 Cities by Restaurant Count")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.show()

print("\nCorrelation Matrix:")
print(
    df[
        ["Latitude",
         "Longitude",
         "Aggregate rating"]
    ].corr()
)
