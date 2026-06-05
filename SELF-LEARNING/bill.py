# Input total electricity units consumed
units = int(input("Enter electricity units consumed: "))

# Variable to store the bill amount
bill = 0

# Calculate bill according to slabs
if units <= 100:
    # First 100 units charged at ₹5 per unit
    bill = units * 5

elif units <= 200:
    # First 100 units at ₹5/unit
    # Remaining units at ₹7/unit
    bill = (100 * 5) + ((units - 100) * 7)

else:
    # First 100 units at ₹5/unit
    # Next 100 units at ₹7/unit
    # Remaining units above 200 at ₹10/unit
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Check if surcharge is applicable
if bill > 5000:
    # Calculate 10% surcharge
    surcharge = bill * 0.10

    # Add surcharge to the bill
    bill += surcharge

    # Display surcharge amount
    print("Surcharge Applied: ₹", surcharge)

# Display final payable amount
print("Final Payable Amount: ₹", bill)