#Write a program that accepts marks from the user and continues asking for marks until the entered score is 40 or more. Display a congratulatory message once the student passes the assessment.
marks=0
while marks<40:
    marks=int(input("Enter marks: "))
    if marks<40:
        print("Marks entered:",marks)
        print("Result: FAIL")
    else:
        print("Marks entered:",marks)
        print("Result: PASS")
    