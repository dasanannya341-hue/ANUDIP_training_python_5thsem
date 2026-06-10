'''Mini Assignment: String in Python 
Assignment 1: Password Security Analyzer 
Problem Statement 
A cybersecurity company wants to analyze user passwords before allowing account creation. 
The system should accept at least 15 passwords and generate a security report. 
Requirements 
For each password: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Check minimum length (8 characters).  
6. Check if spaces exist.  
7. Determine password strength:  
o Strong  
o Medium  
o Weak  
8. Display repeated characters.  
9. Count vowels and consonants.  
10. Identify the most frequently occurring character.  
Challenge 
Generate a report showing: 
Total Passwords Analyzed 
Strong Passwords 
Medium Passwords 
Weak Passwords '''

# Password Security Analyzer

strong_count = 0
medium_count = 0
weak_count = 0

# Analyze 15 passwords
for i in range(1, 16):

    print("\nPassword", i)
    password = input("Enter Password: ")

    upper = 0
    lower = 0
    digits = 0
    special = 0
    vowels = 0
    consonants = 0

    # Count character types
    for ch in password:

        if ch.isupper():
            upper += 1

        elif ch.islower():
            lower += 1

            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

        elif ch.isdigit():
            digits += 1

        else:
            special += 1

    # Check length
    if len(password) >= 8:
        print("Minimum Length Check : Passed")
    else:
        print("Minimum Length Check : Failed")

    # Check spaces
    if " " in password:
        print("Spaces Exist : Yes")
    else:
        print("Spaces Exist : No")

    # Password strength
    if len(password) >= 8 and upper > 0 and lower > 0 and digits > 0 and special > 0:
        strength = "Strong"
        strong_count += 1

    elif len(password) >= 8 and (upper > 0 or lower > 0) and digits > 0:
        strength = "Medium"
        medium_count += 1

    else:
        strength = "Weak"
        weak_count += 1

    # Repeated characters
    repeated = []

    for ch in password:
        if password.count(ch) > 1 and ch not in repeated:
            repeated.append(ch)

    # Most frequent character
    max_char = ""
    max_count = 0

    for ch in password:
        if password.count(ch) > max_count:
            max_count = password.count(ch)
            max_char = ch

    # Display report for current password
    print("\n--- Password Report ---")
    print("Uppercase Letters :", upper)
    print("Lowercase Letters :", lower)
    print("Digits :", digits)
    print("Special Characters :", special)
    print("Vowels :", vowels)
    print("Consonants :", consonants)
    print("Password Strength :", strength)

    print("Repeated Characters :", repeated)

    print("Most Frequent Character :", max_char)
    print("Frequency :", max_count)

# Final Summary Report
print("\n========== SECURITY REPORT ==========")
print("Total Passwords Analyzed :", 15)
print("Strong Passwords :", strong_count)
print("Medium Passwords :", medium_count)
print("Weak Passwords :", weak_count)