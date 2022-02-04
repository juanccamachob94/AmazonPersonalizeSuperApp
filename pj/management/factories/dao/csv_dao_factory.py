from pj.management.models.dao.csv.articles_dao import ArticlesDAO

class CSVDAOFactory:
    @classmethod
    def perform(cls, db_entity_name):
        if db_entity_name == ArticlesDAO.DB_ENTITY_NAME:
            return ArticlesDAO()
        raise Exception('CSVDAO instance not valid -', db_entity_name)
