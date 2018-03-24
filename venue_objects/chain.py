from venue_objects.helper import add_attr_db, convert_params


class Chain:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "best_name": "best-name",
            "best_name_lang": "best-name-lang",
            "logo_prefix": "logo-prefix",
            "logo_suffix": "logo-suffix"
        }

        if db_result is None:
            db_result = db.find("venue_chains", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)