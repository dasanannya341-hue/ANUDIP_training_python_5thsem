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

# 1. Display all available seat numbers.
available_seats = []
for seat_num, status in seats.items():
    if status == "Available":
        available_seats.append(seat_num)

print("Available Seats:")
if available_seats:
    print(" ".join(str(seat) for seat in available_seats))
else:
    print("No available seats")
print()

# 2. Count booked and available seats.
booked_count = 0
available_count = 0
for status in seats.values():
    if status == "Booked":
        booked_count += 1
    else:
        available_count += 1

print(f"Booked Seats: {booked_count}")
print(f"Available Seats: {available_count}")
print()

# 3. Reserve the first available seat.
if available_seats:
    first_available = available_seats[0]
    seats[first_available] = "Booked"
    print(f"Seat {first_available} Reserved Successfully.")
else:
    first_available = None
    print("No available seats to reserve.")
print()

# 4. Cancel booking for a given seat number.
try:
    cancel_seat = int(input("Enter seat number to cancel booking: "))
    if cancel_seat in seats:
        if seats[cancel_seat] == "Booked":
            seats[cancel_seat] = "Available"
            print(f"Seat {cancel_seat} booking cancelled successfully.")
        else:
            print(f"Seat {cancel_seat} is not currently booked.")
    else:
        print(f"Seat {cancel_seat} does not exist.")
except ValueError:
    print("Invalid seat number entered.")
print()

# 5. Store the updated reservation status in reservations.txt.
with open("reservations.txt", "w") as reservation_file:
    for seat, status in sorted(seats.items()):
        reservation_file.write(f"Seat {seat}: {status}\n")
print("Reservation Details Saved Successfully.")
print()

# 6. Display occupancy percentage.
booked_count = 0
for status in seats.values():
    if status == "Booked":
        booked_count += 1

if len(seats) > 0:
    occupancy_percentage = (booked_count / len(seats)) * 100
else:
    occupancy_percentage = 0.0

print(f"Occupancy Percentage: {occupancy_percentage:.1f}%")

