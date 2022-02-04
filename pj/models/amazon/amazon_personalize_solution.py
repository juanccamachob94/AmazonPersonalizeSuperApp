import os

from pj.models.amazon.amazon_credentials_container import AmazonCredentialsContainer

class AmazonPersonalizeSolution:
    KEYS_TYPE = None

    def __init__(self, amazon_client):
        keys_type = self.__class__.KEYS_TYPE
        self.amazon_client = amazon_client
        self.tracking_id = os.environ[f'AWS_DEFAULT_PERSONALIZE_{keys_type}_TRACKING_ID']
        self.campaign_arn = os.environ[f'AWS_DEFAULT_PERSONALIZE_{keys_type}_CAMPAIGN_ARN']
        self.user_dataset_arn = os.environ[f'AWS_DEFAULT_PERSONALIZE_{keys_type}_USER_DATASET_ARN']
        self.item_dataset_arn = os.environ[f'AWS_DEFAULT_PERSONALIZE_{keys_type}_ITEM_DATASET_ARN']


    def get_tacking_id(self):
        return self.tracking_id


    def get_campaign_arn(self):
        return self.campaign_arn


    def get_user_dataset_arn(self):
        return self.user_dataset_arn


    def get_item_dataset_arn(self):
        return self.item_dataset_arn


    def get_client(self):
        return self.amazon_client.get_client()
