from venue_objects.country import Country
from venue_objects.helper import add_attr_db, convert_params


class City:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "city": "city",
            "state": "state",
            "postalCode": "postalCode"
        }

        if db_result is None:
            db_result = db.find("cities", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)

        if db_result.get('_id_country') is not None:
            self.country = Country(db, id=db_result["_id_country"])
