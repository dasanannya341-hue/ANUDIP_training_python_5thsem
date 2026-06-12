'''Problem 3: E-Commerce Coupon Fraud Detection 
Problem Statement 
A file named coupons.txt contains coupon usage records. 
SAVE50 
WELCOME20 
SAVE50 
FESTIVE10 
SAVE50 
WELCOME20 
NEWUSER 
FESTIVE10 
SAVE50 
NEWUSER 
Tasks 
1. Count the usage frequency of each coupon.  
2. Identify coupons used more than 3 times.  
3. Create a set of unique coupons.  
4. Display the most frequently used coupon.  
5. Save suspicious coupon records into fraud_report.txt.  
Sample Output 
Coupon Usage Frequency: 
SAVE50 : 4 
WELCOME20 : 2 
FESTIVE10 : 2 
NEWUSER : 2 
Suspicious Coupons: 
SAVE50 
Unique Coupons: 
{'SAVE50', 'WELCOME20', 'FESTIVE10', 'NEWUSER'} 
Most Frequently Used Coupon: 
SAVE50 '''

# Problem 3: E-Commerce Coupon Fraud Detection

# Step 1: Create an empty dictionary to store coupon frequencies
coupon_count = {}

try:
    # Step 2: Open the coupons.txt file in read mode
    file = open("ANUDIP_training_python_5thsem/CLASSROOM/PYTHON-CODING CHALLANGE3/coupons.txt", "r")

    # Step 3: Read each coupon from the file
    for line in file:
        coupon = line.strip()

        # 1. Count the usage frequency of each coupon.
        if coupon in coupon_count:
            coupon_count[coupon] += 1
        else:
            coupon_count[coupon] = 1

    # Close the file
    file.close()

    print("Coupon Usage Frequency:")
    for coupon, count in coupon_count.items():
        print(coupon, ":", count)

    # 2. Identify coupons used more than 3 times.
    print("\nSuspicious Coupons:")
    suspicious_coupons = []

    for coupon, count in coupon_count.items():
        if count > 3:
            print(coupon)
            suspicious_coupons.append(coupon)

    # 3. Create a set of unique coupons.
    unique_coupons = set(coupon_count.keys())

    print("\nUnique Coupons:")
    print(unique_coupons)

    # 4. Display the most frequently used coupon.
    max_count = 0
    most_used_coupon = ""

    for coupon, count in coupon_count.items():
        if count > max_count:
            max_count = count
            most_used_coupon = coupon

    print("\nMost Frequently Used Coupon:")
    print(most_used_coupon)

    # 5. Save suspicious coupon records into fraud_report.txt.
    report = open("fraud_report.txt", "w")

    for coupon in suspicious_coupons:
        report.write(coupon + "\n")

    report.close()

    print("\nFraud Report Generated Successfully.")

except FileNotFoundError:
    print("Error: coupons.txt file not found")