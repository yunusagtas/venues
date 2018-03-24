from venue_objects.helper import add_attr_db, convert_params


class Country:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "country": "country",
            "cc": "cc"
        }
        if db_result is None:
            db_result = db.find("countries", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)
