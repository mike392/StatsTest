'''
Created on Dec 27, 2016

@author: Mikhail_Barsukou
'''
import sqlite3
import os
from common.settings import RESOURCES_DIR

class DatabaseUtils:
    select_string = 'Select * from (SELECT a.id, countries.name as Country, leagues.name as League, a.season, a.stage, a.date, home_teams.team_long_name as home_team, away_teams.team_long_name as away_team, a.home_team_goal, a.away_team_goal FROM Match a left outer join Country countries on a.country_id = countries.id left outer join League leagues on a.league_id = leagues.id left outer join Team home_teams on a.home_team_api_id = home_teams.team_api_id left outer join Team away_teams on a.away_team_api_id = away_teams.team_api_id) tab WHERE {}'
    def get_database(self, database_name):
        return sqlite3.connect(os.path.join(RESOURCES_DIR,database_name))

    def get_db_cursor(self, db_object):
        return db_object.cursor()
    
    def get_conditions_string(self, conditions_dict):
        conditions_string = ''
        for column, value in conditions_dict.iteritems():
            if isinstance(value, str):
                value = value.split()
            conditions_string += column + ' in (' + ','.join(value) + ') and '
        return conditions_string[:-4]
    
    def get_simple_query_result(self, cursor, table_name):
        cursor.execute('SELECT * FROM {}'.format(table_name))
        return cursor.fetchall()
    
    def get_match_query_result(self, cursor, conditions_dict):
        cursor.execute(self.select_string.format(self.get_conditions_string(conditions_dict)))
        columns = [item[0] for item in cursor.description]
        return cursor.fetchall(), columns 
    
    def get_table_columns_list(self, cursor, table_name):
        cursor.execute('PRAGMA table_info({})'.format(table_name))
        result = cursor.fetchall()
        return [item[1] for item in result]