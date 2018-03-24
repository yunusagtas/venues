from venue_objects.helper import add_attr_db, convert_params


class BeenHere:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "unconfirmed_count": "unconfirmed_Count",
            "marked": "marked",
            "last_checkin_expired_at": "lastCheckinExpiredAt"
        }

        if db_result is None:
            db_result = db.find("been_here", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)
