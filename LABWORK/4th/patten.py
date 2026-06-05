#Accept the number of rows and print the following pattern: For Input: 5 Output: 1 12 123 1234 12345 Challenge: Print the reverse pattern as well. 
rows = int(input("Enter the number of rows: "))
# Printing the pattern
print("Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# Printing the reverse pattern
print("Reverse Pattern:")
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    