import boto3

class AmazonResource:
    def __init__(self, resource_name, amazon_credentials_container):
        self.resource = boto3.resource(
            resource_name,
            aws_access_key_id=amazon_credentials_container.get_access_key_id(),
            aws_secret_access_key=amazon_credentials_container.get_secret_key()
        )


    def get_resource(self):
        return self.resource
