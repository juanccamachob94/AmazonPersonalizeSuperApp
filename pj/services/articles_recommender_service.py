from pj.management.models.article import Article
from pj.services.amazon.personalize.recommendations_service import RecommendationsService
from pj.services.articles_by_recommendation_service import ArticlesByRecommendationService
from pj.services.amazon.personalize.generic_recommendations_service \
    import GenericRecommendationsService

class ArticlesRecommenderService:
    @classmethod
    def perform(cls, item_recommender):
        articles_by_algorithm = {}
        data_limit = item_recommender.get_default_data_limit()
        recommendations_by_algorithm = GenericRecommendationsService.perform(item_recommender)
        for algorithm in recommendations_by_algorithm:
            articles = []
            total_articles = 0
            iterate = True
            for recommendation in recommendations_by_algorithm[algorithm]:
                last_evaluated_key = None
                while iterate:
                    db_articles_data = ArticlesByRecommendationService \
                        .find_all_by_category(recommendation, last_evaluated_key, data_limit)
                    article_data_items = db_articles_data.get('Items')

                    if not len(article_data_items):
                        break

                    for article_data in article_data_items:
                        articles.append(cls.__build_article(article_data))
                        total_articles += 1
                        if(total_articles == item_recommender.get_default_data_limit()):
                            iterate = False
                            break

                    last_evaluated_key = db_articles_data.get('LastEvaluatedKey')
                    if not last_evaluated_key:
                        break
            articles_by_algorithm[algorithm] = articles
        return articles_by_algorithm


    @classmethod
    def __build_article(cls, item_data):
        valid_item_data = {}
        for key_item in item_data:
            valid_item_data[key_item.lower()] = item_data[key_item]
        return Article.build(valid_item_data)
