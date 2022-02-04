class BaseDAO:
    DB_ENTITY_NAME = None

    def find(self, _identifiers_dict):
        raise Exception('find method not implemented')


    def find_all(self, _identifiers_dict):
        raise Exception('find_all method not implemented')


    def create(self, _model_dict):
        raise Exception('create method not implemented')


    def save(self, _model_dict):
        raise Exception('save method not implemented')


    def delete(self, _identifiers_dict):
        raise Exception('delete method not implemented')
