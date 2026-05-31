import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Loading CSV file 
df=pd.read_csv('Online-Store-Orders.csv')
# Total rows
print("Total rows",len(df))
# Null values
print("empty values in each column",df.isnull().sum())
duplicates=df.duplicated().sum()
# Duplicate values
print(f"\nDuplicated rows: {duplicates}")
# Checking datatype
print("/n Raw Data")
print(df.info())
# Converting date (str) to datetime
df['Date']=pd.to_datetime(df['Date'])
# Fix null values
df['CouponCode']=df['CouponCode'].fillna('No Coupon',inplace=True)
print("/n Clean Data")
print(df.info())

# CHART 1
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

#CHART 2
plt.figure(figsize=(8,8)) # Chart size
payment_count=df['PaymentMethod'].value_counts() # Count Payment method
plt.pie(payment_count.values,labels=payment_count.index,autopct='1%.1f%%') # PieChart
# Title 
plt.title('Payment Method Distribution')
# Showing Graph
plt.show()

# CHART 3
plt.figure(figsize=(10,6))
status_count=df['OrderStatus'].value_counts()
sns.barplot(x=status_count.index,y=status_count.values)
plt.title('Order Status Distribution')
plt.xlabel('Status')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.show()
df.to_csv('cleaned_data.csv',index=False)