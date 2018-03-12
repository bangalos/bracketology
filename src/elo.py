# Python 3 program for Elo Rating
# It accepts two input files
# 1. Initial list of teams and their ratings
# 2. List of games and results
#
# It prints the output of team and their ratings to terminal
 
import math
import sys
import csv
 
# Function to calculate the Probability
def Probability(rating1, rating2):
 
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))
 
 
# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B. 
def EloRating(Ra, Rb, K, d):
    # To calculate the Winning Probability of Player B
    Pb = Probability(Ra, Rb)
 
    # To calculate the Winning Probability of Player A
    Pa = Probability(Rb, Ra)
 
    # Case 1: When Player A wins:  Updating the Elo Ratings
    if (d == 1) :
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)
     
    # Case 2: When Player B wins: Updating the Elo Ratings
    else :
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)
     
    print("Updated Ratings:-")
    print("Ra =", round(Ra, 6)," Rb =", round(Rb, 6))
 
def elo_delta(Ra, Rb, d):
    K = 100
    Pb = Probability(Ra, Rb)
    Pa = Probability(Rb, Ra)
    if (d == 1) :
        delta = K * (1 - Pa)
        return int(round(delta))
    else:
        delta = K * (0 - Pa)
        return round(delta, 6)

# Driver code
initial_rating_file = sys.argv[1]
game_results_file = sys.argv[2]

team_rating = {}

#First read the initial rating file
with open(initial_rating_file, "r") as irf:
    reader = csv.reader(irf, delimiter="\t")
    for i, line in enumerate(reader):
        team_rating[str(line[0])] = int(line[1])

#Then Read the games and results
#Then calculate the new ELO and publish them
with open(game_results_file, "r") as grf:
    reader = csv.reader(grf, delimiter="\t")
    for i, line in enumerate(reader):
        team_1 = str(line[0])
        team_2 = str(line[1])
        result = int(line[2])
        elo_1 = team_rating[team_1]
        elo_2 = team_rating[team_2]
        delta = elo_delta (elo_1, elo_2, result)
        team_rating[team_1] = team_rating[team_1] + delta
        team_rating[team_2] = team_rating[team_2] - delta

for key,val in team_rating.items():
    print '{}\t{}'.format(key,val)
