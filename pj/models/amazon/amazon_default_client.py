from pj.models.amazon.amazon_client import AmazonClient
from pj.factories.amazon_credentials_container_factory import AmazonCredentialsContainerFactory

class AmazonDefaultClient(AmazonClient):
    def __init__(self, service_name):
        super().__init__(service_name, AmazonCredentialsContainerFactory.get_default_instance())
