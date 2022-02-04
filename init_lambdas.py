import sys
import ssl

sys.path.append('./')
ssl._create_default_https_context = ssl._create_unverified_context

from pj.lambdas import users_lambda
from pj.lambdas import item_recommender_lambda
from pj.lambdas import interactions_lambda
from pj.lambdas import base_lambda
from pj.helpers.string_helper import StringHelper
from pj.management.clients.articles_data_client import ArticlesDataClient


def lambda_handler(event, context):
    try:
        event_type = event.get('type')
        event_content = event.get('content')
        if event_type and not(event.get('application') in ['APP SuperApp']):
            raise Exception('Invalid application parameter')
        if event_type == 'user':
            return users_lambda.lambda_handler(event_content, context)
        elif event_type == 'recommender':
            return item_recommender_lambda_handler(event_content, context)
        elif event_type == 'interaction':
            return interactions_lambda_handler(event_content, context)
        else:
            return base_lambda.BaseLambda.build_http_response(ArticlesDataClient.perform(), 200)
    except Exception as exception:
        return base_lambda.BaseLambda.build_http_response(''.join(['error ', str(exception)]), 500)


def item_recommender_lambda_handler(event_content, context):
    additional_user_lambda_handler(event_content, context)
    return item_recommender_lambda.lambda_handler(event_content, context)


def interactions_lambda_handler(event_content, context):
    if StringHelper.first_string(event_content['interaction']['item_id'], '|'):
        additional_user_lambda_handler(event_content, context)
        return interactions_lambda.lambda_handler(event_content, context)
    else:
        raise Exception('Invalid ')


def additional_user_lambda_handler(event_content, context):
    user_id = event_content.get('user_id') or event_content.get('interaction', {}).get('user_id')
    device_id = event_content.get('user_device_id') \
        or event_content.get('interaction', {}).get('user_device_id') or 1
    user_event_content = {
        "action": "save",
        "user": {
            "user_id": user_id,
            "device_id": int(device_id)
        }
    }
    users_lambda.lambda_handler(user_event_content, context)
