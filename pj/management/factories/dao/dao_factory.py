import pj.factories.dao.dao_factory

from pj.services.db.csv_manager import CSVManager
from pj.services.db.dynamo_manager import DynamoManager
from pj.services.db.open_search_manager import OpenSearchManager
from pj.management.factories.dao.csv_dao_factory import CSVDAOFactory
from pj.management.factories.dao.dynamo_dao_factory import DynamoDAOFactory
from pj.management.factories.dao.open_search_dao_factory import OpenSearchDAOFactory

class DAOFactory(pj.factories.dao.dao_factory.DAOFactory):
    @classmethod
    def _get_instance(cls, db_manager_type, db_entity_name):
        if db_manager_type == CSVManager.NAME:
            return CSVDAOFactory.perform(db_entity_name)
        elif db_manager_type == DynamoManager.NAME:
            return DynamoDAOFactory.perform(db_entity_name)
        elif db_manager_type == OpenSearchManager.NAME:
            return OpenSearchDAOFactory.perform(db_entity_name)
