from pj.services.readers.xml_reader import XMLReader

class SitemapXMLReader(XMLReader):
    CONTAINERS = ['urlset', 'url']
