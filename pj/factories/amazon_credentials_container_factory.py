from pj.models.amazon.amazon_default_credentials_container import AmazonDefaultCredentialsContainer

class AmazonCredentialsContainerFactory:
    default_instance = None

    @classmethod
    def get_default_instance(cls):
        if not cls.default_instance:
            cls.default_instance = AmazonDefaultCredentialsContainer()
        return cls.default_instance
