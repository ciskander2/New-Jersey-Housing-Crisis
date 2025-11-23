import pandas as pd
import matplotlib.pyplot as plt
# Read the csv
df = pd.read_csv('Housing.csv')
# Basic Information:
print("Shape (rows, columns): ", df.shape)
print("\nColumn info:")
print(df.info())
print("\nMissing values per column:")
print(df.isna().sum())
print("\nFirst 5 Rows:")
print(df.head())
# Data Cleaning for the File:
df = df.dropna()
# Filtering the Data for what we need:
three_BR_Homes = df[df["bedrooms"] == 3] #
ten_million_plus = three_BR_Homes[three_BR_Homes['price'] > 10000000]
median_home = df["price"].median() # Finding median home
df["Price per Square Foot"] = df["price"] / df["area"]
price_per_square_foot = df["Price per Square Foot"]
three_BR_homes_and_furnished_and_above_1M = df[(df["bedrooms"] == 3) & (df["furnishingstatus"] == "furnished") & (df["price"] > 10000000)]
# Printing our answers and revealing insights from the data:
print(f"Number of ten million dollar 3BR homes: {ten_million_plus.shape[0]}")
print(f"Price per square foot: {price_per_square_foot}")
print(f"Median home price: {median_home}")
print(f"Number of Three Bedroom Homes, Furnished,and above 1M Dollars: {three_BR_homes_and_furnished_and_above_1M.shape[0]}")

# New header:
print(ten_million_plus.head())
# Saving the file:
df.to_csv('cleaned_Housing.csv', index=False)
## Plotting the results
plt.figure()
df["Price per Square Foot"].hist(bins=6)
plt.title("Distribution of Price per Square Foot for Building: ")
plt.ylabel("Price per square foot")
plt.xlabel("Count")
plt.tight_layout()
plt.show()


