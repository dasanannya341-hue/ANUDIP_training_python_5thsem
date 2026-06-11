'''Problem 6: Employee Attendance Monitoring System 
Problem Statement 
Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P 
EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P 
EMP108,A 
EMP109,P 
EMP110,P 
Tasks 
1. Count present and absent employees.  
2. Display absent employee IDs.  
3. Calculate attendance percentage.  
4. Generate an absentee report in absent_report.txt.  
5. Display employees eligible for attendance awards (100% attendance).  
Sample Output 
Present Employees: 7 
 
Absent Employees: 3 
 
Absent Employee IDs: 
EMP102 
EMP105 
EMP108 
 
Attendance Percentage: 70.0% 
 
Absentee Report Generated Successfully. 
 
Attendance Award Eligibility: 
Not Applicabl'''

# Read file
attendance = {}

file = open("attendance.txt", "r")

for line in file:
    data = line.strip().split(",")

    # validation using if-else
    if len(data) == 2:
        emp_id = data[0]
        status = data[1]

        if status == "P" or status == "A":
            attendance[emp_id] = status

file.close()

# Counters
present = 0
absent = 0

print("Absent Employee IDs:")
absent_ids = []

# Count present and absent
for emp_id in attendance:
    if attendance[emp_id] == "P":
        present = present + 1
    else:
        absent = absent + 1
        absent_ids.append(emp_id)
        print(emp_id)

print()

# Attendance percentage
total = present + absent

if total > 0:
    percentage = (present / total) * 100
    print("Present Employees:", present)
    print("Absent Employees:", absent)
    print(f"Attendance Percentage: {percentage:.1f}%")
else:
    print("No valid data found")

print()

# Write absent report
file = open("absent_report.txt", "w")

file.write("ABSENT EMPLOYEE REPORT\n\n")

for emp in absent_ids:
    file.write(emp + "\n")

file.close()

print("Absentee Report Generated Successfully.")

print()

# Award eligibility
if absent == 0:
    print("Attendance Award Eligibility:")
    for emp_id in attendance:
        print(emp_id)
else:
    print("Attendance Award Eligibility:")
    print("Not Applicable")