'''
Created on Jan 16, 2017

@author: Mikhail_Barsukou
'''
from common import settings
import pymongo
import datetime
from main import db_instance
from bson.objectid import ObjectId

class MongoUtils:
    '''
    classdocs
    '''
    __db__ = None

    def __init__(self):
        '''
        Constructor
        '''

        
    def get_db_instance(self):
        if self.__db__ is None:
            self.__db__ = pymongo.MongoClient(host=self.mongo_host, port=self.mongo_port).match_repo
        return self.__db__
    
    def insert_data(self, db_instance, result_dict):
        id = db_instance.match_results.insert(result_dict)
        self.insert_session(db_instance, id, 'match_results')
    
    def insert_session(self, db_instance, id, collection_name):
        now = datetime.datetime.now()
        index = self.get_next_session_index(db_instance)
        result = {'SessionIndex' : index, 'SessionTime': str(now), 'SessionId' : str(id),  'CollectionName': collection_name}
        db_instance.sessions.insert(result)
        
    def get_next_session_index(self, db_instance):
        result = self.get_max_session_index(db_instance)
        return (result + 1) if result else 1
    
    def get_max_session_index(self, db_instance):
        result = list(db_instance.sessions.aggregate([{'$group' : { '_id': 0, 'count' : { '$max' : '$SessionIndex'} }}]))
        return result[0]['count'] if len(result) > 0 else None
    
    def get_last_session_id(self, db_instance):
        result = list(db_instance.sessions.find({'SessionIndex' : self.get_max_session_index(db_instance)}))
        return result[0]['SessionId']
    
    def get_data(self, db_instance):
        session_id = self.get_last_session_id(db_instance)
        result = list(db_instance.match_results.aggregate([{'$match' : { '_id' : ObjectId(session_id)}},
                                                           {'$unwind':{ 'path' :'$England' }},{
                                                               '$project':{
                '_id':0,
                'country': "England",
                'home_team': "$England.home_team",
                'away_team': "$England.away_team",
                'home_team_goal': "$England.home_team_goal",
                'away_team_goal': "$England.away_team_goal"
                }
                                                               },
                                                           { '$limit' : settings.MATCH_NUMBER_LIMIT }]))
        return result