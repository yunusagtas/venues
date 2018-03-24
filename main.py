from flask import Flask, Response
from json import JSONEncoder
import re

from database import Database

from venue_objects.attribute import Attribute
from venue_objects.attributes_item import AttributesItem
from venue_objects.been_here import BeenHere
from venue_objects.category import Category
from venue_objects.chain import Chain
from venue_objects.contact import Contact
from venue_objects.country import Country
from venue_objects.helper import VenueJsonEncoder
from venue_objects.hours import Hours
from venue_objects.hours_timeframe import HoursTimeFrame
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
from venue_objects.phrases_sample import PhrasesSample
from venue_objects.prices import Prices
from venue_objects.reasons_item import ReasonsItem
from venue_objects.stats import Stats
from venue_objects.tips_group import TipsGroup
from venue_objects.tips_item import TipsItem
from venue_objects.user import User
from venue_objects.venue import Venue
import json

app = Flask(__name__)
db = Database()


@app.route('/', methods=['GET'])
def main_page():
    return "No query parameter."


@app.route('/<param>/', methods=['GET'])
def get_from_param(param):
    result = ""
    if param == "venues":
        result = VenueJsonEncoder().encode(Venue(db))
    elif param == "photos":
        result = VenueJsonEncoder().encode(Photos(db))
    elif param == "tips":
        result = VenueJsonEncoder().encode(TipsGroup(db))
    elif param == "lists":
        result = VenueJsonEncoder().encode(ListedGroup(db))
    elif param == "users":
        result = VenueJsonEncoder().encode(User(db))
    elif param == "attributes":
        result = VenueJsonEncoder().encode(Attribute(db))

    else:
        return "your parameter (" + param + ") is not valid"

    return Response(result, mimetype='application/json')


@app.route('/<param>/<id>/', methods=['GET'])
def get_from_id(param, id=None):
    result = ""
    if not id.isdigit():
        return "id(" + id + ") must be numeric."
    else:
        try:
            if param == "venue":
                result = VenueJsonEncoder().encode(Venue(db, id=int(id)))
            elif param == "photosGroup":
                result = VenueJsonEncoder().encode(Photos(db, id=int(id)))
            elif param == "photoItem":
                result = VenueJsonEncoder().encode(PhotoItem(db, id=int(id)))
            elif param == "photoSource":
                result = VenueJsonEncoder().encode(PhotoSource(db, id=int(id)))
            elif param == "tipsGroup":
                result = VenueJsonEncoder().encode(TipsGroup(db, id=int(id)))
            elif param == "tip":
                result = VenueJsonEncoder().encode(TipsItem(db, id=int(id)))
            elif param == "list":
                result = VenueJsonEncoder().encode(ListedGroup(db, id=int(id)))
            elif param == "listsGroup":
                result = VenueJsonEncoder().encode(ListedGroupsItem(db, id=int(id)))
            elif param == "listItem":
                result = VenueJsonEncoder().encode(ListedItemListitem(db, id=int(id)))
            elif param == "user":
                result = VenueJsonEncoder().encode(User(db, id=int(id)))
            elif param == "contact":
                result = VenueJsonEncoder().encode(Contact(db, id=int(id)))
            elif param == "attribute":
                result = VenueJsonEncoder().encode(Attribute(db, id=int(id)))
            elif param == "attributeItem":
                result = VenueJsonEncoder().encode(AttributesItem(db, id=int(id)))
            elif param == "beenHere":
                result = VenueJsonEncoder().encode(BeenHere(db, id=int(id)))
            elif param == "category":
                result = VenueJsonEncoder().encode(Category(db,  id=int(id)))
            elif param == "chain":
                result = VenueJsonEncoder().encode(Chain(db, id=int(id)))
            elif param == "city":
                result = VenueJsonEncoder().encode(City(db, id=int(id)))
            elif param == "color":
                result = VenueJsonEncoder().encode(Color(db, id=int(id)))
            elif param == "country":
                result = VenueJsonEncoder().encode(Country(db, id=int(id)))
            elif param == "hereNow":
                result = VenueJsonEncoder().encode(HereNow(db, id=int(id)))
            elif param == "hours":
                result = VenueJsonEncoder().encode(Hours(db, id=int(id)))
            elif param == "hoursTimeframe":
                result = VenueJsonEncoder().encode(HoursTimeFrame(db, id=int(id)))
            elif param == "likes":
                result = VenueJsonEncoder().encode(Likes(db, id=int(id)))
            elif param == "location":
                result = VenueJsonEncoder().encode(Location(db, id=int(id)))
            elif param == "menu":
                result = VenueJsonEncoder().encode(Menu(db, id=int(id)))
            elif param == "page":
                result = VenueJsonEncoder().encode(Page(db, id=int(id)))
            elif param == "pageLink":
                result = VenueJsonEncoder().encode(PageLink(db, id=int(id)))
            elif param == "pharases":
                result = VenueJsonEncoder().encode(Phrases(db, id=int(id)))
            elif param == "pharasesSample":
                result = VenueJsonEncoder().encode(PhrasesSample(db,  id=int(id)))
            elif param == "prices":
                result = VenueJsonEncoder().encode(Prices(db, id=int(id)))
            elif param == "reasonsItem":
                result = VenueJsonEncoder().encode(ReasonsItem(db, id=int(id)))
            elif param == "stats":
                result = VenueJsonEncoder().encode(Stats(db, id=int(id)))

            else:
                return "your parameter (" + param + ") is not valid"
        except:
            return "Your id (" + str(id) + ") is not valid"

    return Response(result, mimetype='application/json')


