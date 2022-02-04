from pj.helpers.csv_helper import CSVHelper
from pj.helpers.application_helper import ApplicationHelper
from pj.services.csv_management_service import CSVManagementService
from pj.services.db.csv.csv_model_finder_service import CSVModelFinderService
from pj.services.db.csv.csv_model_service import CSVModelService
from pj.services.storages.storage_service import StorageService

class CSVModelUpdaterService(CSVModelService):
    @classmethod
    def perform(cls, csv_manager_client, uniq_dict_record, new_model):
        temporary_file = cls._read(csv_manager_client, new_model)
        model = new_model.__class__.build(uniq_dict_record)
        row_uniq_dict = cls.row_uniq_dict_record(model)
        current_model_row = CSVModelFinderService.perform(csv_manager_client, model)
        if not current_model_row:
            return None
        new_model_dict = cls.__build_new_model_dict(current_model_row, new_model)
        updated_temporary_file = \
            CSVManagementService.replace(temporary_file.name,
                CSVHelper.build_official_headers_list(new_model), row_uniq_dict, new_model_dict)
        StorageService \
            .perform(updated_temporary_file.name, csv_manager_client.get_relative_output_route())
        updated_temporary_file.close()
        temporary_file.close()
        return new_model.__class__.build(new_model_dict)


    @classmethod
    def __build_new_model_dict(cls, current_model_row, new_model):
        current_model_dict = ApplicationHelper.keys_values_to_dict(
            CSVHelper.build_official_headers_list(new_model),
            current_model_row
        )
        new_model_dict = new_model.to_dict()
        for key in current_model_dict:
            if new_model_dict[key]:
                current_model_dict[key] = new_model_dict[key]
        return current_model_dict
