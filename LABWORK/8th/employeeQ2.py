'''2. Employee Performance Dashboard 
Problem Statement 
Employee performance scores are stored as: 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Create separate lists:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60)  
Sample Output 
Employees Scoring Above 80: 
EMP101 
EMP104 
EMP105 
EMP107 
 
Top Performer: EMP105 (97) 
 
Employees Needing Improvement: 3 
 
Average Score: 71.3 
 
Excellent: 
['EMP101', 'EMP105'] 
 
Good: 
['EMP102', 'EMP104', 'EMP107'] 
 
Average: 
['EMP108', 'EMP110'] 
 
Poor: 
['EMP103', 'EMP106', 'EMP109']'''

performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 

#create a list 
dict_items = list(performance.items())
#Display employees scoring above 80.
print("Employees Scoring Above 80 :")

for item in dict_items:
    if item[1] > 80:
        print(item[0])

# Count employees needing improvement (score < 60)

improvement_count = 0

for item in dict_items:
    if item[1] < 60:
        improvement_count += 1

print("\nEmployees Needing Improvement :", improvement_count)

# --------------------------------------------------
#Find the top performer. 
top_employee = dict_items[0][0]
top_score = dict_items[0][1]

for item in dict_items:
    if item[1] > top_score:
        top_employee = item[0]
        top_score = item[1]

print("\nTop Performer :", top_employee, "(", top_score, ")")

#------------------------------------------------------------
# Calculate average performance score

total_score = 0

for item in dict_items:
    total_score += item[1]

average_score = total_score / len(dict_items)

print("\nAverage Score :", average_score) 
#--------------------------------------------------------------------
## Create separate lists

excellent = []
good = []
average = []
poor = []

for item in dict_items:

    if item[1] >= 90:
        excellent.append(item[0])

    elif item[1] >= 75 and item[1] <= 89:
        good.append(item[0])

    elif item[1] >= 60 and item[1] <= 74:
        average.append(item[0])

    else:
        poor.append(item[0])

print("\nExcellent :")
print(excellent)

print("\nGood :")
print(good)

print("\nAverage :")
print(average)

print("\nPoor :")
print(poor)
