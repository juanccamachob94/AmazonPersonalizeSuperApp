from pj.management.factories.dao.dao_factory import DAOFactory
from pj.values.db_entity_names import DYNAMO_ENTITY_NAMES
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class ArticlesByRecommendationService:
    @classmethod
    def find_all_by_category(cls, recommendation, _last_evaluated_key, data_limit):
        # _last_evaluated_key is used by DynamoDB
        return DAOFactory.perform('open-search', OPEN_SEARCH_ENTITY_NAMES['Article']) \
            .find_all({ 'SECTION': recommendation['itemId'].split('|')[0] }, data_limit)
