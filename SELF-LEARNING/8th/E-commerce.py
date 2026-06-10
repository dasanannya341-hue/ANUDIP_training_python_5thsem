'''E-Commerce Inventory & Sales Dashboard 
Problem Statement 
An online store wants to manage products and sales. 
Example Structure 
products = { 
    "P101": { 
        "name": "Laptop", 
        "price": 55000, 
        "stock": 12, 
        "sold": 25 
    } 
} 
Maintain records of at least 30 products. 
Requirements 
1. Display all products.  
2. Add a new product.  
3. Update stock after sales.  
4. Find out-of-stock products.  
5. Find products with stock less than 5.  
6. Calculate total inventory value.  
7. Find best-selling product.  
8. Find least-selling product.  
9. Calculate total revenue generated.  
10. Generate a low-stock report.  
11. Display products whose sales exceed the average sales.  
12. Create a dictionary of products eligible for promotion (sales < 10).  
Challenge 
Generate a complete business report.'''


products = {
    "P101": {"name":"Laptop","price":55000,"stock":12,"sold":25},
    "P102": {"name":"Mouse","price":800,"stock":20,"sold":40},
    "P103": {"name":"Keyboard","price":1800,"stock":4,"sold":15},
    "P104": {"name":"Monitor","price":12000,"stock":8,"sold":12},
    "P105": {"name":"Printer","price":9000,"stock":0,"sold":8},
    "P106": {"name":"Tablet","price":28000,"stock":6,"sold":18},
    "P107": {"name":"Speaker","price":3500,"stock":3,"sold":7},
    "P108": {"name":"Webcam","price":2500,"stock":10,"sold":9},
    "P109": {"name":"Headphones","price":4200,"stock":2,"sold":22},
    "P110": {"name":"Router","price":3200,"stock":15,"sold":5}
}

dict_items = list(products.items())

# Display all products
print("All Products :")

for item in dict_items:
    print(item[0], item[1])

# --------------------------------------------------

# Add new product
products["P111"] = {
    "name":"SSD",
    "price":5000,
    "stock":7,
    "sold":11
}

# --------------------------------------------------

# Update stock after sale
products["P101"]["stock"] -= 2

# --------------------------------------------------

# Out of stock products

print("\nOut Of Stock Products :")

for item in dict_items:
    if item[1]["stock"] == 0:
        print(item[1]["name"])

# --------------------------------------------------

# Stock less than 5

print("\nProducts With Stock Less Than 5 :")

for item in dict_items:
    if item[1]["stock"] < 5:
        print(item[1]["name"])

# --------------------------------------------------

# Total inventory value

inventory_value = 0

for item in dict_items:
    inventory_value += item[1]["price"] * item[1]["stock"]

print("\nTotal Inventory Value :", inventory_value)

# --------------------------------------------------

# Best Selling Product

best_product = dict_items[0][1]["name"]
best_sales = dict_items[0][1]["sold"]

for item in dict_items:

    if item[1]["sold"] > best_sales:
        best_sales = item[1]["sold"]
        best_product = item[1]["name"]

print("\nBest Selling Product :", best_product)

# --------------------------------------------------

# Least Selling Product

least_product = dict_items[0][1]["name"]
least_sales = dict_items[0][1]["sold"]

for item in dict_items:

    if item[1]["sold"] < least_sales:
        least_sales = item[1]["sold"]
        least_product = item[1]["name"]

print("\nLeast Selling Product :", least_product)

# --------------------------------------------------

# Total Revenue

revenue = 0

for item in dict_items:
    revenue += item[1]["price"] * item[1]["sold"]

print("\nTotal Revenue :", revenue)

# --------------------------------------------------

# Low Stock Report

low_stock = []

for item in dict_items:

    if item[1]["stock"] < 5:
        low_stock.append(item[1]["name"])

print("\nLow Stock Report :")
print(low_stock)

# --------------------------------------------------

# Average Sales

total_sales = 0

for item in dict_items:
    total_sales += item[1]["sold"]

average_sales = total_sales / len(dict_items)

print("\nAverage Sales :", average_sales)

# Products Above Average Sales

print("\nProducts Above Average Sales :")

for item in dict_items:

    if item[1]["sold"] > average_sales:
        print(item[1]["name"])

# --------------------------------------------------

# Promotion Products

promotion = {}

for item in dict_items:

    if item[1]["sold"] < 10:
        promotion[item[0]] = item[1]

print("\nPromotion Products :")
print(promotion)

# --------------------------------------------------

# Business Report

print("\n----- BUSINESS REPORT -----")

print("Total Inventory Value :", inventory_value)
print("Total Revenue :", revenue)
print("Best Selling Product :", best_product)
print("Least Selling Product :", least_product)
print("Average Sales :", average_sales)
print("Low Stock Products :", low_stock)
print("Products For Promotion :", len(promotion))