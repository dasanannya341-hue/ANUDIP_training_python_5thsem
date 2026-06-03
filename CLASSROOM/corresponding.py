#program to convert time into corresponding hr min and sec 
#input time in seconds
time = int(input("Enter time in seconds: "))
#calculate hours, minutes and seconds
if(time < 0):
    print("Time cannot be negative")
    print("Please enter a valid time in seconds")
    hour = 0
    minute = 0
    #converting number of seconds into hours
    if(time >= 3600):
        hour = time//3600
        time = time%3600
    #converting number of seconds into minutes
    if(time >= 60):
        minute = time//60
        time = time%60
    #remaining seconds
    second = time
    print("Time in hours, minutes and seconds is:", hour, "hours", minute, "minutes", second, "seconds")