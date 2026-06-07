'''. Student Attendance Tracker 
Problem Statement 
Attendance for 15 days is recorded as: 
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
Write a program to: 
• Count present and absent days.  
• Calculate attendance percentage.  
• Determine eligibility (minimum 75% attendance).  
• Display positions where the student was absent. '''

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 

#count present and absent 
count_present = 0 
count_absent = 0 
for item in attendance:
    if item == 'P':
        count_present += 1
    elif item == 'A': 
        count_absent +=1


print(count_present)
print( count_absent)
     
#============================================================================================
#Calculate attendance percentage.

attendance_percentage = (count_present / len(attendance)) * 100
print("Attendance Percentage:", attendance_percentage, "%")

#============================================================
#Determine eligibility 
if attendance_percentage >=75:
    print("eligible for exam")
else:
    print("not eligible for exam")

#=============================================================
#display positions where student student was absent 
print("absent on days :")
for i in range(len(attendance)):
    if attendance[i] =='A':

      print(i+1,end=" ")

