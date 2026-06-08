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


for i in range(len(dict_items)):
    if dict_items[i][1] > 20:
        print(dict_items[i][0])
print()