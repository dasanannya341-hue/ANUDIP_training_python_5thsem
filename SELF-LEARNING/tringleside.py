#write a program to check whether the triangle is valid or not in side 
a = int(input("Enter the first side: "))
if(a <= 0):
    exit("Side cannot be negative or zero")
#------------------------------------------------------
b = int(input("Enter the second side: "))
if(b <= 0):
    exit("Side cannot be negative or zero")
#------------------------------------------------------
c = int(input("Enter the third side: "))
if(c <= 0):
    exit("Side cannot be negative or zero")
#check whether the sum of any two sides is greater than the third side or not
#if the sum of any two sides is greater than the third side then the triangle is valid otherwise it is not valid
if(a + b > c and a + c > b and b + c > a):
    print("The triangle is valid")
else:
    print("The triangle is not valid")