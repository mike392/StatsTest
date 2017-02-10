'''
Created on Dec 27, 2016

@author: Mikhail_Barsukou
'''
from StatTest.StatTest import StatTest
from DataLoaderManager.DataLoaderManager import DataloaderManager
from common.settings import SOCCER_STATS_TEAMS, OUTPUT_DF_COLUMNS
from utils.PandasUtils.PandasUtils import PandasUtils as pd
from pprint import PrettyPrinter


if __name__ == '__main__':
    team_pairs = [
        [SOCCER_STATS_TEAMS[4], SOCCER_STATS_TEAMS[18]],
        [SOCCER_STATS_TEAMS[20], SOCCER_STATS_TEAMS[13]],
        [SOCCER_STATS_TEAMS[11], SOCCER_STATS_TEAMS[19]],
        [SOCCER_STATS_TEAMS[6], SOCCER_STATS_TEAMS[10]],
        [SOCCER_STATS_TEAMS[15], SOCCER_STATS_TEAMS[7]],
        [SOCCER_STATS_TEAMS[9], SOCCER_STATS_TEAMS[8]],
        [SOCCER_STATS_TEAMS[5], SOCCER_STATS_TEAMS[2]],
        [SOCCER_STATS_TEAMS[12], SOCCER_STATS_TEAMS[1]],
        [SOCCER_STATS_TEAMS[17], SOCCER_STATS_TEAMS[16]],
        [SOCCER_STATS_TEAMS[14], SOCCER_STATS_TEAMS[3]]
        ]
                  
    result = []
    
    dlm = DataloaderManager()
    working_dataframe = dlm.get_data()
    for team_pair in team_pairs:
        test = StatTest(team_pair[0], team_pair[1], working_dataframe)
        result.append(test.start())
    pnd = pd()
    df = pnd.get_dataframe(result, OUTPUT_DF_COLUMNS)
    pp = PrettyPrinter()
    pp.pprint(df)
    