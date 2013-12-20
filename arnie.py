#!/bin/python
import csv
import operator
from scipy import stats
from numpy import *

killWeapon = {}
killYear = {}

Years = [1969, 1977, 1982, 1984, 1985, 1986, 1987, 1988, 1990, 1991, 1993, 1994, 1996, 1997, 1999, 2000, 2002, 2003, 2012, 2013]

gunKills = {}
stKills  = {}
bombsKills  = {}
swordsKills  = {}
drivingKills = {}

def constructor(b):
    for x in Years:
        if (not x in b):
            b[x] = 0

def CreateDicts():
    constructor(killYear)
    constructor(gunKills)
    constructor(stKills)
    constructor(bombsKills)
    constructor(swordsKills)
    constructor(drivingKills)

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

        # air-gun, guns, freezegun, laser-gun
        if(method.find('gun') != -1):
            if(not year in gunKills):
                gunKills[year] = 0
            gunKills[year] += kills

        if(method.find('driving') != -1):
            if(not year in drivingKills):
                drivingKills[year] = 0
            drivingKills[year] += kills
            
        # hand combat
        items = ['strength', 'projectiles', 'crowbar', 'boulders', 'teeth']
        for x in items:
            if(method.find(x) != -1):
                if(not year in stKills):
                    stKills[year] = 0
                stKills[year] += kills
                
        # explosions
        items = ['bomb', 'missile', 'flame-thrower']
        for x in items:
            if(method.find(x) != -1):
                if(not year in bombsKills):
                    bombsKills[year] = 0
                bombsKills[year] += kills

        # knives
        items = ['knives', 'swords']
        for x in items:
            if(method.find(x) != -1):
                if(not year in swordsKills):
                    swordsKills[year] = 0
                swordsKills[year] += kills
                            

    return totKills

if __name__ == "__main__":
    CreateDicts()
    kills = main()
    print "Total kills: ",kills
    # print swordsKills
    
    writeLogs ("_year.log",     sorted(killYear.items()))
    writeLogs ("_weapon.log",   sorted(killWeapon.iteritems(), key=operator.itemgetter(1)))

    writeLogs ("_sk_guns.log",      sorted(gunKills.items()))
    writeLogs ("_sk_strength.log",  sorted(stKills.items()))
    writeLogs ("_sk_bombs.log",     sorted(bombsKills.items()))
    writeLogs ("_sk_driving.log",   sorted(drivingKills.items()))
    writeLogs ("_sk_swords.log",    sorted(swordsKills.items()))
    
    
    