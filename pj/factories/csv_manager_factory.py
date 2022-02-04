from pj.services.db.csv_manager import CSVManager
from pj.models.db_manager_clients.csv_manager_client import CSVManagerClient
from pj.values.db_entity_names import CSV_ENTITY_NAMES

class CSVManagerFactory:
    SUFFIX_FILE = '.csv'
    VALID_INSTANCE_TYPES = [
        CSV_ENTITY_NAMES['ArticleInteraction'],
        CSV_ENTITY_NAMES['Item'],
        CSV_ENTITY_NAMES['Interaction'],
        CSV_ENTITY_NAMES['SubItem'],
        CSV_ENTITY_NAMES['User']
    ]
    instances = {}

    @classmethod
    def perform(cls, db_entity_name):
        if not db_entity_name in cls.VALID_INSTANCE_TYPES:
            raise Exception('unknown CSV db_entity_name value -', db_entity_name)

        if not cls.instances.get(db_entity_name):
            cls.instances[db_entity_name] = cls.__build_csv_manager(db_entity_name)
        return cls.instances[db_entity_name]

    @classmethod
    def __build_csv_manager(cls, instance_type):
        return CSVManager(CSVManagerClient(''.join([instance_type, cls.SUFFIX_FILE])))
