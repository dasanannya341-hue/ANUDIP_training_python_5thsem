# Input 6-digit secret code
code = input("Enter 6-digit code: ")

# Check length
if len(code) == 6:
    # Sum of first 3 digits
    first_sum = int(code[0]) + int(code[1]) + int(code[2])

    # Sum of last 3 digits
    last_sum = int(code[3]) + int(code[4]) + int(code[5])

    # Compare sums
    if first_sum == last_sum:
        print("Valid Code")
    else:
        print("Invalid Code")
else:
    print("Invalid Code")