'''Problem 3: Smart Parking Management System 
Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
] 
Tasks 
1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt.  
Sample Output 
Vacant Parking Slots: 
2 4 7 9 
 
Occupied Slots: 6 
Vacant Slots: 4 
 
Vehicle Allocated to Slot 2 
 
Occupancy Percentage: 70.0% 
 
Parking Details Saved Successfully.'''

parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
] 

#  Display vacant parking slot numbers. 

# Parking data
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# 1. Display vacant parking slot numbers
vacant_slots = []

print("Vacant Parking Slots:")
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        vacant_slots.append(i + 1)  
         # slot number starts from 1
        print(i + 1, end=" ")
print("\n")

# 2. Count occupied and vacant slots
occupied_count = parking_slots.count("Occupied")
vacant_count = parking_slots.count("Vacant")

print(f"Occupied Slots: {occupied_count}")
print(f"Vacant Slots: {vacant_count}\n")

# 3. Allocate first vacant slot (with validation)
if vacant_count > 0:
    first_vacant_index = parking_slots.index("Vacant")
    parking_slots[first_vacant_index] = "Occupied"

    print(f"Vehicle Allocated to Slot {first_vacant_index + 1}")
else:
    print("No vacant slots available")
print()

# 4. Calculate occupancy percentage (with validation)
total_slots = len(parking_slots)

if total_slots > 0:
    occupied_count = parking_slots.count("Occupied")
    occupancy_percentage = (occupied_count / total_slots) * 100
    print(f"Occupancy Percentage: {occupancy_percentage:.1f}%")
else:
    print("No parking slots found")
print()

# 5. Store updated parking information in file
try:
    with open("parking.txt", "w") as file:
        for i, status in enumerate(parking_slots):
            file.write(f"Slot {i + 1}: {status}\n")

    print("Parking Details Saved Successfully.")
except Exception as e:
    print("Error saving file:", e)