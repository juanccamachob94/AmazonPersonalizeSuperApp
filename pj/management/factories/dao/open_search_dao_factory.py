from pj.management.models.dao.open_search.articles_dao import ArticlesDAO

class OpenSearchDAOFactory:
    @classmethod
    def perform(cls, db_entity_name):
        if db_entity_name == ArticlesDAO.DB_ENTITY_NAME:
            return ArticlesDAO()
        raise Exception('OpenSearchDAO instance not valid -', db_entity_name)
