'''. Cricket Tournament Analytics System 
Problem Statement 
Store statistics of at least 30 cricket players. 
Example Structure 
players = { 
    "Virat": { 
        "runs": 645, 
        "matches": 12, 
        "wickets": 0 
    } 
} 
Requirements 
1. Display all player statistics.  
2. Find highest run scorer.  
3. Find lowest run scorer.  
4. Calculate average runs.  
5. Find player with maximum wickets.  
6. Find all-rounders (runs > 300 and wickets > 5).  
7. Display players scoring above average.  
8. Create categories:  
o Star Performer  
o Good Performer  
o Average Performer  
o Poor Performer  
9. Generate team statistics.  
10. Display top 5 batsmen.  
11. Display top 5 bowlers.  
12. Create a separate dictionary for award winners.  
Challenge 
Generate a tournament report '''

# Cricket Tournament Analytics System

players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 580, "matches": 12, "wickets": 1},
    "Gill": {"runs": 698, "matches": 12, "wickets": 0},
    "Rahul": {"runs": 435, "matches": 11, "wickets": 0},
    "Hardik": {"runs": 278, "matches": 10, "wickets": 8},
    "Jadeja": {"runs": 301, "matches": 12, "wickets": 12},
    "Surya": {"runs": 389, "matches": 11, "wickets": 0},
    "Pant": {"runs": 534, "matches": 12, "wickets": 0},
    "Kuldeep": {"runs": 45, "matches": 12, "wickets": 15},
    "Bumrah": {"runs": 25, "matches": 12, "wickets": 18}
}

while True:

    print("\n===== CRICKET TOURNAMENT ANALYTICS =====")
    print("1. Display All Players")
    print("2. Highest Run Scorer")
    print("3. Lowest Run Scorer")
    print("4. Average Runs")
    print("5. Maximum Wickets")
    print("6. All Rounders")
    print("7. Players Above Average")
    print("8. Performance Categories")
    print("9. Team Statistics")
    print("10. Top 5 Batsmen")
    print("11. Top 5 Bowlers")
    print("12. Award Winners")
    print("13. Tournament Report")
    print("14. Exit")

    choice = int(input("Enter Choice : "))

    # --------------------------------------------------
    # Display all player statistics

    if choice == 1:

        dict_items = list(players.items())

        for item in dict_items:
            print(item[0], ":", item[1])

    # --------------------------------------------------
    # Highest run scorer

    elif choice == 2:

        dict_items = list(players.items())

        top_player = dict_items[0][0]
        top_runs = dict_items[0][1]["runs"]

        for item in dict_items:

            if item[1]["runs"] > top_runs:

                top_runs = item[1]["runs"]
                top_player = item[0]

        print("\nHighest Run Scorer")
        print(top_player, "-", top_runs)

    # --------------------------------------------------
    # Lowest run scorer

    elif choice == 3:

        dict_items = list(players.items())

        low_player = dict_items[0][0]
        low_runs = dict_items[0][1]["runs"]

        for item in dict_items:

            if item[1]["runs"] < low_runs:

                low_runs = item[1]["runs"]
                low_player = item[0]

        print("\nLowest Run Scorer")
        print(low_player, "-", low_runs)

    # --------------------------------------------------
    # Average runs

    elif choice == 4:

        total_runs = 0

        dict_items = list(players.items())

        for item in dict_items:
            total_runs += item[1]["runs"]

        average_runs = total_runs / len(players)

        print("Average Runs :", average_runs)

    # --------------------------------------------------
    # Maximum wickets

    elif choice == 5:

        dict_items = list(players.items())

        best_bowler = dict_items[0][0]
        max_wickets = dict_items[0][1]["wickets"]

        for item in dict_items:

            if item[1]["wickets"] > max_wickets:

                max_wickets = item[1]["wickets"]
                best_bowler = item[0]

        print("Best Bowler :", best_bowler)

    # --------------------------------------------------
    # All rounders

    elif choice == 6:

        print("\nAll Rounders")

        dict_items = list(players.items())

        for item in dict_items:

            if item[1]["runs"] > 300 and item[1]["wickets"] > 5:

                print(item[0])

    # --------------------------------------------------
    # Players above average

    elif choice == 7:

        total_runs = 0

        dict_items = list(players.items())

        for item in dict_items:
            total_runs += item[1]["runs"]

        average_runs = total_runs / len(players)

        print("\nPlayers Above Average")

        for item in dict_items:

            if item[1]["runs"] > average_runs:
                print(item[0])

    # --------------------------------------------------
    # Performance categories

    elif choice == 8:

        star = []
        good = []
        average = []
        poor = []

        dict_items = list(players.items())

        for item in dict_items:

            if item[1]["runs"] >= 600:
                star.append(item[0])

            elif item[1]["runs"] >= 400:
                good.append(item[0])

            elif item[1]["runs"] >= 200:
                average.append(item[0])

            else:
                poor.append(item[0])

        print("\nStar Performer :", star)
        print("Good Performer :", good)
        print("Average Performer :", average)
        print("Poor Performer :", poor)

    # --------------------------------------------------
    # Team statistics

    elif choice == 9:

        total_runs = 0
        total_wickets = 0

        dict_items = list(players.items())

        for item in dict_items:

            total_runs += item[1]["runs"]
            total_wickets += item[1]["wickets"]

        print("\nTeam Statistics")
        print("Total Runs :", total_runs)
        print("Total Wickets :", total_wickets)

    # --------------------------------------------------
    # Top 5 batsmen

    elif choice == 10:

        print("\nTop 5 Batsmen")

        temp = players.copy()

        for i in range(5):

            dict_items = list(temp.items())

            top_player = dict_items[0][0]
            top_runs = dict_items[0][1]["runs"]

            for item in dict_items:

                if item[1]["runs"] > top_runs:

                    top_runs = item[1]["runs"]
                    top_player = item[0]

            print(top_player, "-", top_runs)

            del temp[top_player]

    # --------------------------------------------------
    # Top 5 bowlers

    elif choice == 11:

        print("\nTop 5 Bowlers")

        temp = players.copy()

        for i in range(5):

            dict_items = list(temp.items())

            best_bowler = dict_items[0][0]
            max_wickets = dict_items[0][1]["wickets"]

            for item in dict_items:

                if item[1]["wickets"] > max_wickets:

                    max_wickets = item[1]["wickets"]
                    best_bowler = item[0]

            print(best_bowler, "-", max_wickets)

            del temp[best_bowler]

    # --------------------------------------------------
    # Award winners dictionary

    elif choice == 12:

        awards = {}

        dict_items = list(players.items())

        for item in dict_items:

            if item[1]["runs"] > 500:

                awards[item[0]] = item[1]

        print("\nAward Winners")
        print(awards)

    # --------------------------------------------------
    # Tournament report

    elif choice == 13:

        total_runs = 0
        total_wickets = 0

        dict_items = list(players.items())

        for item in dict_items:

            total_runs += item[1]["runs"]
            total_wickets += item[1]["wickets"]

        print("\n===== TOURNAMENT REPORT =====")
        print("Total Players :", len(players))
        print("Total Runs :", total_runs)
        print("Total Wickets :", total_wickets)

    # --------------------------------------------------
    # Exit

    elif choice == 14:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")