# CodeAlpha Task 2 : Exploratory Data Analysis using Python
# Dataset Used
Name: Online Store Orders Dataset
File: Online.Store.Orders.csv
Source: Kaggle
# Objective
To perform Exploratory Data Analysis on E-commerce order data to extract meaningful business insights using python.
# Tech Stack
Python, Pandas, Numpy, Matplotlib, Seaborn
# Work Done
1. **Data Loading & Initial exploration:**
Used.head(),.shape,.info(),.discribe() to understand data.
2. **Data Cleaning**
  -Converted 'Date' column to datetime format.
  -Handled missing values in 'CouponCode' column using 'No Coupon'
  -Checked and Analyzed duplicate entries
3. **Data Visualization**
  -**Bar Chart** Top 5 most sold products by quantity
  -**Pie Chart** Payment method distribution Analysis
  -**Pie Chart** Order Status Distribution - completed vs cancelled vs others
  
4. **Data Export** Saved cleaned dataset as 'cleaned_data.csv' for future use
5. **Key Insights**
  1.**Product Performance** Successfully identified Top 5 most sold products helping understand customer preferences and inventory planning
  2.**Payemnt Trends**Analyzed distribution of payment methods to identify most popular payment options used by customers
  3.**Order MAnagement** Tracked Order Status distribution to measure completion rate and identify cancellation patterns
  4.**Seasonal Trends** Visualized Monthly Order Trend to identify peak sales months and seasonal patterns in customer orders
  5.**Data Quality Check** Ensured data integrity by handling null value and indentifying duplicates before analysis



