#A Mountain Number is a number whose digits first increase and then decrease.
number = input("Enter a number: ")
is_mountain = True
increasing = True
for i in range(1, len(number)):
    if increasing:
        if number[i] > number[i - 1]:
            continue
        elif number[i] < number[i - 1]:
            increasing = False
        else:
            is_mountain = False
            break
    else:
        if number[i] < number[i - 1]:
            continue
        else:
            is_mountain = False
            break

if is_mountain:
    print("The number is a mountain number.")
else:
    print("The number is not a mountain number.")