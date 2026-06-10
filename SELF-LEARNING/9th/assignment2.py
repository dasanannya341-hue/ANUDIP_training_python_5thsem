'''Assignment 2: Email Validation & Domain Analytics System 
Problem Statement 
An organization has collected 20 email addresses from users. 
Create a program to analyze these email addresses. 
Requirements 
For each email: 
1. Extract username.  
2. Extract domain.  
3. Extract extension.  
4. Count digits in username.  
5. Count special characters.  
6. Check if email is valid:  
o Exactly one '@'  
o Contains '.'  
o No spaces  
7. Display invalid emails.  
8. Count emails belonging to each domain.  
Sample Input 
rahul123@gmail.com 
priya@outlook.com 
anuj@company.in 
Challenge 
Generate a domain report: 
gmail.com     -> 8 users 
outlook.com   -> 5 users 
yahoo.com     -> 3 users 
company.in    -> 4 users'''

# Email Validation & Domain Analytics System

domain_count = {}
invalid_emails = []

# Input 20 email addresses
for i in range(1, 21):

    print("\nEmail", i)
    email = input("Enter Email: ")

    print("\n--- Email Analysis ---")

    # Validation
    if email.count("@") == 1 and "." in email and " " not in email:

        # Extract username
        username = email.split("@")[0]

        # Extract domain
        domain = email.split("@")[1]

        # Extract extension
        extension = domain.split(".")[-1]

        # Count digits in username
        digit_count = 0

        for ch in username:
            if ch.isdigit():
                digit_count += 1

        # Count special characters in username
        special_count = 0

        for ch in username:
            if not ch.isalnum():
                special_count += 1

        print("Username :", username)
        print("Domain :", domain)
        print("Extension :", extension)
        print("Digits in Username :", digit_count)
        print("Special Characters :", special_count)
        print("Valid Email")

        # Domain analytics
        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1

    else:
        print("Invalid Email")
        invalid_emails.append(email)

# Display Invalid Emails
print("\n===== INVALID EMAILS =====")

if len(invalid_emails) == 0:
    print("No Invalid Emails")
else:
    for email in invalid_emails:
        print(email)

# Domain Report
print("\n===== DOMAIN REPORT =====")

for domain in domain_count:
    print(domain, "->", domain_count[domain], "users")