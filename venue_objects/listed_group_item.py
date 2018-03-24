from venue_objects.listed_item_listitem import ListedItemListitem
from venue_objects.photo_item import PhotoItem
from venue_objects.user import User
from venue_objects.helper import add_attr_db, convert_params


class ListedGroupsItem:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "name": "name",
            "description": "description",
            "type": "type",
            "editable": "editable",
            "public": "public",
            "collaborative": "collaborative",
            "url": "url",
            "created_at": "created-at",
            "updated_at": "updated_at",
            "log_view": "log-view",
            "follower_count": "follower-count",
            "listitems_count": "listitems-count"
        }
        if db_result is None:
            db_result = db.find("listed_groups_items", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)

        if db_result.get('_id_user') is not None:
            self.user = User(db, _id=db_result["_id_user"])

        if db_result.get('_id_photos_groups_item') is not None:
            self.photo_item = PhotoItem(db, _id=db_result["_id_photos_groups_item"])

        if db_result.get('_id_listed_groups_items_listitems') is not None:
            self.item = ListedItemListitem(db, _id=db_result["_id_listed_groups_items_listitems"])
