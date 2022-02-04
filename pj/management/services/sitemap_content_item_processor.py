from pj.management.services.sitemap_content_item_data_processor \
    import SitemapContentItemDataProcessor
from pj.management.factories.dao.dao_factory import DAOFactory
from pj.management.models.article import Article
from pj.models.item import Item
from pj.values.db_entity_names import CSV_ENTITY_NAMES
from pj.values.db_entity_names import DYNAMO_ENTITY_NAMES
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES
from pj.helpers.date_helper import DateHelper
import pj.factories.dao.dao_factory
from pj.management.services.sub_item_recorder import SubItemRecorder
from pj.management.services.item_recorder import ItemRecorder

class SitemapContentItemProcessor:
    @classmethod
    def perform(cls, site, sitemap_content_item_data):
        if sitemap_content_item_data:
            article = Article.build(sitemap_content_item_data)
            print('processing...', article.get_identifier())
            if cls.__create_article(article):
                ItemRecorder.perform(article.get_section(), site)
                SubItemRecorder.perform(article)
                print('Ok!')
            else:
                print('Article not registered')
            print('finished', article.get_identifier())


    @classmethod
    def __create_article(cls, article):
        return DAOFactory \
            .perform('open-search', OPEN_SEARCH_ENTITY_NAMES['Article']).create(article)
