from pj.services.db.db_manager import DBManager
from boto3.dynamodb.conditions import Attr

# Amazon database (no relational)
class DynamoManager(DBManager):
    NAME = 'dynamodb'

    def find_all(self, dict_attributes, last_evaluated_key=None):
        """
            keys = ['Items', 'Count', 'ScannedCount', 'LastEvaluatedKey', 'ResponseMetadata']
        """
        # TODO: implement a real logic
        filter_expression = Attr(list(dict_attributes.keys())[0]) \
            .eq(list(dict_attributes.values())[0])
        if last_evaluated_key:
            return self.db_manager_client.get_table() \
                .scan(FilterExpression=filter_expression, ExclusiveStartKey=last_evaluated_key)
        return self.db_manager_client.get_table().scan(FilterExpression=filter_expression)

    def create(self, dynamodb_dict_item):
        """
            dynamodb_item is a dict with the next format:
            {
                'key': {
                    'TYPE_OF_DATA': 'value'
                }, ...
            }
            an example of this expected parameter:
            {
                'USER_ID': {
                    'S': 'fjg2j31-123f3'
                },
                'NAME': {
                    'S': 'Test User'
                }
            }
        """
        amazon_client = self.db_manager_client.get_dynamo_client()
        return amazon_client.get_client().put_item(
            Item=dynamodb_dict_item,
            TableName=self.db_manager_client.get_table_name()
        )
