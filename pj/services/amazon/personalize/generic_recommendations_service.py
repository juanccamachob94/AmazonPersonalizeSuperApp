from pj.services.amazon.personalize.recommendations_service import RecommendationsService
import pj.algoritia.amazon.personalize.recommendations_service
from pj.helpers.string_helper import StringHelper

class GenericRecommendationsService:
    DEFAULT_ERROR_FACTOR = 4 # cuadruple of data limit value

    @classmethod
    def perform(cls, item_recommender):
        return cls(item_recommender).__process()


    def __init__(self, item_recommender):
        self.item_recommender = item_recommender
        self.default_recommendations = []
        self.algoritia_recommendations = []


    def __process(self):
        if not self.item_recommender.is_valid():
            raise Exception("Invalid ItemRecommender")
        try:
            recommendation_category = self.item_recommender.get_recommendation_category()
            if recommendation_category in [1, 2]:
                return self.__perform1()
            elif recommendation_category in [3, 4]:
                return self.__perform2()
        except:
            pass
        try:
            return self.__default_perform()
        except:
            return {}


    def __perform1(self):
        return { "default": self.__get_default_recommendations() }


    def __perform2(self):
        return { "algoritia": self.__get_algoritia_recommendations() }


    def __default_perform(self):
        return {
            "default": self.__get_default_recommendations(),
            "algoritia": self.__get_algoritia_recommendations()
        }


    def __rescue_perform(self):
        """
            Unused method. It builds data with default algorithm and rescue empty elements with
            Algoritia recommendations
        """
        recommendations = []
        try:
            recommendations += self.__get_default_recommendations()
        except:
            pass

        if len(recommendations) == self.item_recommender.get_default_data_limit():
            return recommendations

        try:
            recommendations += self.__get_algoritia_recommendations()
        except:
            return recommendations

        not_repeated_recommendations = []
        recommendation_founded = False
        for recommendation in recommendations:
            recommendation_founded = False
            for not_repeated_recommendation in not_repeated_recommendations:
                if not_repeated_recommendation['itemId'] == recommendation['itemId']:
                    recommendation_founded = True
                    break
            if not recommendation_founded:
                not_repeated_recommendations.append(recommendation)
        return not_repeated_recommendations


    def __get_default_recommendations(self):
        if not(self.default_recommendations):
            self.default_recommendations = list(
                filter(
                    lambda r: self.__class__.__is_valid_recommendation(r),
                    RecommendationsService.perform(
                        self.item_recommender.get_user_id(),
                        self.item_recommender.get_default_data_limit()
                            * self.__class__.DEFAULT_ERROR_FACTOR
                    )['itemList']
                )
            )
        return self.default_recommendations


    def __get_algoritia_recommendations(self):
        '''
        if not(self.algoritia_recommendations):
            self.algoritia_recommendations = pj.algoritia.amazon.personalize. \
                recommendations_service.RecommendationsService.perform(
                    self.item_recommender.get_user_id()
                )['itemList']
        return self.algoritia_recommendations
        '''
        return []


    @classmethod
    def __is_valid_recommendation(self, recommendation):
        site = StringHelper.last_substring(recommendation.get('itemId', ''), '|').lower()
        return site in ['adn40', 'superapp']
