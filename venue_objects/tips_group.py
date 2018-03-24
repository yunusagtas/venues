from venue_objects.tips_item import TipsItem
from venue_objects.helper import add_attr_db, convert_params


class TipsGroup:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "type": "type",
            "name": "name",
            "count": "count"
        }

        if db_result is None:
            db_result = db.find("tips_groups", convert_params(attr_db, query))

        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(TipsGroup(db, db_result=i, id=i["_id"]))
            return

        add_attr_db(self, db_result, attr_db)

        self.items = []
        for id in db_result.get('_ids_tips_groups_items') or ():
            if id is not None:
                self.items.append(TipsItem(db, id=id))
