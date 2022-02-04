import pj.factories.dynamo_manager_factory
from pj.values.db_entity_names import DYNAMO_ENTITY_NAMES

class DynamoManagerFactory(pj.factories.dynamo_manager_factory.DynamoManagerFactory):
    VALID_INSTANCE_TYPES = [DYNAMO_ENTITY_NAMES['Article']]
