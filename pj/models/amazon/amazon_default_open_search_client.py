from pj.models.amazon.amazon_open_search_client import AmazonOpenSearchClient

class AmazonDefaultOpenSearchClient(AmazonOpenSearchClient):
    CREDENTIALS_TYPE = 'DEFAULT'
