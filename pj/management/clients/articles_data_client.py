from pj.management.services.centralized_data_generator import CentralizedDataGenerator
from pj.helpers.date_helper import DateHelper
from pj.management.services.filters.sitemap_filter import SitemapFilter
class ArticlesDataClient:
    @classmethod
    def perform(cls):
        lastmod_requests = cls.__build_lastmod_requests() # change to array
        CentralizedDataGenerator.perform('APP_SuperApp', \
            'https://www.tvazteca.com/superapp/sappcontentindexjson', lastmod_requests)
        return lastmod_requests


    @classmethod
    def __build_lastmod_requests(cls):
        response = { 'sitemap-latest': None }
        if SitemapFilter.LIMIT_DATE:
            response[cls.__build_lastmod_request(SitemapFilter.LIMIT_DATE)] = None
            response[cls.__build_lastmod_request(DateHelper.ago())] = None # now
        return response


    @classmethod
    def __build_lastmod_request(cls, datetime):
        date = datetime.date()
        str_month = str(date.month)
        if len(str_month) == 1:
            str_month = '0' + str_month
        return str(date.year) + (str_month)
