import pj.factories.csv_manager_factory

from pj.values.db_entity_names import CSV_ENTITY_NAMES

class CSVManagerFactory(pj.factories.csv_manager_factory.CSVManagerFactory):
    VALID_INSTANCE_TYPES = [CSV_ENTITY_NAMES['Article']]
