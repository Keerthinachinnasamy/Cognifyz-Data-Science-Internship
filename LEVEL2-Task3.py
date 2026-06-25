import pandas as pd

df = pd.read_csv("Dataset .csv")

df["Restaurant_Name_Length"] = (
    df["Restaurant Name"].str.len())

df["Address_Length"] = (
    df["Address"].str.len())

df["Has_Table_Booking"] = (
    df["Has Table booking"].map({"Yes": 1, "No": 0}))

df["Has_Online_Delivery"] = (
    df["Has Online delivery"].map({"Yes": 1, "No": 0}))

print("New Features Created Successfully!\n")

print(df[
    [
        "Restaurant Name",
        "Restaurant_Name_Length",
        "Address_Length",
        "Has_Table_Booking",
        "Has_Online_Delivery"
    ]
].head())
