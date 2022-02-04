from pj.models.dao.dynamo_dao import DynamoDAO
from pj.models.interaction import Interaction
from pj.values.db_entity_names import DYNAMO_ENTITY_NAMES

class InteractionsDAO(DynamoDAO):
    DB_ENTITY_NAME = DYNAMO_ENTITY_NAMES['Interaction']

    def _exists_user(self, _interaction):
        raise Exception('_exists_user method not implemented')


    def _exists_item(self, _interaction):
        raise Exception('_exists_item method not implemented')
