#Calculate electricity bill based on the following slab rates: Units Rate 0-100 ₹5/unit 101-200 ₹7/unit Above 200 ₹10/unit Display: • Units Consumed  • Total Bill  • Category (Low / Medium / High Consumption)  
units = int(input("Enter the number of units consumed: "))
#validating the input
if units < 0:
    print("Units cannot be negative.")
else:
    #calculating the units
    if units <= 100:
        bill = units * 5
        category = "Low Consumption"
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
        category = "Medium Consumption"
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
        category = "High Consumption"
    
    print("Units Consumed:", units)
    print("Total Bill: ₹", bill)
    print("Category:", category)
    