'''Assignment 4: Vehicle Registration Verification System 
Problem Statement 
A transport department wants to verify vehicle registration numbers. 
Store at least 20 vehicle numbers. 
Example 
MH12AB4589 
DL05XY9988 
KA03PQ1234 
Requirements 
For each registration number: 
1. Extract state code.  
2. Extract district code.  
3. Extract series.  
4. Extract vehicle number.  
5. Count letters and digits.  
6. Validate format:  
o First 2 characters = Alphabets  
o Next 2 characters = Digits  
o Next 2 characters = Alphabets  
o Last 4 characters = Digits  
7. Display invalid registrations.  
8. Count vehicles state-wise.  
Challenge 
Generate a state-wise report: 
MH -> 6 Vehicles 
DL -> 4 Vehicles 
KA -> 5 Vehicles 
UP -> 5 Vehicles'''

# Vehicle Registration Verification System

vehicles = [
    "MH12AB4589",
    "DL05XY9988",
    "KA03PQ1234",
    "UP14CD5678",
    "MH22EF1111",
    "DL08GH2222",
    "KA09IJ3333",
    "UP10KL4444",
    "MH15MN5555",
    "DL20OP6666",
    "KA11QR7777",
    "UP12ST8888",
    "MH18UV9999",
    "DL25WX1234",
    "KA05YZ5678",
    "UP09AB4321",
    "MH07CD8765",
    "KA13EF2468",
    "UP16GH1357",
    "MH21IJ9876"
]

state_count = {}
invalid_registrations = []

# Process each vehicle number
for reg in vehicles:

    print("\nVehicle Number :", reg)

    # Extract details
    state_code = reg[0:2]
    district_code = reg[2:4]
    series = reg[4:6]
    vehicle_number = reg[6:10]

    print("State Code :", state_code)
    print("District Code :", district_code)
    print("Series :", series)
    print("Vehicle Number :", vehicle_number)

    # Count letters and digits
    letters = 0
    digits = 0

    for ch in reg:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1

    print("Letters :", letters)
    print("Digits :", digits)

    # Validate registration format
    if (len(reg) == 10 and
        reg[0:2].isalpha() and
        reg[2:4].isdigit() and
        reg[4:6].isalpha() and
        reg[6:10].isdigit()):

        print("Valid Registration")

        # Count vehicles state-wise
        if state_code in state_count:
            state_count[state_code] += 1
        else:
            state_count[state_code] = 1

    else:
        print("Invalid Registration")
        invalid_registrations.append(reg)

# Display invalid registrations
print("\n===== INVALID REGISTRATIONS =====")

if len(invalid_registrations) == 0:
    print("No Invalid Registrations")
else:
    for reg in invalid_registrations:
        print(reg)

# State-wise report
print("\n===== STATE-WISE REPORT =====")

for state in state_count:
    print(state, "->", state_count[state], "Vehicles")