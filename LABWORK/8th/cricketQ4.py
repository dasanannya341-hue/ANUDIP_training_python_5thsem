'''Runs scored by players in a tournament: 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks Problem Statement 
Runs scored by players in a tournament: 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks 
1. Display players scoring more than 500 runs.  
2. Find the Orange Cap winner.  
3. Find the lowest scorer.  
4. Calculate total runs scored.  
5. Create a list of players scoring below 400.  
6. Count players scoring between 400 and 600 runs.  
Sample Output 
Players Scoring More Than 500 Runs: 
Virat 
Rohit 
Gill 
Pant 
 
Orange Cap Winner: Gill (698) 
 
Lowest Scorer: Hardik (278) 
 
Total Tournament Runs: 4657 
 
Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja'] 
 
Players Between 400 and 600 Runs: 5 '''


runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")
for player in runs:
    if runs[player] > 500:
        print(player)

# 2. Orange Cap Winner
highest_runs = 0
winner = ""

for player in runs:
    if runs[player] > highest_runs:
        highest_runs = runs[player]
        winner = player

print("\nOrange Cap Winner:")
print(winner, "(", highest_runs, ")", sep="")

# 3. Lowest Scorer
lowest_runs = 1000
lowest_player = ""

for player in runs:
    if runs[player] < lowest_runs:
        lowest_runs = runs[player]
        lowest_player = player

print("\nLowest Scorer:")
print(lowest_player, "(", lowest_runs, ")", sep="")

# 4. Total Runs
total = 0

for player in runs:
    total += runs[player]

print("\nTotal Tournament Runs:", total)

# 5. Players below 400
below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400:")
print(below_400)

# 6. Count players between 400 and 600
count = 0

for player in runs:
    if 400 <= runs[player] <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs:", count)