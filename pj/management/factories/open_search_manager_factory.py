import pj.factories.dynamo_manager_factory
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class OpenSearchManagerFactory(pj.factories.open_search_manager_factory.OpenSearchManagerFactory):
    VALID_INSTANCE_TYPES = [OPEN_SEARCH_ENTITY_NAMES['Article']]
