from venue_objects.helper import add_attr_db, convert_params


class ReasonsItem:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "summary": "summary",
            "type": "type",
            "reason_name": "reason-name"
        }
        if db_result is None:
            db_result = db.find("reasons_items", convert_params(attr_db, query))
        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(ReasonsItem(db, db_result=i, id=i["_id"]))
            return

        add_attr_db(self, db_result, attr_db)
