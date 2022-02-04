class ArticleInteractionValidator:

    @classmethod
    def is_valid(cls, article_interaction):
        return article_interaction.get_article_id() and article_interaction.get_user_id() and \
            article_interaction.get_timestamp()
