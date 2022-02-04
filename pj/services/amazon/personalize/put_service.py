from pj.factories.amazon_personalize_solutions_factory import AmazonPersonalizeSolutionsFactory

class PutService:
    @classmethod
    def _build_amazon_personalize_default_solution(cls):
        return AmazonPersonalizeSolutionsFactory.get_instance('personalize-events')
