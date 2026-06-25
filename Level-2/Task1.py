import pandas as pd

df = pd.read_csv("Dataset .csv")

table_booking = (df["Has Table booking"] == "Yes").sum()
table_booking_percent = (table_booking / len(df)) * 100

print("Percentage of Restaurants with Table Booking:")
print(round(table_booking_percent, 2), "%")

online_delivery = (df["Has Online delivery"] == "Yes").sum()
online_delivery_percent = (online_delivery / len(df)) * 100

print("\nPercentage of Restaurants with Online Delivery:")
print(round(online_delivery_percent, 2), "%")

print("\nAverage Ratings based on Table Booking:")
print(df.groupby("Has Table booking")["Aggregate rating"].mean())

print("\nOnline Delivery by Price Range:")
print(pd.crosstab(df["Price range"],df["Has Online delivery"]))
