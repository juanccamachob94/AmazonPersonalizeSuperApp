# this package is included to access to extenal file resource
import ssl
import sys
import locale

sys.path.append('./')

locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')

from pj.clients.interactions_client import InteractionsClient
from pj.clients.items_client import ItemsClient
from pj.clients.users_client import UsersClient
from pj.management.clients.articles_data_client import ArticlesDataClient
from pj.management.clients.articles_recommendations_client import ArticlesRecommendationsClient
from pj.management.clients.open_search_client import OpenSearchClient

# context to allow access to external file resources (https://...)
ssl._create_default_https_context = ssl._create_unverified_context

def main(option):
    if option == 1:
        # Register articles
        ArticlesDataClient.perform()
    elif option == 2:
        ArticlesRecommendationsClient.perform()
    elif option == 3:
        UsersClient.perform()
    elif option == 4:
        ItemsClient.perform()
    elif option == 5:
        InteractionsClient.perform()
    elif option == 6:
        OpenSearchClient.perform('Interaction', 'up')

main(1)
