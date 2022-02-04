from pj.management.services.readers.account_sitemap_index_reader import AccountSitemapIndexReader
from pj.management.services.readers.account_sitemap_reader import AccountSitemapReader
from pj.management.services.sitemap_content_item_processor import SitemapContentItemProcessor
from pj.translations.article import article_variables_translation

class CentralizedDataGenerator:
    @classmethod
    def perform(cls, site, url, lastmod_requests):
        lastmod_sitemaps = AccountSitemapIndexReader.perform(url, lastmod_requests)
        for lastmod in lastmod_sitemaps:
            for sitemap in lastmod_sitemaps[lastmod]:
                sitemap_content_items_data = \
                    AccountSitemapReader.perform(sitemap['url'])
                for sitemap_content_item_data in sitemap_content_items_data:
                    for variable in article_variables_translation:
                        if variable == 'media_url':
                            media_array = sitemap_content_item_data.pop('multimedia', [])
                            if media_array:
                                sitemap_content_item_data['media_url'] = media_array[0].get('url')
                        else:
                            sitemap_content_item_data[variable] = \
                                sitemap_content_item_data.pop(
                                    article_variables_translation[variable], None
                                )
                    sitemap_content_item_data['section'] = sitemap['titulo']
                    SitemapContentItemProcessor.perform(site, sitemap_content_item_data)
