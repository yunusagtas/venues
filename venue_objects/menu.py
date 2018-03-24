from venue_objects.helper import add_attr_db, convert_params


class Menu:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "type": "type",
            "label": "label",
            "anchor": "anchor",
            "url": "url",
            "mobilUrl": "mobilUrl"
        }
        if db_result is None:
            db_result = db.find("menu", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)
