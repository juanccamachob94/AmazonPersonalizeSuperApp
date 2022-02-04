from pj.management.services.readers.xml.sitemap_index_xml_reader import SitemapIndexXMLReader
from pj.management.services.readers.json.super_app_index_json_reader \
    import SuperAppIndexJSONReader
from pj.management.services.filters.sitemap_index_filter import SitemapIndexFilter

class AccountSitemapIndexReader:
    @classmethod
    def perform(cls, url, lastmod_requests):
        """
            returns a dict of arrays of OrderedDict instances
            expect lastmod_requests as a dict of lastmod and data_types, ej. { '2020-10': None }
        """
        sitemaps_arrays = {}
        if url.endswith('xml'):
            data_list = SitemapIndexXMLReader.perform(url)
            for lastmod in lastmod_requests:
                sitemaps_arrays[lastmod] = SitemapIndexFilter \
                    .perform(data_list, lastmod, lastmod_requests[lastmod])
        elif 'superapp' in url:
            sitemaps_arrays = { 'sitemap-latest': SuperAppIndexJSONReader.perform(url) }
        return sitemaps_arrays
