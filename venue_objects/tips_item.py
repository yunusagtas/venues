from venue_objects.likes import Likes
from venue_objects.user import User
from venue_objects.helper import add_attr_db, convert_params


class TipsItem:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "created_at": "created-at",
            "text": "text",
            "type": "type",
            "like": "like",
            "log_view": "logView",
            "agree_count": "agree-count",
            "disagree_count": "disagree-count",
            "todo_count": "todo-count"
        }

        if db_result is None:
            db_result = db.find("tips_groups_items", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)

        if db_result.get('_id_likes') is not None:
            self.likes = Likes(db, id=db_result["_id_likes"])

        if db_result.get('_id_user') is not None:
            self.user = User(db, id=db_result["_id_user"])
