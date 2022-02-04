from pj.services.csv_management_service import CSVManagementService
from pj.services.storages.storage_service import StorageService
from pj.helpers.csv_helper import CSVHelper
from pj.services.db.csv.csv_model_service import CSVModelService
from pj.services.db.csv.csv_model_finder_service import CSVModelFinderService

class CSVModelCreatorService(CSVModelService):
    @classmethod
    def perform(cls, csv_manager_client, model, validate_repeated=True):
        temporary_file = cls._read(csv_manager_client, model)
        if not(validate_repeated) or not(cls.__founded(csv_manager_client, model)):
            CSVManagementService.append(
                temporary_file.name, CSVHelper.build_official_headers_list(model), model.to_dict()
            )
            StorageService \
                .perform(temporary_file.name, csv_manager_client.get_relative_output_route())
        temporary_file.close()


    @classmethod
    def __founded(cls, csv_manager_client, model):
        return model.to_uniq_dict() and \
            CSVModelFinderService.perform(csv_manager_client, model)
