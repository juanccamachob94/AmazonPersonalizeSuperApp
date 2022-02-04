from pj.services.db.db_manager import DBManager

import requests

# Amazon database
class OpenSearchManager(DBManager):
    NAME = 'open-search'

    def create_entity(self, entity_body):
        return self.db_manager_client.get_client() \
            .indices.create(self.db_manager_client.get_table_name(), body=entity_body)


    def find_all(self, model_attributes_dict, limit):
        return {
            'Items': list(map(
                lambda hit: hit.get('_source'),
                self.__search(model_attributes_dict, limit).get('hits', {}).get('hits')
            ))
        }


    def find(self, model_attributes_dict):
        return self.find_all(model_attributes_dict, 1)


    def create(self, id, body):
        return self.db_manager_client.get_client().index(body=body, doc_type='_doc',
            id=id, index=self.db_manager_client.get_table_name())


    def delete_entity(self):
        return self.db_manager_client.get_client().indices \
            .delete(index=self.db_manager_client.get_table_name())


    def delete(self, id):
        return self.db_manager_client.get_client().indices \
            .delete(index=self.db_manager_client.get_table_name(), id=id)


    def __search(self, model_attributes_dict, limit):
        body = { 'size': limit, 'query': { 'match': model_attributes_dict } }
        return self.db_manager_client.get_client() \
            .search(body=body, index=self.db_manager_client.get_table_name())
