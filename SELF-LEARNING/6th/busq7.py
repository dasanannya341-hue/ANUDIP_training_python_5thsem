'''7. Bus Route Passenger Analysis 
Sample Data 
passengers = { 
    "Stop1": 12, 
    "Stop2": 25, 
    "Stop3": 18, 
    "Stop4": 32, 
    "Stop5": 9, 
    "Stop6": 28, 
    "Stop7": 14, 
    "Stop8": 7, 
    "Stop9": 21, 
    "Stop10": 16 
} 
Tasks 
• Display stops having more than 20 passengers.  
• Count stops with fewer than 10 passengers.  
• Find the busiest stop.  
• Create a list of stops requiring an extra bus (passengers > 25).  
• Calculate the average number of passengers.  '''

passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Stops having more than 20 passengers
print("Stops Having More Than 20 Passengers:")
for stop in passengers:
    if passengers[stop] > 20:
        print(stop)

# Count stops with fewer than 10 passengers
count = 0
for stop in passengers:
    if passengers[stop] < 10:
        count += 1

print("\nStops With Fewer Than 10 Passengers:", count)

# Busiest stop
highest = 0
busiest_stop = ""

for stop in passengers:
    if passengers[stop] > highest:
        highest = passengers[stop]
        busiest_stop = stop

print("\nBusiest Stop:")
print(busiest_stop, "(", highest, ")", sep="")

# Stops requiring extra bus
extra_bus = []

for stop in passengers:
    if passengers[stop] > 25:
        extra_bus.append(stop)

print("\nStops Requiring Extra Bus:")
print(extra_bus)

# Average passengers
total = 0
count = 0

for stop in passengers:
    total += passengers[stop]
    count += 1

average = total / count

print("\nAverage Passengers:", average)