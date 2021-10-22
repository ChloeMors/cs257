''' Chloe Morscheck, CS257, 10/14/2021
    This program converts two Kaggle csvs into database csvs of my own design
'''

import csv

'''
Questions: 
How much worse is it to store the strings "gold" "silver" "bronze" than to have a three line database with 0 1 2


"Athlete ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"


For line in csv:
id participatoin int,
from athletes.csv of line [0] - athlete_id int,
from teams.csv - team_id int,
from games.csv - game_id int,
from sports.csv - event_id int,
	line[2] - ath_sex text,
	line[4] - ath_height int,
	line[5] - ath_weight int,
	line[3] - ath_age int,
	line[14] - medal text,


'''
in_file = open('noc_regions.csv')
out_file = open('teams.csv', 'w')
csv_reader = csv.reader(in_file, delimiter=',')
csv_writer = csv.writer(out_file, delimiter=',')
id = 0
first = True
teams = {}
for row in csv_reader:
	if first:
		first = False
	else:
		csv_writer.writerow([id, row[0], row[1]])
		teams[row[0]]=([id, row[0], row[1]])
		id = id + 1

in_file.close()
out_file.close()

in_file = open('athlete_events.csv')
athletes_file = open('athletes.csv', 'w')

csv_reader = csv.reader(in_file, delimiter=',')
athletes_writer = csv.writer(athletes_file, delimiter=',')
id = 1
first = True
for row in csv_reader:
	if first:
		first = False
	else:
		if int(row[0]) == id:
			athletes_writer.writerow([id, row[1]])
			id = id + 1

in_file.close()
athletes_file.close()


in_file = open('athlete_events.csv')
games_file = open('games.csv', 'w')
csv_reader = csv.reader(in_file, delimiter=',')
games_writer = csv.writer(games_file, delimiter=',')
id = 0
first = True
games = {}
for row in csv_reader:
	if first:
		first = False
	else:
		if row[8] not in games.keys():
			games[row[8]]=[id, row[8], row[9], row[10], row[11]]
			games_writer.writerow(games[row[8]])
			id = id + 1

games_file.close()
in_file.close()




in_file = open('athlete_events.csv')
sports_file = open('sports.csv', 'w')
csv_reader = csv.reader(in_file, delimiter=',')
sports_writer = csv.writer(sports_file, delimiter=',')
id = 0
first = True
sports = {}
for row in csv_reader:
	if first: 
		first = False
	else:
		if row[13] not in sports.keys():
			sports[row[13]] = [id, row[12], row[13]]
			sports_writer.writerow(sports[row[13]])
			id = id + 1

sports_file.close()
in_file.close()


participations_file = open('participations.csv', 'w')
participations_writer = csv.writer(participations_file, delimiter=',')
in_file = open('athlete_events.csv')
csv_reader = csv.reader(in_file, delimiter=',')


id = 0
first = True
team_id = -1
game_id = -1
event_id = -1
for row in csv_reader:
	if first:
		first = False
	else:
		team_id = teams[row[7]][0]
		game_id = games[row[8]][0]
		sport_id = sports[row[13]][0]
		participations_writer.writerow([id, row[0], team_id, game_id, sport_id, row[2], row[4], row[5], row[3], row[14]])

in_file.close()
participations_file.close()

