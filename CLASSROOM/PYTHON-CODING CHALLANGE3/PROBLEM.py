'''Problem 1: Cyber Security Login Audit System 
Problem Statement 
A file named login_logs.txt contains user login attempts in the following format: 
username,status 
anuj,Success 
rahul,Failed 
anuj,Failed 
priya,Failed 
rahul,Failed 
neha,Success 
anuj,Failed 
karan,Failed 
rahul,Success 
priya,Failed 
Tasks 
1. Count successful and failed login attempts.  
2. Identify users with more than 2 failed attempts.  
3. Create a dictionary storing the number of failures per user.  
4. Create a set of users who logged in successfully.  
5. Display users whose accounts should be reviewed.  
Sample Output 
Successful Login Attempts: 3 
Failed Login Attempts: 7 
 
Failure Count per User: 
anuj : 2 
rahul : 2 
priya : 2 
karan : 1 
 
Users with Successful Logins: 
{'anuj', 'neha', 'rahul'} 
 
Accounts Requiring Review: 
None'''


# Open the file
file = open("ANUDIP_training_python_5thsem/CLASSROOM/PYTHON-CODING CHALLANGE3/login_logs.txt", "r")
#1. Count successful and failed login attempts.  
success_count = 0
failed_count = 0

failure_dict = {}
successful_users = set()

# Read each line
for line in file:
    line = line.strip()

    # Skip header
    if line == "username,status":
        continue

    username, status = line.split(",")

    if status == "Success":
        success_count += 1
        successful_users.add(username)

    elif status == "Failed":
        failed_count += 1

        if username in failure_dict:
            failure_dict[username] += 1
        else:
            failure_dict[username] = 1

file.close()

# Users with more than 2 failed attempts
review_users = []

for user, count in failure_dict.items():
    if count > 2:
        review_users.append(user)

# Output
print("Successful Login Attempts:", success_count)
print("Failed Login Attempts:", failed_count)

print("\nFailure Count per User:")
for user, count in failure_dict.items():
    print(user, ":", count)

print("\nUsers with Successful Logins:")
print(successful_users)

print("\nAccounts Requiring Review:")
if review_users:
    for user in review_users:
        print(user)
else:
    print("None") 