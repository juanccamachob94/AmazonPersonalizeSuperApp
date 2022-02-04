class ItemRecommenderValidator:
    @classmethod
    def is_valid(cls, item_recommender):
        return item_recommender.get_user_id() and cls.__is_valid_category_data(item_recommender)
    
    @classmethod
    def __is_valid_category_data(cls, item_recommender):
        recommender_category = item_recommender.get_recommendation_category()
        if recommender_category == None:
            return True
        if recommender_category in [1, 3]:
            return not item_recommender.get_data_limit()
        elif recommender_category in [2, 4]:
            return item_recommender.get_data_limit()
        return False
