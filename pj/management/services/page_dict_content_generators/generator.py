import http
import tempfile
import urllib.request

class Generator:
    SUFFIX_FILE = None

    @classmethod
    def perform(cls, url):
        temporary_file_wrapper = tempfile.NamedTemporaryFile(suffix=cls.SUFFIX_FILE)
        try:
            urllib.request.urlretrieve(cls._sanitize_url(url), temporary_file_wrapper.name)
            return cls._build_article_data(url, temporary_file_wrapper)
        except http.client.InvalidURL:
            return None
        except urllib.error.HTTPError:
            return None
        except urllib.error.URLError:
            return None
        except:
            return None


    @classmethod
    def _build_article_data(cls, _url, _fp):
        raise Exception('_build_news_data method not implemented')


    @classmethod
    def _sanitize_url(cls, url):
        return url
