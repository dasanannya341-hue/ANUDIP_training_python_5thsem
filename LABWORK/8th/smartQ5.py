'''5. Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) is stored as: 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate total units consumed.  
5. Create lists:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300). '''

units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")

for house in units:
    if units[house] > 400:
        print(house)

# 2. Highest Consumption
highest = 0
highest_house = ""

for house in units:
    if units[house] > highest:
        highest = units[house]
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, "(", highest, " units)", sep="")

# 3. Lowest Consumption
lowest = 1000
lowest_house = ""

for house in units:
    if units[house] < lowest:
        lowest = units[house]
        lowest_house = house

print("\nLowest Consumption:")
print(lowest_house, "(", lowest, " units)", sep="")

# 4. Total Units Consumed
total = 0

for house in units:
    total += units[house]

print("\nTotal Units Consumed:", total)

# 5. Consumption Lists
low = []
medium = []
high = []

for house in units:

    if units[house] < 200:
        low.append(house)

    elif units[house] <= 400:
        medium.append(house)

    else:
        high.append(house)

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)

# 6. Energy-Saving Campaign
count = 0

for house in units:
    if units[house] > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)