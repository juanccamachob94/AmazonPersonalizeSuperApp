from pj.models.base_model import BaseModel
from pj.management.validators.article_validator import ArticleValidator


class Article(BaseModel):
    @classmethod
    def build(cls, article_data):
        article = cls()
        article.set_author(article_data.get('author'))
        article.set_category(article_data.get('category'))
        article.set_html_content(article_data.get('html_content'))
        article.set_description(article_data.get('description'))
        article.set_publication_date(article_data.get('publication_date'))
        article.set_identifier(article_data.get('identifier'))
        article.set_media_url(article_data.get('media_url'))
        article.set_section(article_data.get('section'))
        article.set_title(article_data.get('title'))
        article.set_url(article_data.get('url'))
        return article


    def __init__(self):
        super().__init__()
        self.author = None
        self.category = None
        self.html_content = None
        self.description = None
        self.publication_date = None
        self.identifier = None
        self.media_url = None
        self.section = None
        self.title = None
        self.url = None


    def is_valid(self):
        return ArticleValidator.is_valid(self)


    def to_dict(self):
        return {
            'author': self.author,
            'category': self.category,
            'description': self.description,
            'html_content': self.html_content,
            'identifier': self.identifier,
            'media_url': self.media_url,
            'publication_date': self.publication_date,
            'section': self.section,
            'title': self.title,
            'url': self.url
        }

    def to_uniq_dict(self):
        return { 'identifier': self.identifier }


    def get_author(self):
        return self.author


    def set_author(self, author):
        self.author = author


    def get_category(self):
        return self.category


    def set_category(self, category):
        self.category = category


    def get_description(self):
        return self.description


    def set_description(self, description):
        self.description = description


    def get_html_content(self):
        return self.html_content


    def set_html_content(self, html_content):
        self.html_content = html_content


    def get_identifier(self):
        return self.identifier


    def set_identifier(self, identifier):
        self.identifier = identifier


    def get_media_url(self):
        return self.media_url


    def set_media_url(self, media_url):
        self.media_url = media_url


    def get_section(self):
        return self.section


    def set_section(self, section):
        self.section = section


    def get_publication_date(self):
        return self.publication_date


    def set_publication_date(self, publication_date):
        self.publication_date = publication_date


    def get_title(self):
        return self.title


    def set_title(self, title):
        self.title = title


    def get_url(self):
        return self.url


    def set_url(self, url):
        self.url = url
