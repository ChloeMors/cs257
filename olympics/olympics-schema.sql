CREATE TABLE teams(
    id int,
    NOC text,
    team text
);

CREATE TABLE athletes(
    id int,
    athlete_name text
);

CREATE TABLE games(
    id int,
    game_string text,
    game_year int,
    season text,
    city text
);

CREATE TABLE sports(
    id int,
    athletic_event text,
    sport text
);

CREATE TABLE participations(
    id int,
    athlete_id int,
    team_id int,
    game_id int,
	event_id int,
	ath_sex text,
	ath_height text,
	ath_weight text,
	ath_age text,
	medal text
);

