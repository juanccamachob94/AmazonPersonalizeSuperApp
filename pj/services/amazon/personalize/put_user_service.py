from pj.services.amazon.personalize.put_service import PutService

import json

class PutUserService(PutService):
    @classmethod
    def perform(cls, user):
        amazon_personalize_default_solution = cls._build_amazon_personalize_default_solution()
        client = amazon_personalize_default_solution.get_client()
        client.put_users(
            datasetArn = amazon_personalize_default_solution.get_user_dataset_arn(),
            users = [{
                'userId': str(user.get_user_id()),
                'properties': json.dumps(user.to_body_dict())
            }]
        )
