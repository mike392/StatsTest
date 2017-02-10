'''
Created on Jan 16, 2017

@author: Mikhail_Barsukou
'''
from MongoDBLoader.MongoDBLoader import MongoDBLoader
from pprint import PrettyPrinter
#from DBLoader.DBLoader import DBLoader
class DataloaderManager:
    
    def __init__(self):
        self.dataloader = MongoDBLoader()
#        self.dataloader = DBLoader()

    def get_data(self):
        return self.dataloader.get_working_dataframe()
    
    def insert_results_to_database(self):
        self.dataloader.load_results()
