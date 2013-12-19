#!/bin/python
import csv
import operator
from scipy import stats
from numpy import *

killWeapon = {}
killMovie = {}
killYear = {}

def writeLogs (fname, d):
    writer = csv.writer(open(fname, 'wb'), delimiter='\t')
    for r in d:
        writer.writerow([r[0], r[1]])



def main():
    totKills = 0
    reader = csv.reader(open("killstats.txt","rb"), delimiter='\t')
    for row in reader:
        # print row
        '''
            "name of the movie"    year    kills    method   
        '''
        movie = row[0]
        year = int(row[1])
        kills = int(row[2])
        method = row[3]
        totKills += kills

        if(not year in killYear):
            killYear[year] = 0
        killYear[year] += kills
        if(not method in killWeapon):
            killWeapon[method] = 0
        killWeapon[method] += kills
    return totKills

if __name__ == "__main__":
    kills = main()
    print "Total kills: ",kills
    
    writeLogs ("_year.txt", sorted(killYear.items()))
    writeLogs ("_weapon.txt", sorted(killWeapon.iteritems(), key=operator.itemgetter(1)))
    