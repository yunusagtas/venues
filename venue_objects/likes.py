from venue_objects.helper import add_attr_db,convert_params


class Likes:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "count": "count",
            "summary": "summary",
            "type": "type"
        }
        if db_result is None:
            db_result = db.find("likes", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)
