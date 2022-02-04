from pj.models.dao.csv_dao import CSVDAO
from pj.models.item import Item
from pj.values.db_entity_names import CSV_ENTITY_NAMES

class ItemsDAO(CSVDAO):
    DB_ENTITY_NAME = CSV_ENTITY_NAMES['Item']

    def find(self, item_search_dict):
        return self.db_manager.find(Item.build(item_search_dict))

