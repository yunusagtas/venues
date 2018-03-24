from pymongo import MongoClient

class Database:

    def __init__(self):
        print("database init")
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['venues']

    def find(self, collection_name, query_params):
        result = self.db[collection_name].find(query_params)
        if result.count() > 1:
            return list(result)
        elif result.count() == 1:
            return result[0]
        else:
            return False
