# Input number
num = input("Enter number: ")

# Find middle position
mid = len(num) // 2

# Compare left and right halves
if num[:mid] == num[mid:]:
    print("Mirror Number")
else:
    print("Not a Mirror Number")