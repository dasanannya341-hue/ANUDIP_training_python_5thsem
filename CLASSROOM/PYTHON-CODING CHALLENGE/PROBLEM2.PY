'''Problem 2: Hospital Patient Record Management System 
Problem Statement 
A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
P101,Anuj,Normal 
P102,Rahul,Critical 
P103,Priya,Stable 
P104,Neha,Critical 
P105,Amit,Stable 
P106,Sneha,Normal 
P107,Karan,Critical 
P108,Pooja,Stable 
P109,Rohit,Normal 
P110,Anjali,Stable 
Tasks 
1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt.  
Sample Output 
Critical Patients: 
Rahul 
Neha 
Karan 
 
Patient Count: 
Normal : 3 
Stable : 4 
Critical : 3 
 
Patient Found: 
P104,Neha,Critical 
 
Critical Patient Report Generated Successfully.'''

patients = {}

# ---------- 1. READ FILE ----------
file = open("pat.txt", "r")

for line in file:
    data = line.strip().split(",")

    # simple validation
    if len(data) == 3:
        pid = data[0]
        name = data[1]
        status = data[2]

        patients[pid] = [name, status]

file.close()


# ---------- 2. DISPLAY ALL PATIENTS ----------
print("\nAll Patients:")
for pid in patients:
    print(pid, patients[pid][0], patients[pid][1])


# ---------- 3. DISPLAY CRITICAL PATIENTS ----------
print("\nCritical Patients:")
for pid in patients:
    if patients[pid][1] == "Critical":
        print(patients[pid][0])


# ---------- 4. COUNT PATIENTS ----------
normal = 0
stable = 0
critical = 0

for pid in patients:
    status = patients[pid][1]

    if status == "Normal":
        normal += 1
    elif status == "Stable":
        stable += 1
    elif status == "Critical":
        critical += 1

print("\nPatient Count:")
print("Normal :", normal)
print("Stable :", stable)
print("Critical :", critical)


# ---------- 5. SEARCH PATIENT ----------
search = input("\nEnter Patient ID: ")

if search in patients:
    print("Patient Found:")
    print(search, patients[search][0], patients[search][1])
else:
    print("Patient Not Found")


# ---------- 6. SAVE CRITICAL PATIENTS ----------
file = open("pat.txt", "w")

for pid in patients:
    if patients[pid][1] == "Critical":
        file.write(pid + "," + patients[pid][0] + "," + patients[pid][1] + "\n")

file.close()

print("\nCritical Patient Report Saved Successfully.")