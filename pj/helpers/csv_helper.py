from pj.translations.csv_header_translator import CSVHeaderTranslator
class CSVHelper:
    @classmethod
    def build_official_headers_list(cls, model):
        # returns headers array
        return list(model.to_dict().keys())


    @classmethod
    def build_translated_headers_list(cls, model):
        # upper of translated headers of model dict keys
        translated_header_dict = CSVHeaderTranslator.translated_header(model.__class__.__name__)
        keys = cls.build_official_headers_list(model)
        # returns headers array
        if not translated_header_dict:
            return list(map(lambda key: key.upper(), keys))
        return list(map(lambda key: cls.__translate_key(translated_header_dict, key).upper(), keys))


    @classmethod
    def __translate_key(cls, dict, key):
        translation = dict.get(key)
        if translation:
            return translation
        return key
