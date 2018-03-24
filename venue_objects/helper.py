import json
from json import JSONEncoder

def convert_params(attr_db, queries):
    for key, value in queries.items():
        if key in attr_db:
            queries[attr_db[key]] = queries.pop(key)
    return queries


def add_attr_db(object, db_result, dict):
    if db_result:
        if len(db_result) > 0:
            for key, value in dict.items():
                if value in db_result:
                    if db_result[value] is not None:
                        setattr(object, key, db_result[value])
    else:
        raise Exception('query parameters not enought for single result: %s' % (str(db_result)))


class VenueJsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__