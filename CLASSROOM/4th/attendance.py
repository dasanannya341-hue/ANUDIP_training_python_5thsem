#A teacher is recording attendance as students enter the classroom. The class strength is 30 students. Write a program that inputs whether Student is Present or Absent. Display total number of student present as well as absent.
attendance_count=0
absent_count=0 
while attendance_count+absent_count<30:
    student_number=attendance_count+absent_count+1
    status=input(f"Is student {student_number} present? (present/absent): ")
    if status=='present':
        attendance_count+=1
        print(f"Student {student_number}")
        print("Attendance:",status)
    elif status=='absent':
        absent_count+=1
        print(f"Student {student_number}")

        print("Attendance:",status)
print("Total number of students present:",attendance_count)
print("Total number of students absent:",absent_count)