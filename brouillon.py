import csv
votes = []
votes_recus = {}

with open('eurovision_2022_clean_with_points.csv', newline='',encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for ligne in reader:
        votes.append(dict(ligne))


# supprime un caractère indésirable dans les pays destination
for pos,vote in enumerate(votes):
    votes[pos]['points_to']=vote['points_to'].replace('\xa0','')

for vote in votes:
    if 'points_to' in vote:
        if not vote['points_to'] in votes_recus:
            votes_recus[vote['points_to']]= {}
        try:
            votes_recus[vote['points_to']][vote['points_from']] = int(vote['televote_points'])
        except:
            pass
        try:
            votes_recus[vote['points_to']][vote['points_from']] += int(vote['jury_points'])
        except:
            pass

pays = "Ukraine"
score_pays={}

for pays in votes_recus:
    score_pays[pays] = 0
    for votant in votes_recus[pays]:
        score_pays[pays] += votes_recus[pays][votant]

print(sorted(score_pays.items(),key = lambda t : t[1]))

print("Points donnés à l''Ukraine en fonction du pays :")

resu=sorted(votes_recus["Ukraine"].items(),key = lambda t : t[1])
for pays,points in resu:
    print(f'Pays : {pays}.\t Nb de pts : {points} points')


print("version de 16:56 bordel")
print("version de 16:59 le conflit gagne l'ouest !")
