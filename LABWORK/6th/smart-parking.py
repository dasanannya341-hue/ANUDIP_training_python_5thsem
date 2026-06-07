'''3. Smart Parking System 
Problem Statement 
Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
Where: 
• 1 = Occupied  
• 0 = Available  
Write a program to: 
• Count occupied and available slots.  
• Find the first available slot.  
• Display all available slot numbers.  
• Check whether parking occupancy exceeds 75%.  '''

slots = [1, 0, 1, 1, 0, 0, 1, 0] 

#=========================================
#Count occupied and available slots. 
occupied = 0 
available = 0 

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("occupied slots ",occupied)
print("avalable slots ",available)
#==============================================
#Find the first available slot. 
print(" the first available slot. ")
for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1)
#==============================================
## Display all available slot numbers
print("Available Slot Numbers:")
for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1, end=" ")

print()
#==============================================
# Check whether parking occupancy exceeds 75%.

slots = [1, 0, 1, 1, 0, 0, 1, 0]

occupied = 0

for slot in slots:
    if slot == 1:
        occupied += 1

if occupied > (len(slots) * 75 / 100):
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")