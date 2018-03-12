# bracketology
Aim of this project is to calculate the NCAA 68 teams and the Brackets.

If we can assign an ELO rating to each team, then we will be able rank the 68 teams. So, our aim is to assign an ELO rating to each team.

Elo Ratings are going to be more accurate if it starts with something that is more accurate. So, we will begin with an initial assignment of ELO ratings based on 2015 results. Then, we will run the ELO program for 2016, to obtain initial ELO Rating for 2017. Then, we will run the 2017 games through the ELO rating program to get the current ratings.

#1. Initital Rating Assignment
Initial rating will be 2000 - (rank*5)
The input file will have two columns - rank and team name.
The output file will have two columns - team name and rating.

#2. New Ratings Based on Games Results of 2016.
The input is going to be the games and results in 3 columns. Team 1 name, Team 2 name and result.
The output is going to be two columns - team name and rating.

#3. New Ratings Based on Games Results of 2017.
Same as above.

----------
So, the first task is to figure out the input files from external sources.
1. 2015 ranking for the teams.
2. 2016 results
3. 2017 results.
