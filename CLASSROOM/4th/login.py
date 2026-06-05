#A website allows users to log in using a password. The correct password is admin123. Write a program that keeps asking the user to enter the password until the correct password is provided
valid_password = "admin123"
while True:
    entered_password = input("Please enter the password: ")
    if entered_password == valid_password:
        print("Login successful")
        break
    else:
        print("Incorrect password.")
        print("Please try again.")