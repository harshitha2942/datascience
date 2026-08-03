import pandas as pd
import matplotlib.pyplot as plt

# Enter CSV file path
file_path = input("Enter the CSV file path: ")

# Read CSV file
order_data = pd.read_csv(file_path)

# Convert Order_Date into datetime
order_data["Order_Date"] = pd.to_datetime(order_data["Order_Date"])

print("\nCustomer Orders Data")
print(order_data)

# 1. Total number of orders made by each customer
orders = order_data.groupby("Customer_ID").size()

print("\nTotal Orders by Each Customer")
print(orders)

# 2. Average order quantity for each product
avg_quantity = order_data.groupby("Product_Name")["Order_Quantity"].mean()

print("\nAverage Order Quantity for Each Product")
print(avg_quantity)

# 3. Earliest and Latest Order Dates
print("\nEarliest Order Date:", order_data["Order_Date"].min())
print("Latest Order Date:", order_data["Order_Date"].max())

# -------- Graph --------
plt.figure(figsize=(6,4))
orders.plot(kind="bar", color="skyblue")

plt.title("Total Orders by Customer")
plt.xlabel("Customer ID")
plt.ylabel("Number of Orders")
plt.grid(axis="y")

plt.show()
