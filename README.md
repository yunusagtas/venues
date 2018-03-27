
# Venue Query API
## Description
This is my tutorial. You can get json data of Venue Details

## Installing
 - pip install pymongo
 - pip install flask
 - Unrar Data.rar and start mongodb with --dbpath <your Data directory> argument
 - configure database.py

# How to get data?
## Get Data of Entity Type
if you want all data of entity, use plural like: venues, tips, photos
	

    GET your_ip/<entity_names>/
**List Of Plural Entities**
 - venues
 - photos
 - tips
 - lists
 - users
 - attributes

Sample: `http://127.0.0.1:5000/venue/`

## Get Entity From ID
All entities have unique id number.

    GET your_ip/<entity_name>/<id>
**List Of Entities**
 - venue
 - photosGroup
 - photoItem
 - photoSource
 - tipsGroup
 - tip
 - list
 - listsGroup
 - listItem
 - user
 - contact
 - attribute
 - attributeItem
 - beenHere
 - category
 - chain
 - city
 - color
 - country
 - hereNow
 - hours
 - hoursTimeframe
 - likes
 - location
 - menu
 - page
 - pageLink
 - pharases
 - pharasesSample
 - prices
 - reasonsItem
 - stats

Sample: `http://127.0.0.1:5000/photoItem/1/`

## Get Entity From Key and Value
Some keys begins with "**_ids**". It is array of unique id. You can query like id, if your number is exists in array, will be return entity.

Sample: `http://127.0.0.1:5000/venue/_ids_categories/4/`
Sample2: `http://127.0.0.1:5000/user/gender/male/`

***Importent:*** your result has multiple entity, they are will in **items[]**

**List Of Keys of Entities**
 - venue
	- id
	- _ids_categories
	- _id_lociation
	- _id_contact
	- _id_stats
	- _id_price
	- _id_likes
	- _id_menu
	- _id_special
	- _id_been_here
	- _id_photos
	- _ids_reason_items
	- _id_page
	- _ids_tips_groups
	- _ids_listed_groups
	- _id_phrases
	- _id_hours
	- _ids_venue_chains
	- _ids_attributes
	- _id_best_photo
	- _id_colors
	- name
	- has_menu
	- venuescol
	- like
	- dislike
	- ok
	- rating
	- rating_color
	- rating_signals
	- allow_menu_url_edit
	- created_at
- photosGroup
	- id
	- created_at
	- prefix
	- suffix
	- width
	- height
	- visibility
	- _id_user
	- _id_source
- photoItem
	- id
	- type
	- name
	- count
	- _ids_photos_groups
- photoSource
	- id
	- name
	- url
- tipsGroup
	- id
	- type
	- name
	- count
	- _ids_tips_groups_items
- tip
	- id
	- created_at
	- text
	- type
	- like
	- log_view
	- agree_count
	- disagree_count
	- todo_count
- list
	- id
	- type
	- name
	- count
	- _ids_listed_groups_items
- listGroup
	 - id
	 - name
	 - description
	 - type
	 - editable
	 - public
	 - collaborative
	 - url
	 - created_at
	 - updated_at
	 - log_view
	 - follower_count
	 - listitems_count
	 - _id_user
	 - _id_photos_groups_item
	 - _id_listed_groups_items_listitems
- listItem
	- id
	- created_at
	- _id_tips_groups_items
	- _id_photos_groups_items
- user
	 - id
	 - firstName
	 - gender
	 - prefix
	 - suffix
	 - type
- contact
	- id
	- phone
	- twitter
	- facebook
	- facebook_username
	- facebook_name
	- instagram
- attribute
	- id
	- type
	- name
	- summary
	- count
- attributeItem
	- id
	- display_name
	- display_value
	- pier_tier
- beenHere
	- id
	- unconfirmed_count
	- marked
	- last_checkin_expired_at
- category
	- id
	- name
	- plural_name
	- short_name
	- icon_prefix
	- icon_suffix
	- primary
- chain
	- id
	- best_name
	- best_name_lang
	- logo_prefix
	- logo_suffix
- city
	- id
	- city
	- state
	- postalCode
- color
	- id
	- highlight_value
	- highligth_text_value
- country
	- id
	- country
	- cc
- hereNow
	- id
	- count
	- summary
- hours
	- id
	- status
	- rich_status_text
	- is_open
	- is_local_holiday
	
- hoursTimeframe
	- id
	- days
	- rendered_time
	
-  likes
	- id
	- count
	- summary
	- type
- location
	- id
	- address
	- crossStreet
	- lat
	- lgn
- menu
	- id
	- type
	- label
	- anchor
	- url
	- mobilUrl
- page
	- id
	- description
	- banner
	- _ids_page_links
- pageLink
    - id
    - url
- phrases
    - id
    - phrase
    - count
    - _id_phrases_samples
- phrasesSample
    - id
    - text
    - indices_start
- prices
    - id
    - tier
    - message
    - currency
- reasonsItem
    - id
    - summary
    - type
    - reason_name
- stats
    - id
    - tip_count
    - users_count
    - checkins_count
    - visits_count
