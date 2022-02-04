from pj.models.dao.open_search_dao import OpenSearchDAO
from pj.models.interaction import Interaction
from pj.models.dao.open_search.items_dao import ItemsDAO
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES
from pj.models.dao.interactions_interface_dao import InteractionsInterfaceDAO

class InteractionsDAO(InteractionsInterfaceDAO, OpenSearchDAO):
    DB_ENTITY_NAME = OPEN_SEARCH_ENTITY_NAMES['Interaction']

    def create_entity(self):
        return super().create_entity(Interaction())


    def _exists_item(self, interaction):
        itemsDAO = ItemsDAO()
        return itemsDAO.find({ 'item_id': interaction.get_item_id() })
