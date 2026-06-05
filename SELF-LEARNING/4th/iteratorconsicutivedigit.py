#Accept a number and check whether every digit is exactly 1 greater than its previous digit.
number = input("Enter a number: ")
is_consecutive = True

for i in range(len(number) - 1):
    if int(number[i]) + 1 != int(number[i + 1]):
        is_consecutive = False
        break

if is_consecutive:
    print("The digits are consecutive.")
else:
    print("The digits are not consecutive.")