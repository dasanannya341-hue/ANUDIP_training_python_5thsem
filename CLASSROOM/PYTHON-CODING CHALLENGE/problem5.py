'''Problem 5: Online Shopping Cart Analyzer 
Problem Statement 
The prices of products added to a shopping cart are stored below. 
Sample Data 
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000).  
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price.  
Sample Output 
Total Cart Value: ₹11,097 
 
Most Expensive Product: ₹2,500 
 
Cheapest Product: ₹300 
 
Premium Shipping Eligible Products: 4 
 
Discount Eligible Products: 
[2500, 1800] 
 
Average Product Price: ₹1,109.7 '''

cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 

#1. Calculate the total cart value.  
cart1 = sum(cart)
print( "total cart value ",cart1) 

#Find the most expensive and cheapest products.  
most_expensive = max(cart)
print( "most expensive item" ,most_expensive)

least_expensive = min(cart)
print("least expensive item " ,least_expensive)

#3. Count products eligible for premium shipping (price > ₹1000).  
count_product=0
for item in cart:
    if item >1000:
        count_product +=1

print("count product eligible for premium shipping (price > ₹1000) ",count_product )

# 4. Generate a discount list (products above ₹1500)

discount_list = []

for item in cart:
    if item > 1500:
        discount_list.append(item)

print("Discount List:", discount_list)

# Calculate the average product price.  
if len(cart) > 0:
    total = sum(cart)
    average = total / len(cart)
    print(f"Average Product Price: ₹{average:.1f}")
else:
    print("No products available to calculate average.")