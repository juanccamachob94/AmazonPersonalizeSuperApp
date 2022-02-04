from pj.management.services.page_dict_content_generators.generator import Generator
from bs4 import BeautifulSoup

class HTMLBasedGenerator(Generator):
    SUFFIX_FILE = '.html'

    @classmethod
    def _build_article_data(cls, url, temporary_file_wrapper):
        article_data = None
        with open(temporary_file_wrapper.name) as fp:
            beautiful_soup = BeautifulSoup(fp, "html.parser")
            body_tag = beautiful_soup.find('body')
            head_tag = beautiful_soup.find('head')
            page_main_content = body_tag.find(
                'article', class_='Page-mainContent')
            meta_tag_element = page_main_content.find(
                'div', class_='CreativeWorkPage-metas')
            sub_headline = page_main_content.find(
                'div', class_='CreativeWorkPage-subHeadline')
            article_body = page_main_content.find(
                'div', class_='ArticlePage-articleBody')
            article_title = page_main_content.find(
                'h1', class_='CreativeWorkPage-headline')
            article_cover = page_main_content.find('div', class_='ArticlePage-lead')
            try:
                article_data = {
                    'article_id':
                        head_tag.find('meta', {'name': 'brightspot.contentId'})['content'],
                    'author':
                        meta_tag_element. \
                            find('div', class_='CreativeWorkPage-authorName').get_text(),
                    'category':
                        meta_tag_element.find('div', class_='CreativeWorkPage-section').get_text(),
                    'content': cls.__build_html_content(sub_headline, article_body),
                    'title': article_title.get_text(),
                    'url': url,
                    'url_imagen': article_cover.find('picture').find('img')['data-src']
                }
            except:
                pass
        temporary_file_wrapper.close()
        return article_data


    @classmethod
    def __build_html_content(cls, sub_headline, article_body):
        return ''.join([str(sub_headline), str(article_body)])
