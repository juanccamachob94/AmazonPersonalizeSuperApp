class DBManager:
    NAME = None

    def __init__(self, db_manager_client):
        self.db_manager_client = db_manager_client


    def find_all(self, _dict_identifier):
        pass


    def find(self, _dict_identifier):
        pass


    def create(self, _model):
        pass


    def save(self, _model):
        pass


    def update(self, _uniq_identifier_dict, _model):
        pass


    def delete(cls, _dict_identifier):
        pass


    def get_db_manager_client(self):
        return self.db_manager_client
