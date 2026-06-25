import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv("Dataset .csv")

features = [
    "Average Cost for two",
    "Votes",
    "Price range",
    "Has Table booking",
    "Has Online delivery"
]

df = data[features + ["Aggregate rating"]]

df["Has Table booking"] = df["Has Table booking"].map({"Yes": 1, "No": 0})
df["Has Online delivery"] = df["Has Online delivery"].map({"Yes": 1, "No": 0})

df = df.dropna()

X = df[features]
y = df["Aggregate rating"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("\nModel:", name)
    print("MAE:", mean_absolute_error(y_test, predictions))
    print("RMSE:", mean_squared_error(y_test, predictions) ** 0.5)
    print("R2 Score:", r2_score(y_test, predictions))
