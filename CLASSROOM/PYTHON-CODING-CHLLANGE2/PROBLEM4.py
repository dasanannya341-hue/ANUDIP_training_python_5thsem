'''Problem 4: Online Shopping Inventory System 
Problem Statement 
An online store maintains stock quantities of products. 
Sample Data 
inventory = { 
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
1. Display products with stock below 15 units.  
2. Find the product with maximum stock.  
3. Find the product with minimum stock.  
4. Calculate total stock available.  
5. Create a list of products requiring restocking (<10 units).  
Sample Output 
Products with Stock Below 15: 
Monitor 
Printer 
Tablet 
 
Highest Stock Product: 
Mouse (45 units) 
 
Lowest Stock Product: 
Printer (8 units) 
 
Total Stock Available: 213 
 
Products Requiring Restocking: 
['Printer']'''

inventory = { 
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
# Display products with stock below 15 units.  

