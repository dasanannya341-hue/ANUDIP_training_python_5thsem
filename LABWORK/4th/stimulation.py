#Accept a number from the user and check whether it is an Armstrong Number.
num = int(input("Enter a number: "))
#validating the number
if num < 0:
    print("Negative numbers cannot be Armstrong numbers.")
else:
    #calculating the number of digits in the number
    num_digits = len(str(num))
    armstrong_sum = 0
    temp = num
    #calculating the sum of the digits raised to the power of the number of digits
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_digits
        temp //= 10
    #checking if the calculated sum is equal to the original number
    if armstrong_sum == num:
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")