'''
Chloe Morcheck, October 21, 2021
olympics.py, a command line interface for using with an olympics database
'''

import argparse
import psycopg2

# psycopg2 starter code taken from psycopg2-sample.py
from config import password
from config import database
from config import user

def get_parsed_arguments():
    ''' Create an ArgumentParser object and fill it with information about command lines 
        utilized by this program arguments.
    '''
    parser = argparse.ArgumentParser(add_help=False, description="Search and sort books and authors.")
    parser.add_argument("-n", "--nocs", action = "store_true", dest="nocs") 
    parser.add_argument("-a", "--athletes", nargs=1) 
    parser.add_argument("-h", "--help", action = "store_true", dest="help")
    parser.add_argument("-s", "--sports", action = "store_true", dest="sports")
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    arguments = get_parsed_arguments()
    if arguments.help:
        f = open("usage.txt", "r")
        file_contents = f.read()
        print(file_contents)
        f.close

    # psycopg2 starter code taken from psycopg2-sample.py
    # Connect to the database
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        # The following line is not in this section of code in the lab
        # it works here, but I'm not sure if this is the best place to put it
        cursor = connection.cursor()
    except Exception as e:
        print(e)
        exit()

    if arguments.nocs:
        # List all the NOCs and the number of gold medals they have won, 
        # in decreasing order of the number of gold medals.
        query = '''SELECT teams.NOC, COUNT(participations.medal)
                    FROM teams, participations
                    WHERE participations.medal = 'Gold'
                    AND teams.id = participations.team_id
                    GROUP BY teams.NOC
                    ORDER BY COUNT(participations.medal) DESC;'''
        try:
            cursor.execute(query)
        except Exception as e:
            print(e)
            exit()

        print('===== NOCS and Gold medals =====')
        for row in cursor:
            print(row[0], row[1])
        print()

    if arguments.athletes:
        # List the names of all the athletes from a specified NOC. 
        query = '''SELECT DISTINCT athletes.athlete_name
                    FROM athletes, participations, teams
                    WHERE athletes.id = participations.athlete_id
                    AND participations.team_id = teams.id
                    AND teams.NOC = %s
                    ORDER BY athletes.athlete_name;'''
        search_string = arguments.athletes[0]
        try:
            cursor.execute(query, (search_string,))
        except Exception as e:
            print(e)
            exit()

        print('===== Athletes from {0} ====='.format(search_string))
        for row in cursor:
            print(row[0])
        print()
        

    if arguments.sports:
        # Prints all sports and how many participations they have, descending
        query = '''SELECT sports.athletic_event, COUNT(participations.id)
                    FROM sports, participations
                    WHERE sports.id = participations.event_id
                    GROUP BY sports.athletic_event
                    ORDER BY COUNT(participations.medal) DESC;'''
        try:
            cursor.execute(query)
        except Exception as e:
            print(e)
            exit()

        print('===== Participations per Sport =====')
        for row in cursor:
            print(row[0], row[1])
        print()

    connection.close()


if __name__ == "__main__":
    main()