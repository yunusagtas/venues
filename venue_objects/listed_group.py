from venue_objects.listed_group_item import ListedGroupsItem
from venue_objects.helper import add_attr_db, convert_params


class ListedGroup:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "type": "type",
            "name": "name",
            "count": "count"
        }
        if db_result is None:
            db_result = db.find("listed_groups", convert_params(attr_db, query))

        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(ListedGroup(db, db_result=i, id=i["_id"]))
            return

        add_attr_db(self, db_result, attr_db)

        self.items = []
        for id in db_result.get('_ids_listed_groups_items') or ():
            if id is not None:
                self.items.append(ListedGroupsItem(db, id=id))
