from pj.factories.dao.dao_factory import DAOFactory
from pj.values.db_entity_names import CSV_ENTITY_NAMES
from pj.models.user import User

class UsersClient:
    @classmethod
    def perform(cls):
        print('Users!!')
        user_id = 350
        device_id = 1
        DAOFactory.perform('csv', CSV_ENTITY_NAMES['User']) \
            .save(User.build({ 'user_id': user_id, 'device_id': device_id }))
