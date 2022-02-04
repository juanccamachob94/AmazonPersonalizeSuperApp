from pj.models.dao.csv_dao import CSVDAO
from pj.values.db_entity_names import CSV_ENTITY_NAMES

class ArticleInteractionsDAO(CSVDAO):
    DB_ENTITY_NAME = CSV_ENTITY_NAMES['ArticleInteraction']
