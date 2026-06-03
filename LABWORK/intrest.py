#calculate intrest 
#input principal amount, rate of intrest and time in years
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of intrest: "))
time = int(input("Enter the time in years: "))
#calculate simple intrest
if principal > 0 and rate >=0 and time >=0:
    simple_intrest = (principal * rate * time) / 100
    print("The simple intrest is:", simple_intrest)
else:
    print("Principal amount, rate of intrest and time cannot be negative")
    print("Please enter valid inputs")