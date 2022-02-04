from pj.services.db.db_manager import DBManager
from pj.services.db.csv.csv_model_creator_service import CSVModelCreatorService
from pj.services.db.csv.csv_model_eliminator_service import CSVModelEliminatorService
from pj.services.db.csv.csv_model_finder_service import CSVModelFinderService
from pj.services.db.csv.csv_model_all_finder_service import CSVModelAllFinderService
from pj.services.db.csv.csv_model_updater_service import CSVModelUpdaterService
from pj.services.db.csv.csv_model_saver_service import CSVModelSaverService

class CSVManager(DBManager):
    NAME = 'csv'

    def find_all(self, model, some_model_attributes={}):
        return CSVModelAllFinderService \
            .perform(self.db_manager_client, model, some_model_attributes)


    def find(self, model):
        return CSVModelFinderService.perform(self.db_manager_client, model)


    def create(self, model, validate_repeated=True):
        if model.is_valid():
            CSVModelCreatorService.perform(self.db_manager_client, model, validate_repeated)


    def save(self, model):
        if not model.is_valid():
            return False
        return CSVModelSaverService.perform(self.db_manager_client, model)


    def update(self, uniq_dict_record, new_model):
        if not new_model.is_valid():
            return False
        return CSVModelUpdaterService.perform(self.db_manager_client, uniq_dict_record, new_model)


    def delete(self, model):
        return CSVModelEliminatorService.perform(self.db_manager_client, model)
