from venue_objects.helper import add_attr_db, convert_params


class PhrasesSample:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "text": "text",
            "indices_start": "indices_start"
        }

        if db_result is None:
            db_result = db.find("phrases_samples", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)
