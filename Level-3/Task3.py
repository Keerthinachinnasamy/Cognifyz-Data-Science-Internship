import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Dataset .csv")

plt.figure(figsize=(6,4))
sns.histplot(data["Aggregate rating"], bins=10)
plt.title("Rating Distribution")
plt.show()

top_cities = data.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_cities.plot(kind="bar")
plt.title("Top Cities by Average Rating")
plt.ylabel("Rating")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x="Votes", y="Aggregate rating", data=data)
plt.title("Votes vs Rating")
plt.show()
