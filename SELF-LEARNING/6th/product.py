'''6. Product Price Analysis 
Sample Data 
prices = { 
    "Laptop": 55000, 
    "Mouse": 800, 
    "Keyboard": 1800, 
    "Monitor": 12000, 
    "Printer": 9000, 
    "Tablet": 28000, 
    "Speaker": 3500, 
    "Webcam": 2500, 
    "Headphones": 4200, 
    "Router": 3200 
} 
Tasks 
• Display products costing more than ₹5000.  
• Count products costing less than ₹3000.  
• Find the most expensive product.  
• Create a list of products priced between ₹2000 and ₹10000.  
• Calculate the total value of all products.'''

prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# Display products costing more than 5000
print("Products Costing More Than ₹5000:")
for product in prices:
    if prices[product] > 5000:
        print(product)

# Count products costing less than 3000
count = 0

for product in prices:
    if prices[product] < 3000:
        count += 1

print("\nProducts Costing Less Than ₹3000:", count)

# Find the most expensive product
highest_price = 0
expensive_product = ""

for product in prices:
    if prices[product] > highest_price:
        highest_price = prices[product]
        expensive_product = product

print("\nMost Expensive Product:")
print(expensive_product, "(", highest_price, ")", sep="")

# Create list of products priced between 2000 and 10000
product_list = []

for product in prices:
    if 2000 <= prices[product] <= 10000:
        product_list.append(product)

print("\nProducts Priced Between ₹2000 and ₹10000:")
print(product_list)

# Calculate total value of all products
total = 0

for product in prices:
    total += prices[product]

print("\nTotal Value of All Products:", total)