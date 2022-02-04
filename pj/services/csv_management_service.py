import csv
import tempfile
from csv import DictWriter

class CSVManagementService:
    @classmethod
    def create_temporary_file(cls, headers_list):
        # creates an empty csv file with headers
        temporary_file = tempfile.NamedTemporaryFile(suffix='.csv')
        with open(temporary_file.name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(headers_list)
        return temporary_file


    @classmethod
    def append(cls, file_route, headers_list, dict_record):
        with open(file_route, 'a', newline='') as f_object:  # this file.name represents the route
            dictwriter_object = DictWriter(f_object, fieldnames=headers_list)
            dictwriter_object.writerow(dict_record)


    @classmethod
    def delete(cls, file_route, row_uniq_dict_record):
        """
            dict_position_value => position on row array with values to match record to delete
            on the document
        """
        matched = None
        rows_generator = cls.rows_lazy_iterator(file_route)
        temporary_file = tempfile.NamedTemporaryFile(suffix='.csv')
        # temporary_file.name represents the route of the file
        with open(temporary_file.name, 'a') as csv_file:
            writer = csv.writer(csv_file)
            while True:
                try:
                    row = next(rows_generator)
                    matched = True
                    for position in row_uniq_dict_record:
                        matched = matched and \
                            str(row[position]) == str(row_uniq_dict_record[position])
                        if not matched:
                            writer.writerow(row)
                            break
                except StopIteration:
                    break
        return temporary_file


    @classmethod
    def replace(cls, file_route, headers_list, row_uniq_dict_record, dict_record):
        temporary_file = cls.delete(file_route, row_uniq_dict_record)
        cls.append(temporary_file.name, headers_list, dict_record)
        return temporary_file


    @classmethod
    def rows_lazy_iterator(cls, file_route):
        # it has logic to use generator and produce results with lazy iteration
        with open(file_route, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                yield row
