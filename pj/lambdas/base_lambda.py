class BaseLambda:
    @classmethod
    def build_http_response(cls, body, status_code=200):
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': body,
            'statusCode': status_code
        }
