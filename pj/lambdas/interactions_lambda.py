from pj.lambdas.base_lambda import BaseLambda
from pj.services.interactions_service import InteractionsService

def lambda_handler(event, context):
    return InteractionsLambda.create(event['interaction'])


class InteractionsLambda(BaseLambda):
    @classmethod
    def create(cls, interaction_data):
        InteractionsService.perform(
            interaction_data['user_id'],
            interaction_data['item_id']
        )
        return cls.build_http_response('registered', 201)
