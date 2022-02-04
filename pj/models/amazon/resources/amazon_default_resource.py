from pj.models.amazon.resources.amazon_resource import AmazonResource
from pj.factories.amazon_credentials_container_factory import AmazonCredentialsContainerFactory

class AmazonDefaultResource(AmazonResource):
    def __init__(self, service_name):
        super().__init__(service_name, AmazonCredentialsContainerFactory.get_default_instance())
