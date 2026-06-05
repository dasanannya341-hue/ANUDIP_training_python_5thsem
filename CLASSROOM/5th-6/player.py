#player score
player_score = []
#input of score from user
for i in range(11):
    score = int(input("enter the player score {}: ".format(i+1)))
    player_score.append(score)
#display the player score
print("\n ------- player score -------")
print("score of 11 players: ", player_score)
#find the highest score
highest_score = player_score[0]
for index in range(1, len(player_score)):
    if player_score[index] > highest_score:
        highest_score = player_score[index]
print("highest score is: ", highest_score)
