from pj.models.amazon.resources.amazon_default_resource import AmazonDefaultResource

class AmazonDefaultResourcesFactory:
    instances = {}

    @classmethod
    def get_instance(cls, instance_type):
        if not cls.instances.get(instance_type):
            cls.instances[instance_type] = AmazonDefaultResource(instance_type)
        return cls.instances[instance_type]
