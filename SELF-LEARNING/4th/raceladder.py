# Input number of racers
n = int(input("Enter number of racers: "))

# Input first racer's lap time
time = float(input("Enter lap time of racer 1: "))
fastest = slowest = time
fast_pos = slow_pos = 1

# Input remaining racers
for i in range(2, n + 1):
    time = float(input(f"Enter lap time of racer {i}: "))

    if time < fastest:
        fastest = time
        fast_pos = i

    if time > slowest:
        slowest = time
        slow_pos = i

# Display results
print("Fastest Racer Position:", fast_pos)
print("Slowest Racer Position:", slow_pos)
print("Difference:", slowest - fastest)