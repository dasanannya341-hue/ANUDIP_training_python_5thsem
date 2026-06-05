# Initialize counters
high_count = 0
low_count = 0
total = 0

# Input transactions
while True:
    amt = int(input("Enter transaction (-1 to stop): "))

    if amt == -1:
        break

    total += amt

    if amt > 50000:
        high_count += 1

    if amt < 1000:
        low_count += 1

# Display results
print("Transactions above ₹50000:", high_count)
print("Transactions below ₹1000:", low_count)
print("Total Transaction Amount:", total)