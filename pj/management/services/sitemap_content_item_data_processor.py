from pj.management.services.articles_sitemap_content_dict_generator import ArticlesSitemapContentDictGenerator

class SitemapContentItemDataProcessor:
    @classmethod
    def perform(cls, sitemap_content_item, expected_type='news'):
        if expected_type == 'news':
            return ArticlesSitemapContentDictGenerator.perform(sitemap_content_item)
        return None
