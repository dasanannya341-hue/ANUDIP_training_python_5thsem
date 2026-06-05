#A customer is adding items to a shopping cart. The price of each item is entered one by one. Write a program that continuously accepts item prices and calculates the total bill amount. The program should stop accepting prices when the user enters 0. 
item_price = 0
total_bill = 0
while True:
    item_price = float(input("Item price: "))
    if item_price == 0:
        break
    total_bill += item_price

print("Total bill amount:", total_bill)