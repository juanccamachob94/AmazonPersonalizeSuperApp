from pj.factories.dao.dao_factory import DAOFactory
from pj.lambdas.base_lambda import BaseLambda
from pj.values.db_entity_names import CSV_ENTITY_NAMES
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES
from pj.models.user import User
from pj.services.amazon.personalize.put_user_service import PutUserService

def lambda_handler(event, context):
    action = event['action']
    if action == 'save':
        return UsersLambda.save(event['user'])
    else:
        return UsersLambda.build_http_response('invalid action', 400)


class UsersLambda(BaseLambda):
    @classmethod
    def save(cls, dict_user_attributes):
        user = User.build(dict_user_attributes)
        userDAO = DAOFactory.perform('open-search', OPEN_SEARCH_ENTITY_NAMES['User'])
        if not userDAO.find(user.to_uniq_dict()):
            userDAO.create(user, False)
            PutUserService.perform(user)
            return cls.build_http_response('saved', 201)
        return cls.build_http_response('previously registered', 200)
