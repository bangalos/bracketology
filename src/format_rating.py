import sys
import csv

elo_file = sys.argv[1]
index_file = sys.argv[2]

team_rating = {}

#First read the initial rating file
with open(elo_file, "r") as irf:
    reader = csv.reader(irf, delimiter="\t")
    for i, line in enumerate(reader):
        team_rating[str(line[0])] = int(line[1])

with open(index_file, "r") as indexf:
    reader = csv.reader(indexf, delimiter="\t")
    for i, line in enumerate(reader):
        print '{}\t{}'.format(str(line[1]), team_rating[str(line[0])])

