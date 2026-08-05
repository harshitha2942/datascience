import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from CSV
data = pd.read_csv(r"C:\Users\joshi\Downloads\bedrooms.csv")

# Convert required columns to NumPy array
house_data = data.to_numpy()

# Get houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price
average_price = np.mean(filtered_houses[:, 2])

print("Average Sale Price of Houses with More Than 4 Bedrooms:")
print(round(average_price, 2))

# Save output to CSV
result = pd.DataFrame({
    "Description": ["Average Sale Price (Bedrooms > 4)"],
    "Average Sale Price": [round(average_price, 2)]
})

result.to_csv("house_average_sale_price.csv", index=False)

print("\nOutput saved as house_average_sale_price.csv")

# Graph
plt.figure(figsize=(6,5))
plt.bar(["Bedrooms > 4"], [average_price])

plt.title("Average Sale Price")
plt.ylabel("Sale Price")

plt.text(0, average_price + 10000, round(average_price, 2), ha='center')

plt.grid(axis='y')
plt.show()
