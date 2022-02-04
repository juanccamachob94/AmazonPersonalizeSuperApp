from pj.services.amazon.personalize.put_service import PutService

import json

class PutItemService(PutService):
    @classmethod
    def perform(cls, item):
        amazon_personalize_default_solution = cls._build_amazon_personalize_default_solution()
        client = amazon_personalize_default_solution.get_client()
        client.put_items(
            datasetArn = amazon_personalize_default_solution.get_item_dataset_arn(),
            items = [
                {
                    'itemId': str(item.get_item_id()),
                    'properties': json.dumps(item.to_body_dict())
                }
            ]
        )
