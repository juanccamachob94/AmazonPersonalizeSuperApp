import boto3

class AmazonClient:
    def __init__(self, service_name, amazon_credentials_container):
        self.client = boto3.client(
            service_name,
            aws_access_key_id=amazon_credentials_container.get_access_key_id(),
            aws_secret_access_key=amazon_credentials_container.get_secret_key()
        )


    def get_client(self):
        return self.client
