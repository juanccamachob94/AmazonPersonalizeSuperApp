from pj.management.models.dao.dynamo.articles_dao import ArticlesDAO

class DynamoDAOFactory:
    @classmethod
    def perform(cls, db_entity_name):
        if db_entity_name == ArticlesDAO.DB_ENTITY_NAME:
            return ArticlesDAO()
        raise Exception('DynamoDAO instance not valid -', db_entity_name)
