# Employee Performance Evaluation
# A company stores employee details in a tuple. Each employee record contains:
#
# ("E101", "Anuj", 92),
# ("E102", "Rahul", 76),
# ("E103", "Priya", 58),
# ("E104", "Neha", 88),
# ("E105", "Amit", 45)
#
# Where:
# - First value = Employee ID
# - Second value = Employee Name
# - Third value = Performance Score
#
# Tasks:
# 1. Display details of employees scoring 80 or above.
# 2. Count the number of employees who need improvement (score below 60).
# 3. Find the employee with the highest score.
# 4. Create a list containing the names of all employees scoring above 75.
# 5. Display the performance category for each employee.

employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45),
)
#-----------------------------------------------------------------------------------------------------------------------
# Task 1: Display details of employees scoring 80 or above
print("Employees scoring 80 or above:")
for emp in employees:
    if emp[2] >= 80:
        print("employee scoring 80 0r above")
        print(f"\n {emp[0]},  {emp[1]}, {emp[2]}")

#--------------------------------------------------------------------------------------------------------------------------------
# Task 2: Count the number of employees who need improvement (score below 60)
improvement_count = 0
for emp in employees:
    if emp[2] < 60:
        improvement_count += 1
print(f"Number of employees who need improvement: {improvement_count}")

#----------------------------------------------------------------------------------------------------------------------------------
# Task 3: Find the employee with the highest score
highest_score = employees[0][2]
highest_emp = employees[0]
for emp in employees:
    if emp[2] > highest_score:
        highest_score = emp[2]
        highest_emp = emp
print(f"Employee with the highest score:  {highest_emp[0]},  {highest_emp[1]}, {highest_emp[2]}")

#-----------------------------------------------------------------------------------------------------------------------------
# Task 4 : create list containing the name of all employee scoring above 75
above_75 = []

for emp in employees:
    if emp[2] > 75:
        above_75.append(emp[1])


#---------------------------------------------------------------------------------------------------------------------------------------
# Task 5: Display performance category for each employee
print("\nPerformance Category:")
for emp in employees:
    score = emp[2]
    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"
    print(f" {emp[0]} {emp[1]} ----> {category}")
    