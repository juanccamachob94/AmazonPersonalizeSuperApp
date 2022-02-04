from pj.services.db.db_manager import DBManager

import requests

# Amazon database
class OpenSearchManager(DBManager):
    NAME = 'open-search'

    def create_entity(self, entity_body):
        return self.db_manager_client.get_client() \
            .indices.create(self.db_manager_client.get_table_name(), body=entity_body)

    def _build_search_url(self, sql_parameters):
        return self.db_manager_client.get_https_url() \
            + f'/{self.db_manager_client.get_table_name()}/_search?q={sql_parameters}'


    def find_all(self, sql_parameters):
        hits = requests.get(self._build_search_url(sql_parameters),
            auth=self.db_manager_client.get_awsauth()).json().get('hits', {}).get('hits', [])
        return { 'Items': list(map(lambda hit: hit.get('_source'), hits)) }


    def find(self, sql_parameters):
        items = self.find_all(sql_parameters)['Items']
        return items[0] if items else None


    def create(self, id, body):
        return self.db_manager_client.get_client().index(body=body, doc_type='_doc',
            id=id, index=self.db_manager_client.get_table_name())


    def delete_entity(self):
        return self.db_manager_client.get_client().indices \
            .delete(index=self.db_manager_client.get_table_name())


    def delete(self, id):
        return self.db_manager_client.get_client().indices \
            .delete(index=self.db_manager_client.get_table_name(), id=id)
