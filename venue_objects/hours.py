from venue_objects.hours_timeframe import HoursTimeFrame
from venue_objects.helper import add_attr_db, convert_params


class Hours:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "status": "status",
            "rich_status_text": "rich-status-text",
            "is_open": "is-open",
            "is_local_holiday": "is-local-holiday"
        }
        if db_result is None:
            db_result = db.find("hours", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)

        self.frames = []
        for id in db_result.get('_ids_hours_timeframes') or ():
            if id is not None:
                self.frames.append(HoursTimeFrame(db, id=id))
