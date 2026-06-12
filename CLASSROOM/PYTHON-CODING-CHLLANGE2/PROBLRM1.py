'''Problem 1: Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) of different houses in a residential society is stored as follows: 
Sample Data 
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
4. Calculate the total units consumed.  
5. Create separate lists for:  
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
#1. Display houses consuming more than 400 units.  
print("Display houses consuming more than 400 units")
for item, num in units.items():
    if num > 400:
        print(item, num)

#2. Find the highest-consuming house. 
hightet_consuming=max(units)
print("the highest-consuming house. ",hightet_consuming ,(num))

#3. Find the lowest-consuming house. 
lowest_house = ""
lowest_consuming = 320

for house in units:
    if units[house] < lowest_consuming:
        lowest_consuming = units[house]
        lowest_house = house

print("The lowest-consuming house:", lowest_house, lowest_consuming)

# Calculate the total units consumed.  

total_unit = sum(units.values())
print("Total Units:", total_unit)

'''5. Create separate lists for:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400) '''
lowerst_consuption =[]
Medium_Consumption =[]
hightet_consumiion =[]

for house, unit in units.items():
    if unit < 200:
        lowerst_consuption.append(house)
    elif unit <= 400:
        Medium_Consumption.append(house)
    else:
        hightet_consumiion.append(house)

print("Low Consumption (< 200):", lowerst_consuption)
print("Medium Consumption (200-400):",Medium_Consumption )
print("High Consumption (> 400):", hightet_consumiion)

#6. Count houses eligible for an energy-saving campaign (consumption > 300). '''
count = 0

for house, unit in units.items():
    if unit > 300:
        count = count + 1

print("Houses eligible for energy-saving campaign:", count)


