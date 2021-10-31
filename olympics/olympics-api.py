'''
    olympics-api.py
    Chloe Morscheck, 28 October 2021
    An api for working with the olympics database
    Modified from Jeff's flask-sample.py
'''
import sys
import argparse
import flask
import json
import psycopg2

from config import password
from config import database
from config import user

app = flask.Flask(__name__)
try:
    connection = psycopg2.connect(database=database, user=user, password=password)
    cursor = connection.cursor()
except Exception as e:
    print(e)
    exit()

@app.route('/')
def hello():
    return 'Hello, Citizen of CS257.'

@app.route('/games')
def get_games():
    '''
    RESPONSE: a JSON list of dictionaries, each of which represents one
    Olympic games, sorted by year. Each dictionary in this list will have
    the following fields.

   id -- (INTEGER) a unique identifier for the games in question
   year -- (INTEGER) the 4-digit year in which the games were held (e.g. 1992)
   season -- (TEXT) the season of the games (either "Summer" or "Winter")
   city -- (TEXT) the host city (e.g. "Barcelona")
    '''
    query = '''SELECT games.id, games.game_year, games.season, games.city
                FROM games
                ORDER BY games.game_year ASC
            '''
    try:
        cursor.execute(query)
    except Exception as e: 
        print(e)
        exit()
    games = []
    for row in cursor:
        game = {'id': row[0], 'year': row[1], 'season': row[2], 'city': row[3]}
        games.append(game)
    
    return json.dumps(games)

@app.route('/nocs')
def get_nocs():
    '''
    RESPONSE: a JSON list of dictionaries, each of which represents one
    National Olympic Committee, alphabetized by NOC abbreviation. Each dictionary
    in this list will have the following fields.

   abbreviation -- (TEXT) the NOC's abbreviation (e.g. "USA", "MEX", "CAN", etc.)
   name -- (TEXT) the NOC's full name (see the noc_regions.csv file)

    '''
    query = '''SELECT teams.NOC, teams.team
                FROM teams
                ORDER BY teams.NOC
            '''
    try:
        cursor.execute(query)
    except Exception as e: 
        print(e)
        exit()
    nocs = []
    for row in cursor:
        noc = {'abbreviation': row[0], 'name': row[1]}
        nocs.append(noc)
    
    return json.dumps(nocs)

@app.route('/medalists/games/<games_id>')
def get_medalists(games_id):
    '''
    RESPONSE: a JSON list of dictionaries, each representing one athlete
    who earned a medal in the specified games. Each dictionary will have the
    following fields.

   athlete_id -- (INTEGER) a unique identifier for the athlete
   athlete_name -- (TEXT) the athlete's full name
   athlete_sex -- (TEXT) the athlete's sex as specified in the database ("F" or "M")
   sport -- (TEXT) the name of the sport in which the medal was earned
   event -- (TEXT) the name of the event in which the medal was earned
   medal -- (TEXT) the type of medal ("gold", "silver", or "bronze")

    If the GET parameter noc=noc_abbreviation is present, this endpoint will return
    only those medalists who were on the specified NOC's team during the specified
    games.

    The <games_id> is whatever string (digits or otherwise) that your database/API
    uses to uniquely identify an Olympic games.
    '''
    query = '''SELECT participations.athlete_id, athletes.athlete_name, participations.ath_sex, sports.sport, sports.athletic_event, participations.medal, teams.NOC
                FROM participations, athletes, sports, teams
                WHERE participations.game_id = %s
                AND participations.athlete_id = athletes.id
                AND participations.event_id = sports.id
                AND participations.team_id = teams.id
            '''
    search_string = games_id
    try:
        cursor.execute(query, (search_string,))
    except Exception as e: 
        print(e)
        exit()
    participations = []
    noc = flask.request.args.get('noc')
    for row in cursor:
        participation = {'athlete_id': row[0], 'athlete_name': row[1], 'athlete_sex': row[2], 'sport': row[3], 'event': row[4], 'medal': row[5]}
        participation_noc = row[6].lower()
        if participation['medal'] == 'NA':
            continue
        if noc:
            if noc.lower() == participation_noc:
                participations.append(participation)
        else:
            participations.append(participation)
    
    return json.dumps(participations)

@app.route('/help')
def get_help():
    # -> change help.html
    return flask.render_template('help.html')

# Main code modeled after Jeff's Flask sample API
if __name__ == '__main__':
    parser = argparse.ArgumentParser('An Flask API for the olympics database')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)