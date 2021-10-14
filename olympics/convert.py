''' Chloe Morscheck, CS257, 10/14/2021
    This program converts two Kaggle csvs into database csvs of my own design
'''


'''
Questions: 
How much worse is it to store the strings "gold" "silver" "bronze" than to have a three line database with 0 1 2
For lines 2-end of noc regiions cvs 
    [NOC][Team][Notes] -> [id][NOC][Team] make into teams.csv

For lines 2-end of athlete events

"Athlete ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"

For individual [0][1] combos: Make into athletes.csv [0][1]

FOr individual [8][9][10]: make into games.csv [id][8][9][10]

For individual [12][13]: make into sports.csv [id][12][13]

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