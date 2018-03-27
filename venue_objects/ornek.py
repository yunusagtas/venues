from venue_objects.attributes_item import AttributesItem
from venue_objects.helper import add_attr_db, convert_params


class Ornek:
    def __init__(self, db, db_result=None, **query):
        #soldakiler bu sınıfa ait özellikler, sağdakiler veritabanındaki karşılıkları olacak
        attr_db = {
            "id": "_id",
            "type": "type",
            "name": "name",
            "summary": "summary",
            "count": "count"
        }

        #veritabanından bilgi çeker, eğer bu sınıf kendini çağırırsa 2. kez database sorgulamasını engelledik
        if db_result is None:
            db_result = db.find("ornekler_tablosu", convert_params(attr_db, query))

        #eğer databaseden birden fazla sonuç dönderse items adı altında bu sınıf kendi kendini listeye ekliyecektir
        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(Ornek(db, db_result=i, id=i["_id"]))
            return

        #üstteki dict in veritabanına karşılık gelen kısımlar bu sınıfa eklenirken olmayanlar yada null olanlar es geçilecek
        add_attr_db(self, db_result, attr_db)

        #veritabanındaki id dizisinden kendine alt nesneler ekler
        self.child_items = []
        for id in db_result.get('_ids_ornek_child') or ():
            if id is not None:
                self.child_items.append(AttributesItem(db, id=id))
