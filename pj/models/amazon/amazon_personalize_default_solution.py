from pj.models.amazon.amazon_personalize_solution import AmazonPersonalizeSolution
from pj.factories.amazon_default_clients_factory import AmazonDefaultClientsFactory

class AmazonPersonalizeDefaultSolution(AmazonPersonalizeSolution):
    KEYS_TYPE = 'DEFAULT'
