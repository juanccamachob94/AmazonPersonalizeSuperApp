import pj.models.dao.dynamo_dao
from pj.values.db_entity_names import DYNAMO_ENTITY_NAMES
from pj.management.factories.dynamo_manager_factory import DynamoManagerFactory

class DynamoDAO(pj.models.dao.dynamo_dao.DynamoDAO):
    VALID_INSTANCE_TYPES = [DYNAMO_ENTITY_NAMES['Article']]

    def __init__(self):
        self.db_manager = DynamoManagerFactory.perform(self.DB_ENTITY_NAME)
