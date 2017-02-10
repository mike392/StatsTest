'''
Created on Jan 16, 2017

@author: Mikhail_Barsukou
'''
import urllib2
from bs4 import BeautifulSoup
import lxml
from utils.MongoUtils.MongoUtils import MongoUtils
from common import settings
import datetime

class SiteScraper(MongoUtils):
    '''
    classdocs
    '''
    __name__ = ''

    def __init__(self):
        '''
        Constructor
        '''
        self.mongo_host = settings.MONGO_HOST
        self.mongo_port = settings.MONGO_PORT
        self.db = self.get_db_instance()
        
    def contains_digits(self, s):
            return any(char.isdigit() for char in s)
        
    def prepare_value(self, tag_object):
            return str(tag_object.text.encode('utf-8', 'ignore').replace('\xc2','').replace('\xa0','')).strip()
    
    def grab_data(self):
        resource_to_year_link = settings.RESOURCE_TO_YEAR_ENGLAND
        result_dict = {}
        match_list = []
        for resource in resource_to_year_link.keys():
            page = urllib2.urlopen(resource).read()
            soup = BeautifulSoup(page, "lxml")
            res = soup.find("table", id="btable")
            
            rows = res.select('tr')
            year = resource_to_year_link[resource]
            match_number = 1
            for row in rows:
                cells = row.select("td")
                if len(cells) > 2 and self.contains_digits(cells[3].text):
                    match_data = {}
                    match_date = datetime.datetime.strptime(self.prepare_value(cells[0]).replace('.', ''), '%a %d %b')
                    match_data[settings.MATCH_STRUCTURE[0]] = year
                    match_data[settings.MATCH_STRUCTURE[1]] = match_number
                    match_data[settings.MATCH_STRUCTURE[2]] = match_date.month
                    match_data[settings.MATCH_STRUCTURE[3]] = match_date.day
                    match_data[settings.MATCH_STRUCTURE[4]], match_data[settings.MATCH_STRUCTURE[5]] = self.prepare_value(cells[2]).split(' - ')
                    goals = self.prepare_value(cells[3]).split(' - ')
                    goals = [int(item) for item in goals]
                    match_data[settings.MATCH_STRUCTURE[6]], match_data[settings.MATCH_STRUCTURE[7]] = goals
                    match_number += 1
                    match_list.append(match_data)
        match_list.sort(key=lambda x: (-x[settings.MATCH_STRUCTURE[0]], -x[settings.MATCH_STRUCTURE[1]]))
        result_dict['England'] = match_list
        self.insert_data(self.db, result_dict)
        
    def get_data(self):
        return MongoUtils.get_data(self, self.db)