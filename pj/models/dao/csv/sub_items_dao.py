from pj.models.dao.csv.items_dao import ItemsDAO
from pj.values.db_entity_names import CSV_ENTITY_NAMES

class SubItemsDAO(ItemsDAO):
    DB_ENTITY_NAME = CSV_ENTITY_NAMES['SubItem']
