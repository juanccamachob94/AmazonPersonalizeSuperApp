from pj.models.dao.open_search.items_dao import ItemsDAO
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class SubItemsDAO(ItemsDAO):
    DB_ENTITY_NAME = OPEN_SEARCH_ENTITY_NAMES['SubItem']
