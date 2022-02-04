from pj.factories.amazon_personalize_solutions_factory import AmazonPersonalizeSolutionsFactory

class RecommendationsService:
    @classmethod
    def perform(cls, user_id, num_results=10):
        amazon_personalize_default_solution = \
            AmazonPersonalizeSolutionsFactory.get_instance('personalize-runtime')
        return amazon_personalize_default_solution.get_client().get_recommendations(
            campaignArn=amazon_personalize_default_solution.get_campaign_arn(),
            numResults=num_results,
            userId=str(user_id)
        )
