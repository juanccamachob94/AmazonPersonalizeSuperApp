from pj.models.dao.dynamo_dao import DynamoDAO
from pj.values.db_entity_names import DYNAMO_ENTITY_NAMES

class UsersDAO(DynamoDAO):
    DB_ENTITY_NAME = DYNAMO_ENTITY_NAMES['User']
