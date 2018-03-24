from venue_objects.helper import add_attr_db, convert_params


class AttributesItem:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "display_name": "display-name",
            "display_value": "display-value",
            "pier_tier": "pier-tier"

        }
        if db_result is None:
            db_result = db.find("attributes_items", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)
