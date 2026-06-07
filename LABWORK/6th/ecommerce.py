'''An online store records orders as: 
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
Write a program to: 
• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. '''
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
#--------------------------------------------------------------------------------------
# display all product costing more then 1000
print("order cost more than 1000 ")
for item in orders:
    if item[1]>1000:
        print(item[0],item[1])

#----------------------------------------------------------------------------------------
# Find the most expensive product
item_counter = orders[0]
for item in orders:
    if item[1] > item_counter[1]:
        item_counter = item
print("most expensive item =", item_counter)
#-------------------------------------------------------------------------------------------
#Calculate the total order value.
total_value=0
for item in orders:
    total_value= total_value+item[1]
print("total value=",total_value)
#--------------------------------------------------------------------------------------------
#Count products costing below ₹1000.
count_item = 0
for item in orders:
    if item[1]<1000:
       count_item=count_item + 1
print("item costing less then 1000",count_item)
        
