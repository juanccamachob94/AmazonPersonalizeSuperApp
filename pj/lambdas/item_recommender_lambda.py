from pj.lambdas.base_lambda import BaseLambda
from pj.services.articles_recommender_service import ArticlesRecommenderService
from pj.lambdas.models.item_recommender import ItemRecommender
from pj.lambdas.services.article_url_builder import ArticleUrlBuilder
from pj.helpers.date_helper import DateHelper
from pj.translations.article import article_variables_translation

def lambda_handler(event, context):
    # This change is temporary
    return ItemRecommenderLambda.find_items_data_list(event)


class ItemRecommenderLambda(BaseLambda):
    @classmethod
    def find_items_data_list(cls, event):
        return cls.build_http_response(
            { 'items': cls.__formated_recommended_articles(ItemRecommender(event)) }
        )


    @classmethod
    def __formated_recommended_articles(cls, item_recommender):
        result = []
        recommended_articles_by_algorithm = ArticlesRecommenderService.perform(item_recommender)
        for algorithm in recommended_articles_by_algorithm:
            articles_list = recommended_articles_by_algorithm[algorithm]
            if articles_list:
                result.append(cls.__build_algorithm_format(articles_list))
        return result


    @classmethod
    def __build_algorithm_format(cls, articles_list):
        return { 'items': cls.__build_articles_list_format(articles_list) }


    @classmethod
    def __build_articles_list_format(cls, articles_list):
        result = []
        formated_article = None
        article_dict = None
        for article in articles_list:
            formated_article = {}
            article.set_publication_date(
                DateHelper.gmt_replace(
                    DateHelper.cmtstr_to_datetime(article.get_publication_date().replace(' ', 'T'))
                        .strftime(DateHelper.GMT_FORMAT)
                )
            )
            article_dict = article.to_dict()
            for variable in article_variables_translation:
                formated_article[article_variables_translation[variable]] = article_dict[variable]
            formated_article['multimedia'] = [ { 'url': formated_article.pop('multimediaUrl') } ]
            result.append(formated_article)
        return result
