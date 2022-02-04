from slugify import slugify
# considering ADN40 in all news (articles)
class ArticleUrlBuilder:
    DOMAIN = "https://s3.amazonaws.com/4pp.adn40.com/app/"

    @classmethod
    def perform(cls, article):
        slug_title = slugify(article.get_title())
        # year = item_dict['publication_date'][0:4]
        category = article.get_category().lower()
        return f'{cls.DOMAIN}2020/detalles/{category}/{slug_title}.json'
