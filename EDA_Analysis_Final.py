import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Loading CSV file 
df=pd.read_csv('Online-Store-Orders.csv')
# Understanding data
# Total rows
print("Total rows",len(df))
# Checking datatype
print(df.info())
print(df.describe())
# Converting date column to datetime
df['Date']=pd.to_datetime(df['Date'])
# Null values
print("empty values in each column",df.isnull().sum())
# Filling null couponcode values
df['CouponCode']=df['CouponCode'].fillna('No Coupon',inplace=True)
# Duplicate values
duplicates=df.duplicated().sum()
print(f"/nDuplicated rows: {duplicates}")
print("/n Checking after cleaning data")
print("checking Null Values: ",df.isnull().sum())
print("Final Shape: ",df.shape)
print("Checking Data Types: ",df.dtypes)
# CHART 1 Top 5 most sold products
plt.figure(figsize=(10,6)) # Chart size
top_products=df['Product'].value_counts().head(5) # Top 5 Products
sns.barplot(x=top_products.values,y=top_products.index) # BarGraph
# Title and labels
plt.title('Top 5 most sold products')
plt.xlabel('Numbers of orders')
plt.ylabel('Product Name')
plt.tight_layout()
# Showing Graph
plt.show()

#CHART 2 Payment Method Distribution
plt.figure(figsize=(8,8)) # Chart size
payment_count=df['PaymentMethod'].value_counts() # Count Payment method
plt.pie(payment_count.values,labels=payment_count.index,autopct='1%.1f%%') # PieChart
# Title 
plt.title('Payment Method Distribution')
# Showing Graph
plt.show()

# CHART 3 Order Status Distribution
plt.figure(figsize=(10,6))
status_count=df['OrderStatus'].value_counts()
sns.barplot(x=status_count.index,y=status_count.values)
plt.title('Order Status Distribution')
plt.xlabel('Status')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.show()
df.to_csv('cleaned_data.csv',index=False)

#Chart 4 Monthly order Trend
df['Month']=df['Date'].dt.to_period('M')
monthly_orders=df.groupby('Month').size()
plt.figure(figsize=(12,6))
monthly_orders.plot(kind='line',marker='o')
plt.title('Monthly order Trend')
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
