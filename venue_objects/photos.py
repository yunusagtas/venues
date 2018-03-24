from venue_objects.photo_item import PhotoItem
from venue_objects.helper import add_attr_db, convert_params


class Photos:

    def __init__(self, db, db_result=None, **query):

        attr_db = {
            "id": "_id",
            "type": "type",
            "name": "name",
            "count": "count"
        }

        if db_result is None:
            db_result = db.find("photos", convert_params(attr_db, query))

        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(Photos(db, db_result=i, id=i["_id"]))
            return



        add_attr_db(self, db_result, attr_db)

        self.photos = []
        for id in db_result.get('_ids_photos_groups') or ():
            if id is not None:
                self.photos.append(PhotoItem(db, id=id))
