#program to check whether the triangle is valid or not
angle1 = int(input("enter the first angle :"))
if(angle1 <= 0):
    exit("Angle cannot be negative or zero")
#------------------------------------------------------
angle2 = int(input("enter the second angle :"))
if(angle2 <= 0):
    exit("Angle cannot be negative or zero")
angle3 = int(input("enter the third angle :"))
#-----------------------------------------------------
if(angle3 <= 0):
    exit("Angle cannot be negative or zero")
#check whether the sum of angles is 180 or not
#if the sum of angles is 180 then the triangle is valid otherwise it is not valid8
if(angle1 + angle2 + angle3 == 180):
    print("The triangle is valid")
else:
    print("The triangle is not valid")