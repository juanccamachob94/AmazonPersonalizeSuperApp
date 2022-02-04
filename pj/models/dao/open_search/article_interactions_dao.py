from pj.models.dao.open_search_dao import OpenSearchDAO
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES
from pj.models.article_interaction import ArticleInteraction

class ArticleInteractionsDAO(OpenSearchDAO):
    DB_ENTITY_NAME = OPEN_SEARCH_ENTITY_NAMES['ArticleInteraction']

    def create_entity(self):
        return super().create_entity(ArticleInteraction())
