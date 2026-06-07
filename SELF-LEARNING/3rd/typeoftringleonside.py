#program to check the type of triangle based on its sides
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
    #check the type of triangle based on its sides
    #if all sides are equal then the triangle is an equilateral triangle
    if(a == b == c):
        print("The triangle is an equilateral triangle")
    #if any two sides are equal then the triangle is an isosceles triangle
    elif(a == b or b == c or a == c):
        print("The triangle is an isosceles triangle")
    #if all sides are different then the triangle is a scalene triangle5
    else:
        print("The triangle is a scalene triangle")
else:
    print("The triangle is not valid")