import os

__CURRENT_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.abspath(os.path.join(__CURRENT_FILE_PATH, '..'))
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MATCH_STRUCTURE = ('SeasonYear', 'MatchNumber', 'Month', 'Date', 'home_team', 'away_team', 'home_team_goal', 'away_team_goal')
RESOURCE_TO_YEAR_ENGLAND = {"http://www.soccerstats.com/results.asp?league=england" : 2017, 
                    "http://www.soccerstats.com/results.asp?league=england_2016" : 2016,
                    "http://www.soccerstats.com/results.asp?league=england_2015" : 2015}
MATCH_NUMBER_LIMIT = 760
SOCCER_STATS_TEAMS = {1 : 'Chelsea',
                      2 : 'Tottenham',
                      3 : 'Manchester City',
                      4 : 'Arsenal',
                      5 : 'Liverpool',
                      6 : 'Manchester Utd',
                      7 : 'Everton',
                      8 : 'West Bromwich',
                      9 : 'West Ham Utd',
                      10 : 'Watford',
                      11 : 'Stoke City',
                      12 : 'Burnley',
                      13 : 'Southampton',
                      14 : 'Bournemouth',
                      15 : 'Middlesbrough',
                      16 : 'Leicester City',
                      17 : 'Swansea City',
                      18 : 'Hull City',
                      19 : 'Crystal Palace',
                      20 : 'Sunderland'}

OUTPUT_DF_COLUMNS = ('Home_Team', 'Away_team', 'Home_win_rate', 'Away_win_rate', 'Draw_rate')

