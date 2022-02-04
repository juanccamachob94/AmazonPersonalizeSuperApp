from pj.helpers.string_helper import StringHelper

class UrlHelper:
    @classmethod
    def name_with_extension(cls, url):
        return StringHelper.last_substring(url, '/')


    @classmethod
    def extension(cls, url):
        name_and_extension = cls.name_with_extension(url)
        if '.' not in name_and_extension:
            return ''
        return StringHelper.last_substring(name_and_extension, '.')


    @classmethod
    def name(cls, url):
        name_and_extension = cls.name_with_extension(url)
        return StringHelper.first_substring(name_and_extension, '.')
