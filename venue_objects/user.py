from venue_objects.helper import add_attr_db, convert_params


class User:
    def __init__(self, db, db_result=None, **query):
        print(query)

        attr_db = {
            "id": "_id",
            "firstName": "firstName",
            "gender": "gender",
            "prefix": "prefix",
            "suffix": "suffix",
            "type": "type"
        }

        print(convert_params(attr_db, query))

        if db_result is None:
            db_result = db.find("users", convert_params(attr_db, query))

        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(User(db, db_result=i, id=i["_id"]))
            return

        add_attr_db(self, db_result, attr_db)
