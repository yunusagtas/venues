from venue_objects.helper import add_attr_db, convert_params


class Stats:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "tip_count": "tipCount",
            "users_count": "usersCount",
            "checkins_count": "checkinsCount",
            "visits_count": "visitsCount"
        }
        if db_result is None:
            db_result = db.find("stats", convert_params(attr_db, query))

        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(Stats(db, db_result=i, id=i["_id"]))
            return

        add_attr_db(self, db_result, attr_db)
