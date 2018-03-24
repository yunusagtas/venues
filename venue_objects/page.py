from venue_objects.page_link import PageLink
from venue_objects.helper import add_attr_db, convert_params


class Page:
    def __init__(self, db, db_result=None, **query):
        attr_db = {
            "id": "_id",
            "description": "description",
            "banner": "banner"
        }

        if db_result is None:
            db_result = db.find("page", convert_params(attr_db, query))

        add_attr_db(self, db_result, attr_db)

        self.page_links = []
        for id in db_result.get('_ids_page_links') or ():
            if id is not None:
                self.page_links.append(PageLink(db, id=id))