@app.route('/<param>/<key>/<value>/', methods=['GET'])
def get_from_key_value(param, key, value):
    result = ""
    if key not in ["facebook", "phone", "rating_signals"]:
        if re.match(r"^[-+]?[0-9]+$", value) is not None:
            value = int(value)

    try:
        if param == "venue":
            result = VenueJsonEncoder().encode(Venue(db, **{key:value}))
        elif param == "photosGroup":
            result = VenueJsonEncoder().encode(Photos(db, **{key:value}))
        elif param == "photoItem":
            result = VenueJsonEncoder().encode(PhotoItem(db, **{key:value}))
        elif param == "photoSource":
            result = VenueJsonEncoder().encode(PhotoSource(db, **{key:value}))
        elif param == "tipsGroup":
            result = VenueJsonEncoder().encode(TipsGroup(db, **{key:value}))
        elif param == "tip":
            result = VenueJsonEncoder().encode(TipsItem(db, **{key:value}))
        elif param == "list":
            result = VenueJsonEncoder().encode(ListedGroup(db, **{key: value}))
        elif param == "listGroup":
            result = VenueJsonEncoder().encode(ListedGroupsItem(db, **{key: value}))
        elif param == "listItem":
            result = VenueJsonEncoder().encode(ListedItemListitem(db, **{key: value}))
        elif param == "user":
            result = VenueJsonEncoder().encode(User(db, **{key:value}))
        elif param == "contact":
            result = VenueJsonEncoder().encode(Contact(db, **{key:value}))
        elif param == "attribute":
            result = VenueJsonEncoder().encode(Attribute(db, **{key:value}))
        elif param == "attributeItem":
            result = VenueJsonEncoder().encode(AttributesItem(db, **{key:value}))
        elif param == "beenHere":
            result = VenueJsonEncoder().encode(BeenHere(db, **{key:value}))
        elif param == "category":
            result = VenueJsonEncoder().encode(Category(db, **{key:value}))
        elif param == "chain":
            result = VenueJsonEncoder().encode(Chain(db, **{key:value}))
        elif param == "city":
            result = VenueJsonEncoder().encode(City(db, **{key:value}))
        elif param == "color":
            result = VenueJsonEncoder().encode(Color(db, **{key:value}))
        elif param == "country":
            result = VenueJsonEncoder().encode(Country(db, **{key:value}))
        elif param == "hereNow":
            result = VenueJsonEncoder().encode(HereNow(db, **{key:value}))
        elif param == "hours":
            result = VenueJsonEncoder().encode(Hours(db, **{key:value}))
        elif param == "hoursTimeframe":
            result = VenueJsonEncoder().encode(HoursTimeFrame(db, **{key:value}))
        elif param == "likes":
            result = VenueJsonEncoder().encode(Likes(db, **{key:value}))
        elif param == "location":
            result = VenueJsonEncoder().encode(Location(db, **{key:value}))
        elif param == "menu":
            result = VenueJsonEncoder().encode(Menu(db, **{key:value}))
        elif param == "page":
            result = VenueJsonEncoder().encode(Page(db, **{key:value}))
        elif param == "pageLink":
            result = VenueJsonEncoder().encode(PageLink(db, **{key:value}))
        elif param == "pharases":
            result = VenueJsonEncoder().encode(Phrases(db, **{key: value}))
        elif param == "pharasesSample":
            result = VenueJsonEncoder().encode(PhrasesSample(db, **{key: value}))
        elif param == "prices":
            result = VenueJsonEncoder().encode(Prices(db, **{key: value}))
        elif param == "reasonsItem":
            result = VenueJsonEncoder().encode(ReasonsItem(db, **{key: value}))
        elif param == "stats":
            result = VenueJsonEncoder().encode(Stats(db, **{key: value}))
        else:
            return "your parameter (" + param + ") is not valid"
    except:
        return "Your query (" + key+"=" + str(value) + ") is not valid in "+param

    return Response(result, mimetype='application/json')


if __name__ == '__main__':
    app.run()
