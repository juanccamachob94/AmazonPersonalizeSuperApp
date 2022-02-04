from pj.lambdas.validators.item_recommender_validator import ItemRecommenderValidator

class ItemRecommender:
    DEFAULT_DATA_LIMIT = 3

    def __init__(self, lambda_event):
        self.data_limit = lambda_event.get('data_limit')
        self.recommendation_category = lambda_event.get('recommendation_category')
        self.user_id = lambda_event.get('user_id')


    def is_valid(self):
        return ItemRecommenderValidator.is_valid(self)


    def get_data_limit(self):
        return self.data_limit


    def get_default_data_limit(self):
        return self.data_limit or self.__class__.DEFAULT_DATA_LIMIT


    def get_recommendation_category(self):
        return self.recommendation_category


    def get_user_id(self):
        return self.user_id
