from pj.management.services.page_dict_content_generators.generator import Generator

import json

class JsonBasedGenerator(Generator):
    SUFFIX_FILE = '.json'

    @classmethod
    def _build_article_data(cls, url, temporary_file_wrapper):
        article_data = None
        try:
            article_page_json_data = json.load(open(temporary_file_wrapper.name))
            adjusted_body = article_page_json_data['articleBody'][0]
            article_data = {
                'article_id': article_page_json_data['contentId'],
                'author': article_page_json_data['authorName'],
                'category': article_page_json_data['currentSection'],
                'content': None, # html content not included
                'title': None, # pending
                'url': url, # pending
                'url_imagen': None # pending
            }
        except:
            pass
        temporary_file_wrapper.close()
        return article_data


    @classmethod
    def _sanitize_url(cls, url):
        return url + '_renderer=json'
