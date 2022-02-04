from pj.helpers.string_helper import StringHelper
from pj.helpers.url_helper import UrlHelper
from pj.models.amazon.amazon_s3_client import AmazonS3Client
from pj.models.amazon.amazon_default_credentials_container import AmazonDefaultCredentialsContainer
from pj.services.uploaders.temporary_uploader_service import TemporaryUploaderService
from pj.factories.amazon_credentials_container_factory import AmazonCredentialsContainerFactory

class BasicAmazonS3Strategy:
    @classmethod
    def perform(cls, input_absolute_route, output_relative_route, extra_args):
        temporary_file = TemporaryUploaderService.perform(input_absolute_route)
        AmazonS3Client.upload_file(AmazonCredentialsContainerFactory.get_default_instance(), \
            output_relative_route, temporary_file.name, extra_args)
        temporary_file.close()
