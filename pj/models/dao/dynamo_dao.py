from pj.models.dao.base_dao import BaseDAO
from pj.factories.dynamo_manager_factory import DynamoManagerFactory

class DynamoDAO(BaseDAO):
    def __init__(self):
        self.db_manager = DynamoManagerFactory.perform(self.DB_ENTITY_NAME)

    def create(self, model):
        # DynamoDB has the responsability to consider the item_id as the unique primary key
        result_dict = {}
        if not model.is_valid():
            return result_dict
        model_dict = model.to_dict()
        for key in model_dict:
            result_dict[key.upper()] = { 'S': str(model_dict[key]) }
        return self.db_manager.create(result_dict)


    def find_all(self, model_attributes_dict, last_evaluated_key=None):
        return self.db_manager.find_all(model_attributes_dict, last_evaluated_key)
