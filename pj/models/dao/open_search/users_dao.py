from pj.models.dao.open_search_dao import OpenSearchDAO
from pj.models.user import User
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class UsersDAO(OpenSearchDAO):
    DB_ENTITY_NAME = OPEN_SEARCH_ENTITY_NAMES['User']

    def create_entity(self):
        return super().create_entity(User())


    def create(self, model, _validate_repeated=False):
        return super().create(model)
