from pj.models.dao.base_dao import BaseDAO
from pj.factories.csv_manager_factory import CSVManagerFactory

class CSVDAO(BaseDAO):
    def __init__(self):
        self.db_manager = CSVManagerFactory.perform(self.DB_ENTITY_NAME)


    def save(self, model):
        return self.db_manager.save(model)


    def create(self, model, validate_repeated=True):
        return self.db_manager.create(model, validate_repeated)
