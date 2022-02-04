from pj.models.dao.dynamo.items_dao import ItemsDAO
from pj.values.db_entity_names import DYNAMO_ENTITY_NAMES

class SubItemsDAO(ItemsDAO):
    DB_ENTITY_NAME = DYNAMO_ENTITY_NAMES['SubItem']
