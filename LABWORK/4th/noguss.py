#Generate a secret number between 1 and 50. Allow the user to keep guessing until the correct number is found. Display: • "Too High"  • "Too Low"  • "Correct Guess"  Also display the total number of attempts. 
num = 25  # Secret number
attempts = 0
while True:
    guess = int(input("Enter your guess (between 1 and 50): "))
    attempts += 1
    if guess < num:
        print("Too Low")
    elif guess > num:
        print("Too High")
    else:
        print("Correct Guess!")
        print("Total attempts:", attempts)
        break