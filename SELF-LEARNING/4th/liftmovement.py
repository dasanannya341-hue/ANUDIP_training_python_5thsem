# Lift starts at floor 0
current = 0
total = 0

while True:
    dest = int(input("Enter Destination (-1 to stop): "))

    if dest == -1:
        break

    # Calculate floors travelled
    travelled = abs(dest - current)

    print("Travelled:", travelled, "floors")

    total += travelled
    current = dest

# Display total travel
print("Total Travelled:", total, "floors")