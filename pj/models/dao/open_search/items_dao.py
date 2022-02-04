from pj.models.dao.open_search_dao import OpenSearchDAO
from pj.models.item import Item
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class ItemsDAO(OpenSearchDAO):
    DB_ENTITY_NAME = OPEN_SEARCH_ENTITY_NAMES['Item']

    def create_entity(self):
        return super().create_entity(Item())
