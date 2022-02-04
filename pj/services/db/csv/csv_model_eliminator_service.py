from pj.services.csv_management_service import CSVManagementService
from pj.services.storages.storage_service import StorageService
from pj.services.db.csv.csv_model_service import CSVModelService
from pj.services.db.csv.csv_model_finder_service import CSVModelFinderService

class CSVModelEliminatorService(CSVModelService):
    @classmethod
    def perform(cls, csv_manager_client, model, delete_dict={}):
        temporary_file = cls._read(csv_manager_client, model)
        row_uniq_dict = delete_dict or cls.row_uniq_dict_record(model)
        if not(row_uniq_dict) or not(CSVModelFinderService.perform(csv_manager_client, model)):
            return False
        updated_temporary_file = \
            CSVManagementService.delete(temporary_file.name, row_uniq_dict)
        StorageService \
            .perform(updated_temporary_file.name, csv_manager_client.get_relative_output_route())
        updated_temporary_file.close()
        temporary_file.close()
        return True
