from utils.DatabaseUtils.DatabaseUtils import DatabaseUtils
from utils.PandasUtils.PandasUtils import PandasUtils
from utils.NumpyUtils.NumpyUtils import NumpyUtils
import re


class StatTest( PandasUtils, NumpyUtils):
    
    def __init__(self, home_team, away_team, dataframe):
        self.home_team = home_team
        self.away_team = away_team
        self.input_dataframe = dataframe        
    
    def get_distribution_lambda(self, dataframe, team_flag):
        goal_column_name = '{}_team_goal'.format(team_flag)
        column_name = '{}_team'.format(team_flag)
        team_name = self.home_team if team_flag == 'home' else self.away_team
        avg_goals = self.get_avg_for_column(dataframe, goal_column_name)
        team_pattern = re.compile(team_name)
        team_avg_home_goals_scored = self.get_avg_for_column(dataframe.loc[dataframe[column_name] == team_name], goal_column_name)
        column_name = '{}_team'.format('home') if team_flag == 'away' else '{}_team'.format('away')
        team_name = self.home_team if team_name == self.away_team else self.away_team
        team_avg_away_goals_missed = self.get_avg_for_column(dataframe.loc[dataframe[column_name] == team_name], goal_column_name)
        return ( team_avg_home_goals_scored * team_avg_away_goals_missed ) / avg_goals
         
    def start(self):
               
        home_lambda = self.get_distribution_lambda(self.input_dataframe, 'home') 
        away_lambda = self.get_distribution_lambda(self.input_dataframe, 'away')
        
        home_distrib = self.get_poisson_distrib(home_lambda, range(6))
        away_distrib = self.get_poisson_distrib(away_lambda, range(6))
        
        result_matrix = self.get_product_matrix(home_distrib, away_distrib)
        
        draw_rate, home_win_rate, away_win_rate = self.get_bet_rates(result_matrix)
        
        return(self.home_team, self.away_team, home_win_rate, away_win_rate, draw_rate)
        
    
