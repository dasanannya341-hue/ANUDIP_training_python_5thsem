'''Problem Statement 
Passenger count at each stop: 
passengers = [12, 18, 25, 30, 28, 15, 8] 
Write a program to: 
• Find the busiest stop.  
• Display stops with fewer than 10 passengers.  
• Calculate average passengers.  
• Determine whether any stop exceeded 25 passengers. '''

passengers = [12, 18, 25, 30, 28, 15, 8]

# Find busiest stop
busiest = passengers[0]
stop_no = 1

for i in range(len(passengers)):
    if passengers[i] > busiest:
        busiest = passengers[i]
        stop_no = i + 1

print("Busiest Stop:", stop_no)
print("Passengers:", busiest)

# Display stops with fewer than 10 passengers
print("\nStops with fewer than 10 passengers:")
for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

# Calculate average passengers
total = 0

for item in passengers:
    total += item

average = total / len(passengers)
print("\nAverage Passengers:", average)

# Check if any stop exceeded 25 passengers
exceeded = False

for item in passengers:
    if item > 25:
        exceeded = True

if exceeded:
    print("A stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")