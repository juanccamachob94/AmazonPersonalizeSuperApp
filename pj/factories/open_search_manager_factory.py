from pj.services.db.open_search_manager import OpenSearchManager
from pj.models.db_manager_clients.open_search_manager_client import OpenSearchManagerClient
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class OpenSearchManagerFactory:
    VALID_INSTANCE_TYPES = [
        OPEN_SEARCH_ENTITY_NAMES['ArticleInteraction'],
        OPEN_SEARCH_ENTITY_NAMES['Item'],
        OPEN_SEARCH_ENTITY_NAMES['Interaction'],
        OPEN_SEARCH_ENTITY_NAMES['SubItem'],
        OPEN_SEARCH_ENTITY_NAMES['User']
    ]
    instances = {}

    @classmethod
    def perform(cls, db_entity_name):
        if not db_entity_name in cls.VALID_INSTANCE_TYPES:
            raise Exception('unknown OpenSearch db_entity_name value - ', db_entity_name)
        if not cls.instances.get(db_entity_name):
            cls.instances[db_entity_name] = \
                OpenSearchManager(OpenSearchManagerClient(db_entity_name))
        return cls.instances[db_entity_name]
