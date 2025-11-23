🏠 Housing Analysis — Data Cleaning & Exploratory Insights

This project performs exploratory data analysis (EDA) on a housing dataset using Python, pandas, and matplotlib.
It walks through the full lifecycle of basic data analytics: loading data, cleaning it, engineering features, filtering based on conditions, generating summary statistics, grouping categories, and visualizing results.

The goal is to understand pricing patterns in a dataset of high-end residential properties.

📂 Dataset Description

File: Housing.csv

Columns include:

price — home sale price

area — interior square footage

bedrooms, bathrooms, stories, parking

prefarea — preferred area (yes/no)

furnishingstatus — furnished / semi-furnished / unfurnished

Several binary features such as mainroad, basement, etc.

The dataset contains only luxury-tier homes, with prices ranging from approximately $1.7M to $13M.

🛠 Steps Performed
1. Load & Inspect Data

Previewed top rows with df.head()

Examined structure using df.info()

computed summary statistics using df.describe()

Checked for missing values using df.isna().sum()

2. Clean the Dataset

Removed missing rows with df.dropna()

Ensured numeric columns were cleaned and usable

Saved a cleaned version: cleaned_Housing.csv

3. Feature Engineering

Created a new derived feature:

Price per Square Foot = price / area

This metric gives a better sense of value across homes of different sizes.
4. Filtering with Boolean Logic

Used pandas boolean masks to generate subsets:

All 3-bedroom homes

3BR homes priced above $10M

3BR furnished homes above $10M

These filters demonstrate conditional selection using &, |, and parentheses.

5. Summary Statistics

Computed high-level indicators:

Median home price

Average home price

Price standard deviation

Price per square foot distribution

Count of homes above key thresholds

These statistics help reveal central tendency and market spread.

6. GroupBy Analysis

Used pandas groupby() to identify categorical trends:

Average price by number of bedrooms

Median price by number of bedrooms

Median price by furnishing status

Average price in preferred vs. non-preferred areas

Groupbys provide insight into the relationship between home characteristics and price.

7. Visualization

Generated a histogram to show the distribution of Price per Square Foot:

df["Price per Square Foot"].hist(bins=50)



This helps visualize how housing value varies across the dataset.

(Optional bar charts can be added for groupby results.)

📈 Key Insights

Every home in the dataset is over $1M, with a median of ~$4.3M.

Several 3-bedroom homes exceed $10M, showing significant variance.

Furnished homes tend to cluster in higher price ranges.

Preferred areas generally command higher average prices.

Price per square foot varies widely, revealing differences in property quality and location.

🧪 How to Run

Install dependencies:


pip install pandas matplotlib


Run the script:
python housing_analysis_file.py


📁 Project Structure


nj-housing-analysis/
│
├── Housing.csv                 # Raw dataset
├── cleaned_Housing.csv         # Cleaned dataset
├── housing_analysis_file.py    # Main analysis script
└── README.md                   # Documentation
