
class BaseModel:
    @classmethod
    def build(cls, _base_model_dict):
        raise Exception('build method not implemented')


    def is_valid(self):
        raise Exception('is_valid method not implemented')


    # this dict variables order depends of location in the database entity
    def to_dict(self):
        raise Exception('to_dict method not implemented')


    def to_uniq_dict(self):
        raise Exception('to_uniq_dict method not implemented')


    def to_body_dict(self):
        # self.to_dict() - self.to_uniq_dict()
        keys = list(self.to_uniq_dict().keys())
        dict_clone = self.to_dict()
        for key in keys:
            dict_clone.pop(key)
        return dict_clone
