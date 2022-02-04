from pj.services.db.csv_manager import CSVManager
from pj.services.db.dynamo_manager import DynamoManager
from pj.services.db.open_search_manager import OpenSearchManager
from pj.factories.dao.csv_dao_factory import CSVDAOFactory
from pj.factories.dao.open_search_dao_factory import OpenSearchDAOFactory
from pj.factories.dao.dynamo_dao_factory import DynamoDAOFactory

class DAOFactory:
    instances = {}

    @classmethod
    def perform(cls, db_manager_type, db_entity_name):
        # examples: csv|users , dynamo|interactions
        key = ''.join([db_manager_type, '|', db_entity_name])
        if not cls.instances.get(key):
            cls.instances[key] = cls._get_instance(db_manager_type, db_entity_name)
        return cls.instances[key]


    @classmethod
    def _get_instance(cls, db_manager_type, db_entity_name):
        if db_manager_type == CSVManager.NAME:
            return CSVDAOFactory.perform(db_entity_name)
        elif db_manager_type == DynamoManager.NAME:
            return DynamoDAOFactory.perform(db_entity_name)
        elif db_manager_type == OpenSearchManager.NAME:
            return OpenSearchDAOFactory.perform(db_entity_name)
