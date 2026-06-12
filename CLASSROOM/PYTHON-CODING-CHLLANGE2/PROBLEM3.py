'''Problem 3: Food Delivery Performance Dashboard 
Problem Statement 
Delivery times (in minutes) for different orders are recorded below: 
Sample Data 
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Tasks 
1. Find the fastest delivery time.  
2. Find the slowest delivery time.  
3. Calculate the average delivery time.  
4. Display delayed orders (>45 minutes).  
5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes)  
Sample Output 
Fastest Delivery: 18 minutes 
 
Slowest Delivery: 80 minutes 
 
Average Delivery Time: 40.8 minutes 
 
Delayed Orders: 
[60, 80, 55] 
 
Fast Deliveries: 4 
Normal Deliveries: 3 
Delayed Deliveries: 3'''

delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 

#Find the fastest delivery time.
fast=min(delivery_times)
print("the fast delivery time :",fast , "min")

#2. Find the slowest delivery time. 
slow=max(delivery_times)
print("the slowest delevary : ",slow,"min")

#3.Calculate the average delivery time.  
total = 0
for i in delivery_times:
    total += i
average = total / len(delivery_times)
print("time Average:", average)

#4. Display delayed orders (>45 minutes)
print("Delayed Orders:")
delayed_order=[]
for time in delivery_times:
    if time > 45:
        delayed_order.append(time)
print(delayed_order)

'''Fast Deliveries: 4 
Normal Deliveries: 3 
Delayed Deliveries: 3'''

fast = 0
normal = 0
delayed = 0

for time in delayed_order:
    if time <= 30:
        fast = fast + 1
    elif time <= 45 and time>=31 :
        normal = normal + 1
    else:
        delayed = delayed + 1

print("Fast Deliveries:", fast)
print("Normal Deliveries:", normal)
print("Delayed Deliveries:", delayed)

