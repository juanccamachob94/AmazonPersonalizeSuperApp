"""
    A instance of this class should not be considered valid! It contains the default paramenters
    to use on specific case based on credentials type.
    Its instance is managed by AmazonCredentialsContainerFactory class
"""
import os

from dotenv import load_dotenv

load_dotenv()

class AmazonCredentialsContainer:
    CREDENTIALS_TYPE = None

    def __init__(self):
        credentials_type = self.__class__.CREDENTIALS_TYPE
        self.access_key_id = os.environ[f'AWS_{credentials_type}_ACCESS_KEY_ID']
        self.secret_key = os.environ[f'AWS_{credentials_type}_SECRET_KEY']
        self.bucket_name = os.environ[f'AWS_{credentials_type}_BUCKET_NAME']
        self.relative_path = os.environ[f'AWS_{credentials_type}_RELATIVE_PATH']
        self.root_path = os.environ[f'AWS_{credentials_type}_ROOT_PATH']
        self.region = os.environ[f'AWS_{credentials_type}_REGION']


    def get_access_key_id(self):
        return self.access_key_id


    def get_secret_key(self):
        return self.secret_key


    def get_bucket_name(self):
        return self.bucket_name


    def get_relative_path(self):
        return self.relative_path


    def get_root_path(self):
        return self.root_path


    def get_region(self):
        return self.region

    
    def get_absolute_path(self):
        return self.get_root_path() + self.get_relative_path()
