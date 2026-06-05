#An ATM machine requires the user to enter the correct PIN to access their account. The valid PIN is 1234. Write a program that repeatedly asks the user to enter a PIN until the correct PIN is entered. 
valid_pin = "1234"
while True:
    entered_pin = input("Please enter your PIN: ")
    if entered_pin == valid_pin:
        print("PIN accepted. Access granted.")
        break
    else:
        print("Incorrect PIN. Please try again.")