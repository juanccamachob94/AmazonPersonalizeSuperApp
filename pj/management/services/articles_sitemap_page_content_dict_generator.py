from pj.management.services.page_dict_content_generators.html_based_generator \
    import HTMLBasedGenerator
from pj.management.services.page_dict_content_generators.json_based_generator \
    import JsonBasedGenerator

class ArticlesSitemapPageContentDictGenerator:
    @classmethod
    def perform(cls, url, generator_type='html'):
        if generator_type == 'json':
            return JsonBasedGenerator.perform(url)
        return HTMLBasedGenerator.perform(url)
