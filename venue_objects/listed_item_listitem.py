from venue_objects.tips_item import TipsItem
from venue_objects.photo_item import PhotoItem
from venue_objects.helper import add_attr_db, convert_params


class ListedItemListitem:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "created_at": "created-at"
        }
        if db_result is None:
            db_result = db.find("listed_groups_items_listitems", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)

        if db_result.get('_id_tips_groups_items') is not None:
            self.tips_item = TipsItem(db, id=db_result["_id_tips_groups_items"])

        if db_result.get('_id_photos_groups_items') is not None:
            self.photo_item = PhotoItem(db, id=db_result["_id_photos_groups_items"])
