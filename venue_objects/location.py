from venue_objects.city import City
from venue_objects.helper import add_attr_db, convert_params


class Location:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "address": "address",
            "crossStreet": "crossStreet",
            "lat": "lat",
            "lgn": "lgn"
        }
        if db_result is None:
            db_result = db.find("location", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)

        if db_result.get("_id_city") is not None:
            self.city = City(db, _id=db_result["_id_city"])
