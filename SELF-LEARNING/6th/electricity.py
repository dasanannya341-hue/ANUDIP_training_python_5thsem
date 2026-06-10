''' Electricity Consumption Report 
Sample Data 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 450, 
    "House104": 290, 
    "House105": 150, 
    "House106": 510, 
    "House107": 220, 
    "House108": 390, 
    "House109": 170, 
    "House110": 260 
} 
Tasks 
• Display houses consuming more than 300 units.  
• Count houses consuming less than 200 units.  
• Find the house with the highest consumption.  
• Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).  
• Categorize houses as:  
o Low: < 200 units  
o Medium: 200–350 units  
o High: > 350 units  '''

units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Houses consuming more than 300 units
print("Houses Consuming More Than 300 Units:")
for house in units:
    if units[house] > 300:
        print(house)

# Count houses consuming less than 200 units
count = 0

for house in units:
    if units[house] < 200:
        count += 1

print("\nHouses Consuming Less Than 200 Units:", count)

# Highest consumption
highest = 0
highest_house = ""

for house in units:
    if units[house] > highest:
        highest = units[house]
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, "(", highest, " units)", sep="")

# Energy-saving awareness campaign
campaign = []

for house in units:
    if units[house] > 400:
        campaign.append(house)

print("\nEligible for Awareness Campaign:")
print(campaign)

# Categorize houses
low = []
medium = []
high = []

for house in units:

    if units[house] < 200:
        low.append(house)

    elif units[house] <= 350:
        medium.append(house)

    else:
        high.append(house)

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)