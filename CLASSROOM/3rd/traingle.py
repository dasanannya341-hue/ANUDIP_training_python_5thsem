#program to calculate the area and parameter of triangle 
print("Enter the sides of the triangle")
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("enter the third side "))
p = a+b+c 
s = p/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The perimeter of the triangle is:", p)
print("The area of the triangle is:", area)