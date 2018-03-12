#Program for assigning initial rating
import csv
import sys

filename = sys.argv[1]
with open(filename, "r") as fp:
    reader = csv.reader(fp, delimiter="\t")
    for i, line in enumerate(reader):
        rating = 2000 - 5*int(line[1])
        print '{}\t{}'.format(line[0], str(rating))
