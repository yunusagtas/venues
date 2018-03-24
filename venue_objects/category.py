from venue_objects.helper import add_attr_db, convert_params


class Category:

    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "name": "name",
            "plural_name": "pluralName",
            "short_name": "shortName",
            "icon_prefix": "icon_prefix",
            "icon_suffix": "icon_suffix",
            "primary": "primary"
        }

        if db_result is None:
            db_result = db.find("categories", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)
