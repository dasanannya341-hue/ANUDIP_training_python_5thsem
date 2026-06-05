#Initial Balance = ₹10,000 Display a menu repeatedly: 1. Check Balance 2. Deposit 3. Withdraw 4. Exit Requirements: • Withdrawal should not exceed balance.  • Display appropriate messages.  • Continue until Exit is selected.  
balance = 10000
while True:
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print("Your current balance is: ₹", balance)
    
    elif choice == '2':
        deposit_amount = float(input("Enter the amount to deposit: ₹"))
        if deposit_amount > 0:
            balance += deposit_amount
            print("Amount deposited successfully. New balance: ₹", balance)
        else:
            print("Deposit amount must be positive.")
    
    elif choice == '3':
        withdraw_amount = float(input("Enter the amount to withdraw: ₹"))
        if withdraw_amount > balance:
            print("Insufficient balance. Your current balance is: ₹", balance)
        elif withdraw_amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            balance -= withdraw_amount
            print("Amount withdrawn successfully. New balance: ₹", balance)
    
    elif choice == '4':
        print("Thank you for using the ATM simulation system. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option (1-4).")
                