from venue_objects.phrases_sample import PhrasesSample
from venue_objects.helper import add_attr_db, convert_params


class Phrases:
    def __init__(self, db, db_result=None, **query):

        attr_db = {
            "id": "_id",
            "phrase": "phrase",
            "count": "count"
        }

        if db_result is None:
            db_result = db.find("phrases", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)

        if db_result.get('_id_phrases_samples') is not None:
            self.phrase_sample = PhrasesSample(db, id=db_result["_id_phrases_samples"])
