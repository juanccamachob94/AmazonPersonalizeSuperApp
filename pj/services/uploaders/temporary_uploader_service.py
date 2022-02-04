import shutil
import tempfile
import urllib.request
from pj.helpers.url_helper import UrlHelper

class TemporaryUploaderService:
    @classmethod
    def perform(cls, resource_absolute_route):
        """
            - temporary_file_wrapper.name returns the absolute path of the temporary file
            - temporary file absolute path is /tmp or /var/folders/* (depends of Operative System)
        """
        temporary_file_wrapper = tempfile.NamedTemporaryFile(
            suffix=cls.__build_suffix(resource_absolute_route)
        )
        cls.__copy(resource_absolute_route, temporary_file_wrapper.name)
        return temporary_file_wrapper


    @classmethod
    def __build_suffix(cls, resource_absolute_route):
        extension = UrlHelper.extension(resource_absolute_route)
        if not extension: # if extension is empty
            return ''
        return f'.{extension}'


    @classmethod
    def __copy(cls, resource_absolute_route, temporary_file_wrapper_absolute_route):
        if resource_absolute_route.startswith('http'):
            urllib.request.urlretrieve(resource_absolute_route,
                temporary_file_wrapper_absolute_route)
        else:
            shutil.copy(resource_absolute_route, temporary_file_wrapper_absolute_route)
