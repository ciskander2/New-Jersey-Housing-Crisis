import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.ticker as ticker

# 1. Read the csv
df = pd.read_csv('Housing.csv')

# 2. Basic Information:
print(f"Shape (rows, columns) {df.shape}")
print("\nColumn info:")
print(df.info())
print("\nMissing values per column:")
print(df.isna().sum())
print("\nFirst 5 Rows:")
print(df.head())

# 3. Data Cleaning for the File:
df = df.dropna()

# 4. Filtering the Data for what we need:
three_BR_homes_and_above_10M = df[(df["bedrooms"] == 3) & (df["price"] > 10000000)]
three_BR_homes_and_furnished_and_above_10M = df[(df["bedrooms"] == 3) & (df["furnishingstatus"] == "furnished") & (df["price"] > 10000000)]
homes_above_3000_sqft = df["area"] > 3000
df["Price per Square Foot"] = df["price"] / df["area"]
price_per_square_foot = df["Price per Square Foot"]

# 5. Statistics for the homes
standard_deviation_between_homes = df["price"].std()
median_home = df["price"].median()
average_home = df["price"].mean()

#6. Group by for statistics
average_price_per_bedroom = df.groupby("bedrooms")["price"].mean()
median_price_per_bedroom = df.groupby("bedrooms")["price"].median()
median_price_per_furnishing_status = df.groupby("furnishingstatus")["price"].median()
main_road_average = df.groupby("mainroad")["price"].mean()
average_price_per_square_foot_by_preferred_area = df.groupby("prefarea")["price"].mean()

# 7. Printing our answers and revealing insights from the data:
print(f"\nNumber of ten million dollar 3BR homes: {three_BR_homes_and_above_10M.sum()}")
print(f"\nNumber of Three Bedroom Homes, Furnished, and above 10M Dollars: {three_BR_homes_and_furnished_and_above_10M.sum()}")
print(f"\nNumber of homes above 3000 Square Feet: {homes_above_3000_sqft.sum()}")
print("\nPrice per square foot (first 10 homes):")
print(price_per_square_foot.head(10).round(2).to_string(index=False))
print(f"Median Home Price: ${median_home:,.2f}")
print(f"Average Home Price: ${average_home:,.2f}")
print(f"Standard Deviation between home price: ${standard_deviation_between_homes:,.2f}")
print("\nAverage price per bedroom:")
print(average_price_per_bedroom.round(2).to_string())
print("\nMedian price per bedroom:")
print(median_price_per_bedroom.round(2).to_string())
print("\nMedian price per furnishing status:")
print(median_price_per_furnishing_status.round(2).to_string())
print("\nAverage price per square foot by the preferred area:")
print(average_price_per_square_foot_by_preferred_area.round(2).to_string())
print("\nHomes on main roads vs non main roads:")
print(main_road_average.round(2).to_string())

# 8. New header:
print("\nTen Million Dollar Plus Home and 3 Bedrooms:")
print(three_BR_homes_and_above_10M.head())

# 9. Saving the file:
df.to_csv('cleaned_Housing.csv', index=False)

# 10. Plotting the results
plt.figure()
df["Price per Square Foot"].hist(bins=50)
plt.title("Distribution of Price per Square Foot for Building: ")
plt.ylabel("Price per square foot")
plt.xlabel("Count")
plt.tight_layout()
plt.show()
average_price_per_bedroom.plot(kind="bar", figsize=(8,5), color="skyblue")
plt.title("Average Home Price by Number of Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Average Price ($)")
plt.tight_layout()
plt.show()

# 11. Machine Learning and Linear Regression Portion
machine_learning_df = df.copy()
yes_or_no_columns = ["mainroad", "guestroom", "basement",
                     "hotwaterheating", "airconditioning",
                     "prefarea"]
quantitative_columns = ["area", "bedrooms", "bathrooms", "stories", "parking"]
for column in yes_or_no_columns:
    machine_learning_df[column] = machine_learning_df[column].astype(str).str.strip().str.lower().map({"yes": 1, "no": 0})
machine_learning_df = pd.get_dummies(machine_learning_df, columns = ["furnishingstatus"], drop_first = True)
furnishing_columns = [c for c in machine_learning_df.columns if c.startswith("furnishingstatus_")]
total_columns = yes_or_no_columns + quantitative_columns + furnishing_columns
x = machine_learning_df[total_columns]
y = machine_learning_df["price"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
MAE = mean_absolute_error(y_test, y_pred)
RSME = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n<Mean Absolute Error & Root Mean Squared Error:")
print(f"Mean Absolute Error: {MAE}")
print(f"Root Mean Squared Error: {RSME}")
next_10_homes = machine_learning_df[total_columns].tail(10)
next_10_homes_prediction = model.predict(next_10_homes)
print("\nPredicting Prices for the next 10 Homes:")
for i, price in enumerate(next_10_homes_prediction, start=1):
    print(f"Home {i}: ${price:,.2f}")
  
# 12. Additional Plot for the Predicted vs Actual Price
plt.figure(figsize=(6,10))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Home Prices: ")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f"${y:,.0f}"))
plt.tight_layout()
plt.show()



