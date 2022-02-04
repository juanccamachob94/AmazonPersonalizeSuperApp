from pj.services.articles_recommender_service import ArticlesRecommenderService
from pj.lambdas.models.item_recommender import ItemRecommender

class ArticlesRecommendationsClient:
    @classmethod
    def perform(cls):
        item_recommender = ItemRecommender({ 'user_id': 12 })
        articles = ArticlesRecommenderService.perform(item_recommender)
        item = 1
        for article in articles:
            print(item, '-', article.get_article_id())
            item += 1
