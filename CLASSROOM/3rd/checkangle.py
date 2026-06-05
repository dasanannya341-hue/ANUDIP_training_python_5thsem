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
#if the sum of angles is 180 then the triangle is valid otherwise it is not valid
if(angle1 + angle2 + angle3 == 180):
    print("The triangle is valid")
#verifying triangle formation using angle 
    if(angle1 == 90 or angle2 == 90 or angle3 == 90):
        print("The triangle is a right angled triangle")
    elif(angle1 > 90 or angle2 > 90 or angle3 > 90):
        print("The triangle is an obtuse angled triangle")
    else:
        print("The triangle is an acute angled triangle")
else:
    print("The triangle is not valid")