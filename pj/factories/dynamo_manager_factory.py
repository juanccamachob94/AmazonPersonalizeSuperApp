from pj.services.db.dynamo_manager import DynamoManager
from pj.models.db_manager_clients.dynamo_manager_client import DynamoManagerClient
from pj.values.db_entity_names import DYNAMO_ENTITY_NAMES

class DynamoManagerFactory:
    VALID_INSTANCE_TYPES = [
        DYNAMO_ENTITY_NAMES['Item'],
        DYNAMO_ENTITY_NAMES['Interaction'],
        DYNAMO_ENTITY_NAMES['SubItem'],
        DYNAMO_ENTITY_NAMES['User']
    ]
    instances = {}

    @classmethod
    def perform(cls, db_entity_name):
        if not db_entity_name in cls.VALID_INSTANCE_TYPES:
            raise Exception('unknown DynamoDB db_entity_name value -', db_entity_name)

        if not cls.instances.get(db_entity_name):
            cls.instances[db_entity_name] = DynamoManager(DynamoManagerClient(db_entity_name))
        return cls.instances[db_entity_name]
