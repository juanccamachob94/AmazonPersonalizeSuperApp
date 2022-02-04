from pj.models.amazon.amazon_personalize_default_solution import AmazonPersonalizeDefaultSolution
from pj.factories.amazon_default_clients_factory import AmazonDefaultClientsFactory
class AmazonPersonalizeSolutionsFactory:
    instances = {}

    @classmethod
    def get_instance(cls, instance_type):
        if not cls.instances.get(instance_type):
            cls.instances[instance_type] = AmazonPersonalizeDefaultSolution(
                AmazonDefaultClientsFactory.get_instance(instance_type)
            )
        return cls.instances[instance_type]
