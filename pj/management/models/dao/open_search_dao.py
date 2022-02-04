import pj.models.dao.open_search_dao
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES
from pj.management.factories.open_search_manager_factory import OpenSearchManagerFactory

class OpenSearchDAO(pj.models.dao.open_search_dao.OpenSearchDAO):
    VALID_INSTANCE_TYPES = [OPEN_SEARCH_ENTITY_NAMES['Article']]

    def __init__(self):
        self.db_manager = OpenSearchManagerFactory.perform(self.DB_ENTITY_NAME)
