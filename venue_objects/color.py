from venue_objects.photo_item import PhotoItem
from venue_objects.helper import add_attr_db, convert_params


class Color:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "highlight_value": "higlight_value",
            "highligth_text_value": "highligth_text_value"
        }

        if db_result is None:
            db_result = db.find("colors", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)

        if db_result.get('_id_highlight_photo') is not None:
            self._id_highlight_photo = PhotoItem(db, id=db_result["_id_highlight_photo"])

        if db_result.get('_id_higlight_text_photo') is not None:
            self._id_highlight_photo = PhotoItem(db, id=db_result["_id_higlight_text_photo"])

