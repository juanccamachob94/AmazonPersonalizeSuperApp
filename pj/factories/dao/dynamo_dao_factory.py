from pj.models.dao.dynamo.items_dao import ItemsDAO
from pj.models.dao.dynamo.sub_items_dao import SubItemsDAO
from pj.models.dao.dynamo.users_dao import UsersDAO
from pj.models.dao.dynamo.article_interactions_dao import ArticleInteractionsDAO
from pj.models.dao.dynamo.interactions_dao import InteractionsDAO

class DynamoDAOFactory:
    @classmethod
    def perform(cls, db_entity_name):
        if db_entity_name == UsersDAO.DB_ENTITY_NAME:
            return UsersDAO()
        elif db_entity_name == ItemsDAO.DB_ENTITY_NAME:
            return ItemsDAO()
        elif db_entity_name == InteractionsDAO.DB_ENTITY_NAME:
            return InteractionsDAO()
        elif db_entity_name == SubItemsDAO.DB_ENTITY_NAME:
            return SubItemsDAO()
        elif db_entity_name == ArticleInteractionsDAO.DB_ENTITY_NAME:
            return ArticleInteractionsDAO()
        raise Exception('DynamoDAO instance not valid - ', db_entity_name)
