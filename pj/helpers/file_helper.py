import os

from pj.helpers.url_helper import UrlHelper

class FileHelper:
    @classmethod
    def file_size(cls, file):
        """
            file is instance of file resource, not the path/url/route
            An instance example of file is: <tempfile._TemporaryFileWrapper>
            Implementation based on https://stackabuse.com/example-upload-a-file-to-aws-s3-with-boto
        """
        try:
            return cls.__file_size_based_on_file_descriptor(file)
        except:
            return cls.__file_size_based_on_file_seek(file)


    @classmethod
    def content_type(cls, file_route):
        extension = UrlHelper.extension(file_route)
        if extension == 'csv':
            return 'text/csv'
        return None


    @classmethod
    def __file_size_based_on_file_descriptor(cls, file):
        file_descriptor_identifier = file.fileno()  # <int>
        file_descriptor_status = os.fstat(file_descriptor_identifier)  # <os.stat_result>
        return file_descriptor_status.st_size


    @classmethod
    def __file_size_based_on_file_seek(cls, file):
        file.seek(0, os.SEEK_END)
        return file.tell()
