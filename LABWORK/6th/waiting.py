'''Train Reservation Waiting List 
Problem Statement 
Passenger records: 
passengers = [ 
    ("Anuj", "Confirmed"), 
    ("Rahul", "Waiting"), 
    ("Priya", "Confirmed"), 
    ("Amit", "Waiting"), 
    ("Neha", "Confirmed") 
] 
Write a program to: 
• Display all waiting-list passengers.  
• Count confirmed and waiting passengers.  
• Find whether a specific passenger has a confirmed ticket.  
• Create separate lists for confirmed and waiting passengers.'''

passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed_count = 0
waiting_count = 0

confirmed_list = []
waiting_list = []

# Display all waiting-list passengers
print("Waiting List Passengers:")
for item in passengers:
    if item[1] == "Waiting":
        print(item[0])

# Count confirmed and waiting passengers
for item in passengers:
    if item[1] == "Confirmed":
        confirmed_count += 1
    else:
        waiting_count += 1

print("\nConfirmed Passengers =", confirmed_count)
print("Waiting Passengers =", waiting_count)

# Find whether a specific passenger has a confirmed ticket
name = input("\nEnter passenger name: ")

found = False

for item in passengers:
    if item[0] == name and item[1] == "Confirmed":
        found = True

if found:
    print(name, "has a confirmed ticket")
else:
    print(name, "does not have a confirmed ticket")

# Create separate lists for confirmed and waiting passengers
for item in passengers:
    if item[1] == "Confirmed":
        confirmed_list.append(item[0])
    else:
        waiting_list.append(item[0])

print("\nConfirmed List =", confirmed_list)
print("Waiting List =", waiting_list)