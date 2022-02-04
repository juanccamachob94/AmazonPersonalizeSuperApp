from pj.services.csv_management_service import CSVManagementService
from pj.services.db.csv.csv_model_service import CSVModelService

class CSVModelFinderService(CSVModelService):
    @classmethod
    def perform(cls, csv_manager_client, model, search_dict={}):
        """
            The last parameter uses the positions ids on row array with the respective values
            to match the data and validate if the row is registered. The most basic use of this
            method would use the position that belongs to id of record ({ 0: 'id' })
        """
        row_dict_positions_values = search_dict or cls.row_uniq_dict_record(model)
        if not row_dict_positions_values:
            return None
        # file.name is usted to represent the file location
        temporary_file = cls._read(csv_manager_client, model)
        rows_generator = CSVManagementService.rows_lazy_iterator(temporary_file.name)
        matched = None
        founded_row = None
        while True:
            try:
                row = next(rows_generator)
                matched = True
                for position in row_dict_positions_values:
                    matched = matched and \
                        str(row[position]) == str(row_dict_positions_values[position])
                if matched:
                    founded_row = row
                    break
            except StopIteration:
                break
        temporary_file.close()
        return founded_row
