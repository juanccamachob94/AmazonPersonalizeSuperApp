from pj.lambdas.base_lambda import BaseLambda
from pj.services.amazon.personalize.generic_recommendations_service \
    import GenericRecommendationsService
from pj.lambdas.models.item_recommender import ItemRecommender
from pj.lambdas.services.article_url_builder import ArticleUrlBuilder
from pj.helpers.date_helper import DateHelper
from pj.translations.article import article_variables_translation


def lambda_handler(event, context):
    # This change is temporary
    return ItemRecommenderLambda.find_items_data_list(event)


class ItemRecommenderLambda(BaseLambda):
    ALGORITHMS = {
        'algoritia': 'itemsSession',
        'default': 'itemsUser'
    }

    @classmethod
    def find_items_data_list(cls, event):
        return cls.build_http_response(
            { 'items': cls.__formated_recommended_articles(ItemRecommender(event)) }
        )


    @classmethod
    def __formated_recommended_articles(cls, item_recommender):
        result = []
        recommended_articles_by_algorithm = GenericRecommendationsService.perform(item_recommender)
        for algorithm in recommended_articles_by_algorithm:
            articles_list = recommended_articles_by_algorithm[algorithm]
            if articles_list:
                items_key = cls.ALGORITHMS[algorithm]
                result.append( { items_key: articles_list })
        return result
