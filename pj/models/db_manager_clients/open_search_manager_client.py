from pj.factories.amazon_open_search_client_factory import AmazonOpenSearchClientFactory

# Amazon OpenSearch database client
class OpenSearchManagerClient:
    def __init__(self, table_name):
        self.open_search_client = AmazonOpenSearchClientFactory.get_default_instance()
        self.table_name = table_name


    def get_client(self):
        return self.open_search_client.get_client()


    def get_https_url(self):
        return self.open_search_client.__class__.get_https_url()


    def get_awsauth(self):
        return self.open_search_client.get_awsauth()

    def get_table_name(self):
        return self.table_name
