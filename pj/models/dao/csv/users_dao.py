from pj.models.dao.csv_dao import CSVDAO
from pj.models.user import User
from pj.values.db_entity_names import CSV_ENTITY_NAMES

class UsersDAO(CSVDAO):
    DB_ENTITY_NAME = CSV_ENTITY_NAMES['User']

    def find(self, user_search_dict):
        return self.db_manager.find(User.build(user_search_dict))


    def save(self, user_attributes):
        return self.db_manager.save(User.build(user_attributes))
