from pj.services.storages.strategies.basic_amazon_s3_strategy import BasicAmazonS3Strategy
from pj.helpers.file_helper import FileHelper

class StorageService:
    @classmethod
    def perform(cls, input_route, output_route):
        extra_args = {
            'ACL': 'public-read',
            'ContentType': FileHelper.content_type(input_route)
        }
        BasicAmazonS3Strategy.perform(input_route, output_route, extra_args)
