from pj.models.timestamp_model import TimestampModel
from pj.validators.user_validator import UserValidator

class User(TimestampModel):
    @classmethod
    def build(cls, dict_user_attributes):
        user = cls()
        user.set_user_id(dict_user_attributes.get('user_id'))
        user.set_device_id(dict_user_attributes.get('device_id'))
        return user


    def __init__(self):
        super().__init__()
        self.user_id = None
        self.device_id = None


    def is_valid(self):
        return UserValidator.is_valid(self)


    def to_dict(self):
        return {
            'user_id': self.user_id,
            'device_id': self.device_id,
            'timestamp': self.timestamp
        }


    def to_uniq_dict(self):
        return { 'user_id': self.user_id }


    def get_user_id(self):
        return self.user_id


    def set_user_id(self, user_id):
        self.user_id = user_id


    def get_device_id(self):
        return self.device_id


    def set_device_id(self, device_id):
        self.device_id = device_id
