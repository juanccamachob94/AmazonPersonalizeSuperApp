from pj.management.services.articles_sitemap_page_content_dict_generator \
    import ArticlesSitemapPageContentDictGenerator
from pj.helpers.date_helper import DateHelper

class ArticlesSitemapContentDictGenerator:
    @classmethod
    def perform(cls, sitemap_content_item):
        news_dict = sitemap_content_item.get('news:news', {})
        publication_date = DateHelper.cmtstr_to_datetime(news_dict.get('news:publication_date'))
        dict_news_sitemap_content = { 'publication_date': str(publication_date) }
        item_data = ArticlesSitemapPageContentDictGenerator.perform(sitemap_content_item.get('loc'))
        if not item_data:
            return None
        dict_news_sitemap_content.update(item_data)
        return dict_news_sitemap_content
