from pj.models.timestamp_model import TimestampModel
from pj.validators.article_interaction_validator import ArticleInteractionValidator

# timestamp attribute has the same value of the related Interaction
class ArticleInteraction(TimestampModel):
    @classmethod
    def build(cls, article_interaction_dict):
        article_interaction = cls()
        article_interaction.set_user_id(article_interaction_dict.get('user_id'))
        article_interaction.set_article_id(article_interaction_dict.get('article_id'))
        article_interaction.set_timestamp(article_interaction_dict.get('timestamp'))
        return article_interaction


    def __init__(self):
        self.article_id = None
        self.user_id = None
        self.timestamp = None


    def is_valid(self):
        return ArticleInteractionValidator.is_valid(self)


    def to_dict(self):
        return {
            'article_id': self.article_id,
            'user_id': self.user_id,
            'timestamp': self.timestamp
        }


    def to_uniq_dict(self):
        return {} # uniq id doesn't exists


    def get_user_id(self):
        return self.user_id


    def set_user_id(self, user_id):
        self.user_id = user_id


    def get_article_id(self):
        return self_article_id


    def set_article_id(self,_article_id):
        self.article_id =_article_id
