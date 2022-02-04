import pj.management.factories.dao.dao_factory
from pj.factories.dao.dao_factory import DAOFactory
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class OpenSearchDBEntityManager:
    @classmethod
    def up(cls, key):
        try:
            print(DAOFactory.perform('open-search', OPEN_SEARCH_ENTITY_NAMES[key]).create_entity())
        except:
            print(pj.management.factories.dao.dao_factory \
                .DAOFactory.perform('open-search', OPEN_SEARCH_ENTITY_NAMES[key]).create_entity())


    @classmethod
    def down(cls, key):
        try:
            print(DAOFactory.perform('open-search', OPEN_SEARCH_ENTITY_NAMES[key]).delete_entity())
        except:
            print(pj.management.factories.dao.dao_factory \
                .DAOFactory.perform('open-search', OPEN_SEARCH_ENTITY_NAMES[key]).delete_entity())
