import boto3

from botocore.exceptions import NoCredentialsError
from pj.helpers.url_helper import UrlHelper
from pj.helpers.file_helper import FileHelper

class AmazonS3Client:
    instance = None

    @classmethod
    def upload_file(cls, amazon_credentials_container, output_relative_route, \
        input_absolute_route, extra_args):
        cls.get_instance(amazon_credentials_container) \
            .__upload(output_relative_route, input_absolute_route, extra_args)


    @classmethod
    def get_instance(cls, amazon_credentials_container):
        if cls.instance == None:
            cls.instance = cls(amazon_credentials_container)
        return cls.instance


    def __init__(self, amazon_credentials_container):
        # the order of these attributes are very important
        self.amazon_credentials_container = amazon_credentials_container


    def __upload(self, output_relative_route, input_absolute_route, extra_args):
        s3 = boto3.client('s3',
            aws_access_key_id=self.amazon_credentials_container.get_access_key_id(),
            aws_secret_access_key=self.amazon_credentials_container.get_secret_key()
        )
        official_relative_route = self.amazon_credentials_container.get_relative_path() + \
            output_relative_route
        try:
            s3.upload_file(input_absolute_route,
                self.amazon_credentials_container.get_bucket_name(), official_relative_route, \
                ExtraArgs=extra_args)
        except FileNotFoundError:
            raise 'The file was not found'
        except NoCredentialsError:
            raise 
