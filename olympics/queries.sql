SELECT teams.NOC 
FROM teams
ORDER BY teams.NOC;

SELECT DISTINCT athletes.athlete_name
FROM athletes, participations, teams
WHERE athletes.id = participations.athlete_id
AND participations.team_id = teams.id
AND teams.team = 'Kenya'
ORDER BY athletes.athlete_name;

SELECT games.game_string, sports.sport, participations.medal
FROM participations, athletes, games, sports
WHERE participations.athlete_id = athletes.id
AND participations.game_id = games.id
AND participations.event_id = sports.id
AND athletes.athlete_name = 'Gregory Efthimios "Greg" Louganis'
ORDER BY games.game_year;

SELECT teams.NOC, COUNT(participations.medal)
FROM teams, participations
WHERE participations.medal = 'Gold'
AND teams.id = participations.team_id
GROUP BY teams.NOC
ORDER BY COUNT(participations.medal) DESC;