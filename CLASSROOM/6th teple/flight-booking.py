'''A flight reservation system stores passenger records as tuples: 
bookings = ( 
    ("P101", "Delhi", "Confirmed"), 
    ("P102", "Mumbai", "Waiting"), 
    ("P103", "Delhi", "Confirmed"), 
    ("P104", "Chennai", "Cancelled"), 
    ("P105", "Mumbai", "Confirmed"), 
    ("P106", "Delhi", "Waiting") 
) 
Where: 
• Passenger ID  
• Destination  
• Booking Status  
Tasks 
Write a Python program to: 
1. Display all passengers whose booking status is Confirmed.  
2. Count the number of passengers travelling to Delhi.  
3. Count Confirmed, Waiting, and Cancelled bookings separately.  
4. Create a list containing passenger IDs with Waiting status.  
5. Determine which destination has the highest number of bookings. '''

bookings = ( 
    ("P101", "Delhi", "Confirmed"), 
    ("P102", "Mumbai", "Waiting"), 
    ("P103", "Delhi", "Confirmed"), 
    ("P104", "Chennai", "Cancelled"), 
    ("P105", "Mumbai", "Confirmed"), 
    ("P106", "Delhi", "Waiting") 
)
# Task1-Display all passengers whose booking status is Confirmed.
print("confermed passanger")
for booking in bookings:
    if booking[2] == "Confirmed":
        print( booking[0], booking[1])
#--------------------------------------------------------------------------------------------------------
# Task 2 - count the number of passanger travelling to delhi 

delhi_count = 0
for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1

print("\nNumber of passengers travelling to Delhi:", delhi_count)

#--------------------------------------------------------------------------------------------------------

# Task 3: Count Confirmed, Waiting, and Cancelled bookings
confirmed = 0
waiting = 0
cancelled = 0

for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed += 1
    elif booking[2] == "Waiting":
        waiting += 1
    elif booking[2] == "Cancelled":
        cancelled += 1

print("\nBooking Status Count:")
print("Confirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

#-----------------------------------------------------------------------------------------------------
# Task 4: Create a list of passenger IDs with Waiting status
waiting_ids = []

for booking in bookings:
    if booking[2] == "Waiting":
        waiting_ids.append(booking[0])

print("\nPassenger IDs with Waiting Status:")
print(waiting_ids) 
#--------------------------------------------------------------------------------------------------------
# task 5 -Determine which destination has the highest number of bookings.
delhi = 0
mumbai = 0
chennai = 0
for booking in bookings:
    if booking[1] == "Delhi":
        delhi += 1
    elif booking[1] == "Mumbai":
        mumbai += 1
    elif booking[1] == "Chennai":
        chennai += 1

highest_destination = "Delhi"
highest_count = delhi

if mumbai > highest_count:
    highest_destination = "Mumbai"
    highest_count = mumbai

if chennai > highest_count:
    highest_destination = "Chennai"
    highest_count = chennai

print("\nDestination with highest number of bookings:")
print(highest_destination, "--", highest_count)

    
 
  