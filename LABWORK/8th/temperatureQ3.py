'''City Temperature Monitoring System 
Problem Statement 
Daily temperatures of different cities are stored as: 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).  
6. Count cities with temperature between 35°C and 40°C.  
Sample Output 
Cities Above 40°C: 
Delhi 
Jaipur 
Ahmedabad 
 
Hottest City: Ahmedabad (43°C) 
 
Coolest City: Bengaluru (28°C) 
 
Average Temperature: 36.8°C 
 
Pleasant Cities: 
['Mumbai', 'Bengaluru', 'Pune'] 
 
Cities Between 35°C and 40°C: 4 '''
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
#create a list 
dict_items = list(temperature.items())

print(dict_items)
#-----------------------------------------------------------
# Display cities having temperature above 40°C

for item in dict_items:

    if item[1] > 40:
        print(item[0])
    else:
        pass

#-----------------------------------------------------------

# Find the hottest city

hottest_city = dict_items[0][0]
highest_temp = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_temp:
        hottest_city = item[0]
        highest_temp = item[1]

print("\nHottest City :", hottest_city, "---", highest_temp)

# --------------------------------------------------
# Find the coolest city

coolest_city = dict_items[0][0]
lowest_temp = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_temp:
        coolest_city = item[0]
        lowest_temp = item[1]

print("\nCoolest City :", coolest_city, "---", lowest_temp)

# --------------------------------------------------
# Calculate average temperature

total_temp = 0

for item in dict_items:
    total_temp += item[1]

average_temp = total_temp / len(dict_items)

print("\nAverage Temperature :", average_temp)

# --------------------------------------------------
# Create a list of pleasant cities

pleasant_cities = []

for item in dict_items:
    if item[1] < 35:
        pleasant_cities.append(item[0])

print("\nPleasant Cities :")
print(pleasant_cities)

# --------------------------------------------------
# Count cities with temperature between 35°C and 40°C

count = 0

for item in dict_items:
    if item[1] >= 35 and item[1] <= 40:
        count += 1
    else:
        pass

print("\nCities With Temperature Between 35°C and 40°C :", count)