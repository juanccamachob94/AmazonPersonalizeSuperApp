from pj.management.services.readers.xml.sitemap_xml_reader import SitemapXMLReader
from pj.management.services.readers.json.super_app_section_json_reader \
    import SuperAppSectionJSONReader
from pj.management.services.filters.sitemap_filter import SitemapFilter

class AccountSitemapReader:
    @classmethod
    def perform(cls, url, expected_type='news'):
        # currently we use news only, the other params allow to know another options of this url
        if url.endswith('xml'):
            return SitemapFilter.perform(SitemapXMLReader.perform(url), expected_type)
        elif 'superapp' in url:
            return SuperAppSectionJSONReader.perform(url)
