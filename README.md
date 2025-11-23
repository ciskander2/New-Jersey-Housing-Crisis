🏠 Housing Analysis — Data Cleaning & Insights Project

📌 Overview

This project performs exploratory data analysis (EDA) on a housing dataset using Python, pandas, and matplotlib.

It demonstrates skills in:

Data loading & inspection

Cleaning & preprocessing

Feature engineering

Filtering with conditional logic

Summary statistics

Basic visualization

Saving cleaned datasets

This is a realistic data engineering / data analytics mini-project similar to what interns and junior analysts do in industry.

📂 Dataset

File: Housing.csv

Columns include:

price — home sale price

area — square footage

bedrooms, bathrooms, stories, parking

prefarea — preferred area (yes/no)

furnishingstatus — furnished / semi-furnished / unfurnished

🛠 Steps Performed

1. Load & Inspect Data
df.head() to preview the first rows

df.info() to check column types & null counts

df.describe() for summary statistics

df.isna().sum() to reveal missing values

2.  Clean the Dataset

Removed missing values with df.dropna()

Ensured all relevant columns were numeric

3. Feature Engineering
   
Created a new column:

Price per Square Foot = price / area

Filtering & Boolean Logic

Examples:

All 3-bedroom homes

3BR homes priced above $1,000,000

Furnished 3BR homes above $1M

This uses pandas boolean masks with &, |, and parentheses.

4. Summary Statistics
   
Generated insights such as:

Total # of million-dollar 3BR homes

Median home price

Distribution of price per square foot

5. Visualization
   
Produced a histogram of Price per Square Foot:

df["Price per Square Foot"].hist(bins=6)

6. Saved Cleaned Dataset
    
Exported a cleaned version for reuse:

cleaned_Housing.csv

📈 Key Findings

The dataset contains several 3-bedroom homes over $1,000,000.

Furnished homes tend to appear more frequently in the luxury category.

Median home price is reasonable compared to high-end outliers.

Price per square foot varies significantly, indicating a broad diversity in housing quality and area.

🧪 How to Run

Install dependencies:

pip install pandas matplotlib

Run the project:

python nj_housing_crisis_and_analysis.py

📁 Project Structure

nj-housing-analysis/


│
├── Housing.csv                 # raw dataset

├── cleaned_Housing.csv         # cleaned version

├── nj_housing_crisis_and_analysis.py

└── README.md
