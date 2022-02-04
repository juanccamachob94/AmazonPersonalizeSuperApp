from pj.management.models.dao.csv_dao import CSVDAO
from pj.management.models.article import Article
from pj.values.db_entity_names import CSV_ENTITY_NAMES

"""
    This implementation is developed to validate the another dependencies without DynamoDB.
    The current implementation works but the large volume of data is unmanageable in a CSV file
"""
class ArticlesDAO(CSVDAO):
    DB_ENTITY_NAME = CSV_ENTITY_NAMES['Article']

    def find_all(self, article_attributes_dict):
        """
            The next implementation emulate the DynamoDB response
        """
        return { 'Items': list(
                map(lambda row_article_data : self.__to_dynamo_dict(row_article_data),
                self.db_manager.find_all(Article.build({}), article_attributes_dict))
            )
        }


    def create(self, model):
        # create method calls save method to not repeat elements in file
        if not model.is_valid():
            return False
        self.db_manager.create(model, False)
        return True


    def __to_dynamo_dict(self, row_article_data):
        return {
            'ARTICLE_ID': row_article_data[0],
            'TITLE': row_article_data[1],
            'CREATED_AT': row_article_data[2],
            'CONTENT': row_article_data[3],
            'CATEGORY': row_article_data[4],
            'SUB_CATEGORY': row_article_data[5],
            'IMPACT': row_article_data[6],
            'IMPORTANCE': row_article_data[7],
            'AUTHOR': row_article_data[8],
            'PUBLICATION_DATE': row_article_data[9],
        }
