'''3. Employee Salary Processing 
Sample Data 
salary = { 
    "EMP101": 45000, 
    "EMP102": 62000, 
    "EMP103": 38000, 
    "EMP104": 75000, 
    "EMP105": 54000, 
    "EMP106": 29000, 
    "EMP107": 82000, 
    "EMP108": 48000, 
    "EMP109": 36000, 
    "EMP110": 68000 
} 
Tasks 
• Display employees earning above ₹60,000.  
• Count employees earning below ₹40,000.  
• Find the highest-paid employee.  
• Create a list of employees eligible for a bonus (salary > ₹50,000).  
• Calculate the average salary.  '''


# Inventory Management System

inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Display products with stock less than 10
print("Products with stock less than 10:")
for product in inventory:
    if inventory[product] < 10:
        print(product, ":", inventory[product])

# Count products having stock more than 50
count = 0
for product in inventory:
    if inventory[product] > 50:
        count += 1

print("\nProducts with stock more than 50 =", count)

# Find the product with minimum stock
min_product = ""
min_stock = None

for product in inventory:
    if min_stock == None or inventory[product] < min_stock:
        min_stock = inventory[product]
        min_product = product

print("\nProduct with minimum stock:")
print(min_product, ":", min_stock)

# Create a list of products requiring restocking
restocking = []

for product in inventory:
    if inventory[product] < 20:
        restocking.append(product)

print("\nProducts requiring restocking:")
print(restocking)

# Calculate total inventory count
total = 0

for product in inventory:
    total += inventory[product]

print("\nTotal Inventory Count =", total)