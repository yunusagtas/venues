from venue_objects.photo_source import PhotoSource
from venue_objects.user import User
from venue_objects.helper import add_attr_db,convert_params


class PhotoItem:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "created_at": "createdAt",
            "prefix": "prefix",
            "suffix": "suffix",
            "width": "width",
            "height": "height",
            "visibility": "visibility"
        }
        if db_result is None:
            db_result = db.find("photos_groups_items", convert_params(attr_db, query))


        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(PhotoItem(db, db_result=i, id=i["_id"]))
            return



        add_attr_db(self, db_result, attr_db)

        if db_result.get('_id_user') is not None:
            self.user = User(db, id=db_result['_id_user'])

        if db_result.get('_id_source') is not None:
            self.source = PhotoSource(db, id=db_result['_id_source'])
