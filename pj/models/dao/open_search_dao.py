from pj.models.dao.base_dao import BaseDAO
from pj.factories.open_search_manager_factory import OpenSearchManagerFactory
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

# It requires only one primary key by model
class OpenSearchDAO(BaseDAO):
    def __init__(self):
        self.db_manager = OpenSearchManagerFactory.perform(self.DB_ENTITY_NAME)


    def find_all(self, model_attributes_dict, limit=10):
        return self.db_manager.find_all(model_attributes_dict, limit)


    def find(self, model_attributes_dict):
        return self.db_manager.find(model_attributes_dict)


    def create_entity(self, model):
        entity_body = {
            'settings': {
                'index': {
                    'number_of_shards': len(model.to_dict())
                }
            }
        }
        return self.db_manager.create_entity(entity_body)


    def create(self, model):
        return self.db_manager.create(self.__class__._find_id(model), model.to_dict())


    def delete(self, model):
        return self.db_manager.delete(self.__class__._find_id(model))


    def delete_entity(self):
        return self.db_manager.delete_entity()


    @classmethod
    def _find_id(cls, model):
        if model.to_uniq_dict():
            return list(model.to_uniq_dict().values())[0]
        return model.get_timestamp()
