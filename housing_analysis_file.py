import pandas as pd
import matplotlib.pyplot as plt
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
average_price_per_square_foot_by_preferred_area = df.groupby("prefarea")["price"].mean()
# 7. Printing our answers and revealing insights from the data:
print(f"\nNumber of ten million dollar 3BR homes: {three_BR_homes_and_above_10M.shape[0]}")
print(f"\nNumber of Three Bedroom Homes, Furnished, and above 10M Dollars: {three_BR_homes_and_furnished_and_above_10M.shape[0]}")
print(f"\nNumber of homes above 3000 Square Feet: {homes_above_3000_sqft.shape[0]}")
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

# New header:
print("\nTen Million Dollar Plus Home and 3 Bedrooms:")
print(three_BR_homes_and_above_10M.head())

# Saving the file:
df.to_csv('cleaned_Housing.csv', index=False)

## Plotting the results
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


