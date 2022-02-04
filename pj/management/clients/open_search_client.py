from pj.management.factories.dao.dao_factory import DAOFactory
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES
from pj.management.models.article import Article
from pj.migrations.open_search_db_entity_manager import OpenSearchDBEntityManager

class OpenSearchClient:
    @classmethod
    def perform(cls, key, action):
        if action == 'up':
            OpenSearchDBEntityManager.up(key)
        elif action == 'down':
            OpenSearchDBEntityManager.down(key)
