# these elements must be sorted alfabetically
class CSVHeaderTranslator:
    ARTICLE_HEADERS = {
        '': ''
    }

    @classmethod
    def translated_header(cls, model_name):
        if model_name == 'Article':
            return cls.ARTICLE_HEADERS
        return {}
