from venue_objects.attributes_item import AttributesItem
from venue_objects.helper import add_attr_db, convert_params


class Attribute:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "type": "type",
            "name": "name",
            "summary": "summary",
            "count": "count"
        }

        if db_result is None:
            db_result = db.find("attributes", convert_params(attr_db, query))

        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(Attribute(db, db_result=i, id=i["_id"]))
            return

        add_attr_db(self, db_result, attr_db)

        self.attributes_items = []
        for id in db_result.get('_ids_attributes_items') or ():
            if id is not None:
                self.attributes_items.append(AttributesItem(db, id=id))