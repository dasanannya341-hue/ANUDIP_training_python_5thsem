#A customer's transactions are stored as: ATM TRANSITION
transactions = [5000, -2000, 3000, -1000, -500, 7000]
balance = 0
deposits = []
withdrawals = []
#Calculate the current balance, total deposits, and total withdrawals.
for transaction in transactions:
    balance += transaction
    if transaction > 0:
        deposits.append(transaction)
    else:
        withdrawals.append(transaction)
print("Current Balance: ", balance)
#list of deposits and withdrawals
print("Deposits: ", deposits)
print("Withdrawals: ", withdrawals)
#find largest deposit and largest withdrawal
largest_deposit = deposits[0]
for deposit in deposits:
    if deposit > largest_deposit:
        largest_deposit = deposit
largest_withdrawal = withdrawals[0]
for withdrawal in withdrawals:
    if withdrawal < largest_withdrawal:
        largest_withdrawal = withdrawal
print("Total Deposits: ", sum(deposits))
print("Total Withdrawals: ", sum(withdrawals))
print("Largest Deposit: ", largest_deposit)
print("Largest Withdrawal: ", largest_withdrawal)
