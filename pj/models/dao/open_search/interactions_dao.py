from pj.models.dao.open_search_dao import OpenSearchDAO
from pj.models.interaction import Interaction
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class InteractionsDAO(OpenSearchDAO):
    DB_ENTITY_NAME = OPEN_SEARCH_ENTITY_NAMES['Interaction']

    def create_entity(self):
        return super().create_entity(Interaction())
