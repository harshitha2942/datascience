import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv(r"C:\Users\joshi\Downloads\matrix.csv")

# Get product names
products = data["Product"]

# Convert sales values to NumPy array
sales = data.iloc[:, 1:].to_numpy()

# Calculate average price for each product
average_prices = np.mean(sales, axis=1)

# Calculate overall average price
overall_average = np.mean(sales)

# Display results
print("Average Price of Each Product\n")

for product, avg in zip(products, average_prices):
    print(product, ":", round(avg, 2))

print("\nOverall Average Price of All Products Sold:", round(overall_average, 2))

# Save output to CSV
result = pd.DataFrame({
    "Product": products,
    "Average Price": average_prices
})

result.loc[len(result)] = ["Overall Average", round(overall_average, 2)]

result.to_csv("average_product_prices.csv", index=False)

print("\nOutput saved as average_product_prices.csv")

# Plot graph
plt.figure(figsize=(7,5))
plt.bar(products, average_prices)

plt.title("Average Price of Products")
plt.xlabel("Products")
plt.ylabel("Average Price")

for i, value in enumerate(average_prices):
    plt.text(i, value + 300, f"{value:.2f}", ha='center')

plt.grid(axis='y')
plt.show()
