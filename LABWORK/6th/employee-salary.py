'''Problem Statement 
Employee data is stored as tuples: 
employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 
Write a program to: 
• Display employees earning above ₹50,000.  
• Find the highest-paid employee.  
• Calculate total salary expenditure.  
• Count employees earning below ₹40,000.  '''

employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 

#display employee earning above 50000
employee_earning = 0
for item in employees:
    if item[1] > 50000:
        employee_earning += 1
print("employee above")

#find most higest paid employee
employee_earnings = 0 
best_employee = None
for item in employees:
    if item[1] > employee_earnings:
      employee_earnings = item[1] 
      best_employee = item 

print("employee highest paid ", item )
#---------------------------------------------------------
# Calculate total salary expenditure.
total_salary = 0

for item in employees:
    total_salary += item[1]


print("total salary",total_salary)

#----------------------------------------------------------
# Count employees earning below ₹40,000.

count_employe = 0 
for item in employees:
    if item[1]<= 40000:
        count_employe +=1

print("less then 40000",count_employe)