from pj.services.db.csv.csv_model_service import CSVModelService
from pj.services.csv_management_service import CSVManagementService
from pj.helpers.csv_helper import CSVHelper
from pj.services.storages.storage_service import StorageService

class CSVModelSaverService(CSVModelService):
    @classmethod
    def perform(cls, csv_manager_client, model, save_dict={}):
        identifier_dict = save_dict or cls.row_uniq_dict_record(model)
        if not identifier_dict:
            return False
        temporary_file = cls._read(csv_manager_client, model)
        updated_temporary_file = CSVManagementService.replace(
            temporary_file.name,
            CSVHelper.build_official_headers_list(model),
            identifier_dict,
            model.to_dict()
        )
        StorageService \
            .perform(updated_temporary_file.name, csv_manager_client.get_relative_output_route())
        temporary_file.close()
        updated_temporary_file.close()
        return True
