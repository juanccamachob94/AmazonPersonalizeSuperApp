from pj.models.amazon.amazon_default_client import AmazonDefaultClient

class AmazonDefaultClientsFactory:
    VALID_INSTANCE_TYPES = [ 'dynamodb', 'personalize-events', 'personalize-runtime' ]
    instances = {}

    @classmethod
    def get_instance(cls, instance_type):
        if not instance_type in cls.VALID_INSTANCE_TYPES:
            raise Exception('AmazonDefaultClient instance invalid')
        if not cls.instances.get(instance_type):
            cls.instances[instance_type] = AmazonDefaultClient(instance_type)
        return cls.instances[instance_type]
