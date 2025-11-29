🏡 Housing Prices Analysis in Pandas

This project performs a full exploratory data analysis (EDA) on a dataset of luxury residential properties.

The goal is to identify the strongest drivers of home prices, uncover hidden patterns, and build a foundation for future machine-learning models.

📌 Overview

This project analyzes a dataset of residential properties to understand the key factors that influence home prices.

Using pandas, NumPy, and matplotlib, it walks through a full end-to-end exploratory workflow:

📂 Project Structure

├── data/
│   ├── raw_data.csv
│   ├── cleaned_data.csv
├── Housing_Prices_Analysis.ipynb
└── README.md

1. Data Cleaning 🧼

Steps included:

Handling missing values

Removing unrealistic or extreme outliers

Converting numeric columns (e.g., price, square footage)

Standardizing categorical values

Creating new features such as price per square foot

✔️ After cleaning, the dataset is ready for analysis and modeling.

✔️ The cleaned CSV is exported for reproducibility.

2. Exploratory Data Analysis (EDA): 📊 

Key Questions Explored:

How are home prices distributed?

Do larger homes always cost more?

What neighborhoods command the highest premiums?

How does number of bedrooms/bathrooms affect price?

Which features show the strongest correlation with price?

Methods Used

Distribution plots

Correlation matrices

Scatter plots

Group-by aggregations

Price per square foot comparisons

3. Key Insights 💡 

📈 Insight 1: Size is the strongest driver of price

Price shows clear positive correlation with square footage, especially above the luxury threshold.

🌍 Insight 2: Location remains a major premium factor

Homes in certain neighborhoods consistently show 20–40% higher price per square foot.

🛏️ Insight 3: Bedroom count matters — but only up to a point

After 4–5 bedrooms, marginal price increase flattens.

💰 Insight 4: Price per square foot (PPSF) varies heavily

Some high-priced homes have lower PPSF, suggesting:

larger lot size

older construction

outdated interiors

rural vs. urban location differences

🏷️ Insight 5: Luxury features → higher valuation

Homes with renovated kitchens, modern finishes, or premium architecture tend to cluster at the high-end of the distribution.

4. Summary Statistics 🧮 

Examples of statistics computed:

Mean, median, and distribution of home prices

Minimum and maximum values

Correlations between features

Group-by statistics by neighborhood or property type

These stats form the foundation for the visual exploration and insights above.

5. Future Predictions and Machine Learning Tools 🤖

Trained a skikit-learn model to predict the price of the next 10 homes

Calculated the Mean Absolute Error and Root Mean Squared Errror using scikit-learn and Numpy

6. Future Improvements (Planned Enhancements) 🚀

📍 Add Geospatial Analysis

Use city/zip code location data to analyze neighborhood-level trends.

📈 Add Data Engineering features

File i/o with PySpark instead of pandas, try to filter with data using SQL instead of pandas, using Airflow, etc. 

📝 Enhance Documentation

Include:

More visualizations

Screenshots of charts

A full “Insights Summary” section

7. Tech Stack 🛠️

Python 3.10+

pandas

numpy

matplotlib / seaborn

scikit-learn

8. How to Run the Project ▶️

Clone the repository

git clone https://github.com/ciskander2/Housing-Prices-Analysis-in-Pandas.git

Install dependencies

pip install -r requirements.txt

Open the notebook

jupyter notebook Housing_Prices_Analysis.ipynb

Run all cells to reproduce the full analysis.

9. Project Archtecture and Diagram 🏗️
    
       ┌─────────────┐
       │  Raw CSV     │
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │ Cleaning     │
       └──────┬──────┘
              │
       ┌──────▼────────────┐
       │ Feature Engineering│
       └──────┬────────────┘
              │
       ┌──────▼──────┐
       │ EDA + Plots │
       └──────┬──────┘
              │
       ┌──────▼────────┐
       │ ML Model       │
       └──────┬────────┘
              │
       ┌──────▼──────────────┐
       │ Predictions + Export │
       └──────────────────────┘


10. 🧑‍💻 Author and Contact Information

Christopher Iskander

NYU Engineering Student | Incoming Data Engineering Intern @ Moody's Corporation | Previously @ Thornton Tomasetti (Applied Science -- Software & Data Science)

📞 + 1 973-524-9266 | 📧 cmi8536@nyu.edu | 🔗 LinkedIn: christopher-iskander

Focused on data analytics, fintech, and real-world decision modeling.
