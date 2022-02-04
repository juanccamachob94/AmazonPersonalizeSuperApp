import pj.models.dao.csv_dao

from pj.management.factories.csv_manager_factory import CSVManagerFactory

class CSVDAO(pj.models.dao.csv_dao.CSVDAO):
    def __init__(self):
        self.db_manager = CSVManagerFactory.perform(self.DB_ENTITY_NAME)
