from pj.services.readers.xml_reader import XMLReader

class SitemapIndexXMLReader(XMLReader):
    CONTAINERS = ['sitemapindex', 'sitemap']
