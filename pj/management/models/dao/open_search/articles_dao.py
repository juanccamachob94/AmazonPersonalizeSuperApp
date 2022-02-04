from pj.management.models.dao.open_search_dao import OpenSearchDAO
from pj.management.models.article import Article
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES
from pj.helpers.date_helper import DateHelper

"""
    This implementation is developed to validate the another dependencies without DynamoDB.
    The current implementation works but the large volume of data is unmanageable in a CSV file
"""
class ArticlesDAO(OpenSearchDAO):
    DB_ENTITY_NAME = OPEN_SEARCH_ENTITY_NAMES['Article']

    @classmethod
    def __build_mappings_properties(cls, article_keys):
        properties = {}
        for article_key in article_keys:
            properties[article_key] = { 'type': 'text' }
        properties['publication_date'] = { 'type': 'date' }
        return properties


    def create_entity(self):
        return super().create_entity(Article())


    def create(self, model):
        model_dict = model.to_dict()
        if model_dict['publication_date']:
            print("model_dict['publication_date']", model_dict['publication_date'])
            model_dict['publication_date'] = \
                DateHelper.gmtstr_to_datetime(model_dict['publication_date'])
        return self.db_manager.create(self.__class__._find_id(model), model_dict)


    def create_entity(self):
        article_keys = list(Article().to_dict().keys())
        entity_body = {
            'settings': {
                'index': {
                    'number_of_shards': len(article_keys)
                }
            },
            'mappings': {
                'properties': self.__class__.__build_mappings_properties(article_keys)
            }
        }
        return self.db_manager.create_entity(entity_body)


    def _sql_parameters(self, dict_attributes, limit):
        keys_values = []
        for dict_attibute in dict_attributes:
            keys_values.append(f'{dict_attibute.lower()}:{dict_attributes[dict_attibute]}')
        url_keys_values = '&'.join(keys_values)
        return f'{url_keys_values}&size={limit}&sort=publication_date:desc'
