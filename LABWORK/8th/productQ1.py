'''
----------------------------------------------------
Problem Statement: Online Shopping Order Analytics

Scenario
An e-commerce company stores product sales data as:

sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

Tasks
• Display products sold more than 20 times.
• Find the best-selling product.
• Find the least-selling product.
• Calculate total products sold.
• Create a list of products requiring promotion (sales < 15).
• Count products having sales between 10 and 30.
----------------------------------------------------
'''
#creating a disconary 
#-----------------------------------------------------------------------
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}
# --------------------------------------------------
# display products sold more than 20 times
print("Products Sold More Than 20 Times :")

dict_items = list(sales.items())

counter = 0

for item in dict_items:

    if item[1] > 20:
        print(item[0])
    else:
        pass

    counter += 1

#---------------------------------------------------
# Find the best-selling product

dict_items = list(sales.items())

product_best = dict_items[0][0]
best_sales = dict_items[0][1]

for i in dict_items:
    if i[1] > best_sales:
        product_best = i[0]
        best_sales = i[1]

print("Best Selling Product :", product_best, "---", best_sales)
# Find the least-selling product

least_product = dict_items[0][0]
least_sales = dict_items[0][1]

for item in dict_items:
    if item[1] < least_sales:
        least_product = item[0]
        least_sales = item[1]

print("Least Selling Product :", least_product, "---", least_sales)

# Calculate total products sold
total_sales = 0
for value in dict_items:
    total_sales += value[1] 

print("total product sold", total_sales)

# Create a list of products requiring promotion (sales < 15).


promotion_products = []

for item in dict_items:
    if item[1] < 15:
        promotion_products.append(item[0])

print("Products Requiring Promotion :")
# Create a list of products requiring promotion

promotion_products = []

for item in dict_items:
    if item[1] < 15:
        promotion_products.append(item[0])

print("Products Requiring Promotion :")
print(promotion_products)

# Count products having sales between 10 and 30

count = 0

for item in dict_items:
    if item[1] > 10 and item[1] < 30:
        count += 1
    else:
        pass

print("Products Having Sales Between 10 and 30 :", count)