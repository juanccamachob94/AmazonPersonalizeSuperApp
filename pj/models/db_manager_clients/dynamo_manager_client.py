from pj.factories.amazon_default_resources_factory import AmazonDefaultResourcesFactory
from pj.factories.amazon_default_clients_factory import AmazonDefaultClientsFactory

# Amazon Dynamo database client
class DynamoManagerClient:
    def __init__(self, table_name):
        self.dynamo_client = AmazonDefaultClientsFactory.get_instance('dynamodb')
        self.dynamo_resource = AmazonDefaultResourcesFactory.get_instance('dynamodb')
        self.table_name = table_name


    def get_dynamo_client(self):
        return self.dynamo_client


    def get_table(self):
        return self.dynamo_resource.get_resource().Table(self.table_name)


    def get_table_name(self):
        return self.table_name
