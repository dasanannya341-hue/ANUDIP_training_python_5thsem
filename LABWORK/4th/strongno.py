#A Strong Number is a number whose sum of factorials of digits equals the number itself. Write a program to check whether a given number is a Strong Number. 
num = int(input("Enter a number: "))
#validating the number
if num < 0:
    print("Enter positive numbers.")
else:
    temp = num
    strong_sum = 0
    #calculating the sum of factorials of digits
    while temp > 0:
        digit = temp % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        strong_sum += factorial
        temp //= 10
    #checking if the calculated sum is equal to the original number
    if strong_sum == num:
        print(num, "is a Strong Number.")
    else:
        print(num, "is not a Strong Number.")