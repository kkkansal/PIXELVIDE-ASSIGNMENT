num_teams = 24
england = ['Arsenal','Man.City','Man. United','BATE']
france = ['Atletico','Real Madrid','Sevilla','Valencia']
spain = ['Leverkusen','wolfsburg','Monchengladbach']
germany = ['Roma']
italy = ['Lyon','Porto']
portugal = ['Shakhtar Donetsk','Dynamo Kyiv']
russia = ['CSKA Moskva']
dutch = ['Astana']
turkey = ['Malmo']
swiss = ['Dinamo Zagreb']
scotland = ['Galatasaray']
greece = ['Gent']
poland = ['Olympiacos']
belgium = ['M.Tel-Aviv']

groupA = []
groupB = []
groupC = []
groupD = []
groupE = []
groupF = []
groupG = []
groupH = []
groups = [groupA, groupB, groupC, groupD, groupE, groupF, groupG, groupH]
countries1 = [england, france, spain, germany, italy, portugal, russia]
countries2 = [dutch, turkey, swiss, scotland, greece, poland, belgium]
used = []
loading = 0
tens = 10


england1 = england[:]
france1 = france[:]
spain1 = spain[:]
germany1 = germany[:]
italy1 = italy[:]
portugal1 = portugal[:]
russia1 = russia[:]
dutch1 = dutch[:]
turkey1 = turkey[:]
swiss1 = swiss[:]
scotland1 = scotland[:]
greece1 = greece[:]
poland1 = poland[:]
belgium1 = belgium[:]

countries3 = [england1, france1, spain1, germany1, italy1, portugal1, russia1]
countries4 = [dutch1, turkey1, swiss1, scotland1, greece1, poland1, belgium1]

# create groups
import random
while num_teams != 7:
    x = 0
    position = random.randrange(len(countries1))
    country = countries1[position]
    country1 = countries3[position]
    if country1:
        team = random.choice(country1)
        if team not in used:
            group = random.choice(groups)
            if len(group) < 3:
                for i in group:
                    if i not in country:
                        x += 0
                    else:
                        x += 1
                if x == 0:
                    group += [team]
                    num_teams -= 1
                    used += [team]
                    country1.remove(team)
                    loading += 1
                    if loading == tens:
                        print("\nLoading...\n")
                        tens += 10
while num_teams != 0:
    x = 0
    position = random.randrange(len(countries2))
    country = countries2[position]
    country1 = countries4[position]
    if country1:
        team = random.choice(country1)
        if team not in used:
            group = random.choice(groups)
            if len(group) < 3:
                for i in group:
                    if i not in country:
                        x += 0
                    else:
                        x += 1
                if x == 0:
                    group += [team]
                    num_teams -= 1
                    used += [team]
                    country1.remove(team)
                    loading += 1
                    if loading == tens:
                        print("\nLoading...\n")
                        tens += 10
from random import choice
Teams=['Barcelona','Bayern','Benfica','Chelsea', 'Juventus','Paris','PSV','zenit']
while len(Teams)>0:
    GroupA1=choice(Teams)
    groupA.append(GroupA1)
    Teams.remove(GroupA1)
    
    GroupB1=choice(Teams)
    groupB.append(GroupB1)
    Teams.remove(GroupB1)
    
    Groupc1=choice(Teams)
    groupC.append(Groupc1)
    Teams.remove(Groupc1)
    
    Groupd1=choice(Teams)
    groupD.append(Groupd1)
    Teams.remove(Groupd1)
    
    Groupe1=choice(Teams)
    groupE.append(Groupe1)
    Teams.remove(Groupe1)
    
    Groupf1=choice(Teams)
    groupF.append(Groupf1)
    Teams.remove(Groupf1)
    
    Groupg1=choice(Teams)
    groupG.append(Groupg1)
    Teams.remove(Groupg1)
    
    Grouph1=choice(Teams)
    groupH.append(Grouph1)
    Teams.remove(Grouph1)

groupA=list(reversed(groupA))
groupB=list(reversed(groupB))
groupC=list(reversed(groupC))
groupD=list(reversed(groupD))
groupE=list(reversed(groupE))
groupF=list(reversed(groupF))
groupG=list(reversed(groupG))
groupH=list(reversed(groupH))

# display groups


print("\nGroup A")
print(groupA[0])
print(groupA[1])
print(groupA[2])
print(groupA[3])

print("\nGroup B")
print(groupB[0])
print(groupB[1])
print(groupB[2])
print(groupB[3])

print("\nGroup C")
print(groupC[0])
print(groupC[1])
print(groupC[2])
print(groupC[3])

print("\nGroup D")
print(groupD[0])
print(groupD[1])
print(groupD[2])
print(groupD[3])

print("\nGroup E")
print(groupE[0])
print(groupE[1])
print(groupE[2])
print(groupE[3])

print("\nGroup F")
print(groupF[0])
print(groupF[1])
print(groupF[2])
print(groupF[3])

print("\nGroup G")
print(groupG[0])
print(groupG[1])
print(groupG[2])
print(groupG[3])

print("\nGroup H")
print(groupH[0])
print(groupH[1])
print(groupH[2])
print(groupH[3])

