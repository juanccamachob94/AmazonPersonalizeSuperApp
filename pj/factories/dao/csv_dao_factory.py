from pj.models.dao.csv.items_dao import ItemsDAO
from pj.models.dao.csv.sub_items_dao import SubItemsDAO
from pj.models.dao.csv.users_dao import UsersDAO
from pj.models.dao.csv.interactions_dao import InteractionsDAO

class CSVDAOFactory:
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
        raise Exception('CSVDAO instance not valid -', db_entity_name)
