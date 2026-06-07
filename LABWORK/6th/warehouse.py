''' Warehouse Product Inspection 
Problem Statement 
Product IDs and quality status: 
products = [ 
    (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"), 
    (105, "Pass") 
] 
Write a program to: 
• Display failed product IDs.  
• Count passed and failed products.  
• Calculate pass percentage.  
• Stop checking if 3 failures are found. '''

products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0

# Display failed product IDs
print("Failed Product IDs:")
for item in products:
    if item[1] == "Fail":
        fail_count += 1
        print(item[0])

        # Stop checking if 3 failures are found
        if fail_count == 3:
            print("3 failures found. Stopping check.")
            break
    else:
        pass_count += 1

# Count passed and failed products
print("\nPassed Products =", pass_count)
print("Failed Products =", fail_count)

# Calculate pass percentage
percentage = (pass_count / (pass_count + fail_count)) * 100
print("Pass Percentage =", percentage, "%")