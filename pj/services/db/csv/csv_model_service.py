from pj.services.csv_management_service import CSVManagementService
from pj.services.uploaders.temporary_uploader_service import TemporaryUploaderService
from urllib.error import HTTPError
from pj.helpers.csv_helper import CSVHelper

class CSVModelService:
    @classmethod
    def _read(cls, csv_manager_client, model):
        try:
            return TemporaryUploaderService.perform(csv_manager_client.get_absolute_input_route())
        except (FileNotFoundError, HTTPError):
            headers_list = CSVHelper.build_translated_headers_list(model)
            return CSVManagementService.create_temporary_file(headers_list)


    @classmethod
    def row_uniq_dict_record(cls, model):
        row_uniq_dict = {}
        model_uniq_dict = model.to_uniq_dict()
        if not model_uniq_dict:
            return {}
        model_dict = model.to_dict()
        for _uniq_key in model_uniq_dict:
            position = 0
            for key in model_dict:
                if model_uniq_dict.get(key):
                    row_uniq_dict[position] = model_uniq_dict[key]
                    break
                position += 1
        
        return row_uniq_dict


    @classmethod
    def model_attributes_to_row_dict(cls, model, some_attributes_dict):
        if not some_attributes_dict:
            return {}
        row_dict = {}
        model_dict = model.to_dict()
        for _key in some_attributes_dict:
            position = 0
            for key in model_dict:
                if some_attributes_dict.get(key):
                    row_dict[position] = some_attributes_dict[key]
                    break
                position += 1
        
        return row_dict
