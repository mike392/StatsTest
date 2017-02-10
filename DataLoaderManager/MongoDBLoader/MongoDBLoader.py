'''
Created on Jan 16, 2017

@author: Mikhail_Barsukou
'''
from utils.MongoUtils.MongoUtils import MongoUtils
from utils.SiteScraper.SiteScraper import SiteScraper
from utils.PandasUtils.PandasUtils import PandasUtils
from common import settings

class MongoDBLoader(MongoUtils, PandasUtils):
    
    def __init__(self):
        pass
    
    def get_working_dataframe(self):
        scraper = SiteScraper()
        scraper.grab_data()
        return self.get_dataframe(scraper.get_data(), settings.MATCH_STRUCTURE)
    
    def load_results(self):
        pass
    