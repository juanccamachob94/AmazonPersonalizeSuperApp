import os

from dotenv import load_dotenv
from requests_aws4auth import AWS4Auth
from opensearchpy import OpenSearch, RequestsHttpConnection
from pj.models.amazon.amazon_client import AmazonClient
from pj.factories.amazon_credentials_container_factory import AmazonCredentialsContainerFactory

load_dotenv()

class AmazonOpenSearchClient(AmazonClient):
    CREDENTIALS_TYPE = None
    SERVICE = 'es'

    def __init__(self, amazon_credentials_container):
        self.amazon_credentials_container = amazon_credentials_container
        self.awsauth = None
        self.client = OpenSearch(
            connection_class=RequestsHttpConnection,
            hosts=[
                {
                    'host': self.__class__.__get_host(),
                    'port': self.__class__.__get_port()
                }
            ],
            http_auth=self.get_awsauth(),
            use_ssl=True,
            verify_certs=True
        )

    def get_awsauth(self):
        if not self.awsauth:
            self.awsauth = AWS4Auth(
                self.amazon_credentials_container.get_access_key_id(),
                self.amazon_credentials_container.get_secret_key(),
                self.amazon_credentials_container.get_region(),
                self.__class__.SERVICE
            )
        return self.awsauth


    @classmethod
    def __get_host(cls):
        return os.environ[f'AWS_{cls.CREDENTIALS_TYPE}_OPENSEARCH_HOST']


    @classmethod
    def get_https_url(cls):
        return f'https://{cls.__get_host()}'


    @classmethod
    def __get_port(cls):
        return int(os.environ[f'AWS_{cls.CREDENTIALS_TYPE}_OPENSEARCH_PORT'])
