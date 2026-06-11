'''Problem 1: Smart Railway Reservation System 
Problem Statement 
A railway reservation system stores the booking status of seats in a train coach. 
Sample Data 
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
Tasks 
1. Display all available seat numbers.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Cancel booking for a given seat number.  
5. Store the updated reservation status in reservations.txt.  
6. Display occupancy percentage.  
Sample Output 
Available Seats: 
2 4 7 9 
 
Booked Seats: 6 
Available Seats: 4 
 
Seat 2 Reserved Successfully. 
 
Occupancy Percentage: 70.0% 
 
Reservation Details Saved Successfully. '''

seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}



# 1. Display available seats
available_seats = []

for seat in seats:
    if seats[seat] == "Available":
        available_seats.append(seat)

print("Available Seats:")
if len(available_seats) > 0:
    for seat in available_seats:
        print(seat, end=" ")
else:
    print("No available seats")
print("\n")


# 2. Count booked and available seats
booked = 0
available = 0

for seat in seats:
    if seats[seat] == "Booked":
        booked += 1
    else:
        available += 1

print("Booked Seats:", booked)
print("Available Seats:", available)
print()


# 3. Reserve first available seat
reserved = False

for seat in seats:
    if seats[seat] == "Available":
        seats[seat] = "Booked"
        print("Seat", seat, "Reserved Successfully.")
        reserved = True
        break

if reserved == False:
    print("No available seats to reserve.")

print()


# 4. Cancel booking
cancel_seat = int(input("Enter seat number to cancel booking: "))

if cancel_seat in seats:
    if seats[cancel_seat] == "Booked":
        seats[cancel_seat] = "Available"
        print("Seat", cancel_seat, "booking cancelled successfully.")
    else:
        print("Seat is not booked.")
else:
    print("Seat does not exist.")

print()


# 5. Save to file
file = open("reservations.txt", "w")

for seat in seats:
    file.write("Seat " + str(seat) + ": " + seats[seat] + "\n")

file.close()

print("Reservation Details Saved Successfully.")
print()


# 6. Occupancy percentage
booked = 0

for seat in seats:
    if seats[seat] == "Booked":
        booked += 1

total = len(seats)

if total > 0:
    percentage = (booked * 100) / total
else:
    percentage = 0

print("Occupancy Percentage:", round(percentage, 1), "%")