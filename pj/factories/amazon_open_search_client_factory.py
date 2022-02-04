from pj.factories.amazon_credentials_container_factory import AmazonCredentialsContainerFactory
from pj.models.amazon.amazon_default_open_search_client import AmazonDefaultOpenSearchClient

class AmazonOpenSearchClientFactory:
    instance = None

    @classmethod
    def get_default_instance(cls):
        if not cls.instance:
            cls.instance = AmazonDefaultOpenSearchClient(
                AmazonCredentialsContainerFactory.get_default_instance()
            )
        return cls.instance
