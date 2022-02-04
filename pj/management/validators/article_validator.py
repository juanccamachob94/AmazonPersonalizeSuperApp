class ArticleValidator:
    @classmethod
    def is_valid(cls, article):
        return article.get_author() and article.get_category() \
            and article.get_html_content() and article.get_description() \
            and article.get_publication_date() and article.get_identifier() \
            and article.get_media_url() and article.get_title() and article.get_url()
