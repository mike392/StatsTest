'''
Created on Dec 29, 2016

@author: Mikhail_Barsukou
'''
from utils.DatabaseUtils.DatabaseUtils import DatabaseUtils
from utils.PandasUtils.PandasUtils import PandasUtils

class DBLoader(DatabaseUtils, PandasUtils):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.database_name = 'database.sqlite'
        self.conditions_dict = {"Country" : "'England'",
                       "season" : "'2015/2016'"}
     
    def get_working_dataframe(self):   
        db_instance = self.get_database(self.database_name)
        cur = self.get_db_cursor(db_instance)
        dataset_list, columns_list = self.get_match_query_result(cur, self.conditions_dict)
        #columns_list = self.get_table_columns_list(cur, self.table_name) 
        return self.get_dataframe(dataset_list, columns_list)
    
    def load_results(self):
        pass