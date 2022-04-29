from slugify import slugify
# considering ADN40 in all news (articles)

class ArticleUrlBuilder:
    DOMAIN = "https://s3.amazonaws.com/4pp.adn40.com/app/2020/detalles/"

    @classmethod
    def perform(cls, article):
        slug_title = cls.__sanitized_slug(article.get_title())
        # year = item_dict['publication_date'][0:4]
        slug_category = cls.__sanitized_slug(article.get_category())
        return f'{cls.DOMAIN}{slug_category}/{slug_title}.json'

    @classmethod
    def __sanitized_slug(cls, string):
        return slugify(string.replace('.', ''))
