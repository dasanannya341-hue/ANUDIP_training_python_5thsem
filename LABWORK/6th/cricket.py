'''A batsman's scores in different matches are stored in a list. 
scores = [45, 78, 12, 100, 67, 8, 90, 55] 
Write a program to: 
• Count half-centuries and centuries.  
• Find the highest score.  
• Display all scores below 20.  
• Calculate the average score.  '''

score = [45,75,12,100,67,8,90,55]

#Count half-centuries and centuries.  
print("count half-centuries")
count_half_centuries = 0
count_centuries = 0
for item in score:
    if item >= 50 and item < 100:
        count_half_centuries += 1
    elif item >= 100:
        count_centuries += 1

print(f"Half-centuries: {count_half_centuries}")
print(f"Centuries: {count_centuries}")

# Find the highest score
print("\nHighest score:")
highest_score = max(score)
print(f"Highest score: {highest_score}")

# Display all scores below 20
print("\nScores below 20:")

for item in score:
    if item <= 20:
        print(item)

# Calculate the average score
print("\nAverage score:")
average_score = sum(score) / len(score)
print(f"Average score: {average_score:.2f}")