import json

class BaseLambda:
    @classmethod
    def build_http_response(cls, body, status_code=200):
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(cls.__santitized_body(body)),
            'statusCode': status_code
        }


    @classmethod
    def __santitized_body(cls, body):
        if isinstance(body, dict):
            return body
        return { 'message': body }
