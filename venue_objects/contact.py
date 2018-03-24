from venue_objects.helper import add_attr_db, convert_params


class Contact:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "phone": "phone",
            "twitter": "twitter",
            "facebook": "facebook",
            "facebook_username": "facebookUsername",
            "facebook_name": "facebook_name",
            "instagram": "instagram"
        }

        if db_result is None:
            db_result = db.find("contact", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)
