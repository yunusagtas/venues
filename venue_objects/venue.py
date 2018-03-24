from venue_objects.attribute import Attribute
from venue_objects.attributes_item import AttributesItem
from venue_objects.been_here import BeenHere
from venue_objects.category import Category
from venue_objects.chain import Chain
from venue_objects.contact import Contact
from venue_objects.hours import Hours
from venue_objects.likes import Likes
from venue_objects.listed_group import ListedGroup
from venue_objects.listed_group_item import ListedGroupsItem
from venue_objects.listed_item_listitem import ListedItemListitem
from venue_objects.location import Location
from venue_objects.menu import Menu
from venue_objects.page import Page
from venue_objects.city import City
from venue_objects.color import Color
from venue_objects.here_now import HereNow
from venue_objects.page_link import PageLink
from venue_objects.photo_item import PhotoItem
from venue_objects.photo_source import PhotoSource
from venue_objects.photos import Photos
from venue_objects.phrases import Phrases
from venue_objects.prices import Prices
from venue_objects.reasons_item import ReasonsItem
from venue_objects.stats import Stats
from venue_objects.tips_group import TipsGroup
from venue_objects.tips_item import TipsItem
from venue_objects.helper import add_attr_db, convert_params


class Venue:
    def __init__(self, db, db_result=None, **query):

        attr_db = {
            "id": "_id",
            "name": "name",
            "has_menu": "hasMenu",
            "venuescol": "venuescol",
            "like": "like",
            "dislike": "dislike",
            "ok": "ok",
            "rating": "rating",
            "rating_color": "ratingColor",
            "rating_signals": "ratingSignals",
            "allow_menu_url_edit": "allowMenuUrlEdit",
            "created_at": "created-at"
        }

        if db_result is None:
            db_result = db.find("venues", convert_params(attr_db, query))

        if type(db_result) is list:
            self.items = []
            for i in db_result:
                self.items.append(Venue(db, db_result=i, id=i["_id"]))
            return

        add_attr_db(self, db_result, attr_db)

        self.categories = []
        for id in db_result.get('_ids_categories') or ():
            if id is not None:
                self.categories.append(Category(db, id=id))

        if db_result.get('_id_location') is not None:
            self.location = Location(db, id=db_result["_id_location"])

        if db_result.get('_id_contact') is not None:
            self.contact = Contact(db, id=db_result["_id_contact"])

        if db_result.get('_id_stats') is not None:
            self.stats = Stats(db, id=db_result["_id_stats"])

        if db_result.get('_id_price') is not None:
            self.prices = Prices(db, id=db_result["_id_price"])

        if db_result.get('_id_likes') is not None:
            self.likes = Likes(db, id=db_result["_id_likes"])

        if db_result.get('_id_menu') is not None:
            self.menu = Menu(db, id=db_result["_id_menu"])

        if db_result.get('_id_been_here') is not None:
            self.been_here = BeenHere(db, id=db_result["_id_been_here"])

        if db_result.get('_id_photos') is not None:
            self.photos = Photos(db, id=db_result["_id_photos"])

        if db_result.get('_id_page') is not None:
            self.page = Page(db, id=db_result["_id_page"])

        if db_result.get('_id_here-now') is not None:
            self.here_now = HereNow(db, id=db_result["_id_here-now"])

        self.reasons = []
        for id in db_result.get('_ids_reason_items') or ():
            if id is not None:
                self.reasons.append(ReasonsItem(db, id=id))

        self.tips = []
        for id in db_result.get('_ids_tips_groups') or ():
            if id is not None:
                self.tips.append(TipsGroup(db, id=id))

        self.listed = []
        for id in db_result.get('_ids_listed_groups') or ():
            if id is not None:
                self.listed.append(ListedGroup(db, id=id))

        self.phrases = []
        for id in db_result.get('_ids_phrases') or ():
            if id is not None:
                self.phrases.append(Phrases(db, id=id))

        self.hours = []
        for id in db_result.get('_ids_hours') or ():
            if id is not None:
                self.hours.append(Hours(db, id=id))

        self.tips = []
        for id in db_result.get('_ids_tips_groups') or ():
            if id is not None:
                self.tips.append(TipsGroup(db, id=id))

        self.chains = []
        for id in db_result.get('_ids_venue_chains') or ():
            if id is not None:
                self.chains.append(Chain(db, id=id))

        self.attributes = []
        for id in db_result.get('_ids_attributes') or ():
            if id is not None:
                self.attributes.append(Attribute(db, id=id))

        if db_result.get('_id_best_photo') is not None:
            self.best_photo = PhotoItem(db, id=db_result["_id_best_photo"])

        if db_result.get('_id_colors') is not None:
            self.color = Color(db, id=db_result["_id_colors"])
