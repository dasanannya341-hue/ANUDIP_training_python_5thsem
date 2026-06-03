#calculate intrest 
#input principal amount, rate of intrest and time in years
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of intrest: "))
time = float(input("Enter the time in years: "))
#calculate simple intrest
simple_intrest = (principal * rate * time) / 100
#calculate compound intrest
compound_intrest = principal * (1 + rate / 100) ** time - principal
print("The simple intrest is:", simple_intrest)
print("The compound intrest is:", compound_intrest)
principal = principal + compound_intrest    
print("The new principal amount is:", principal)