from pj.models.base_model import BaseModel
from pj.helpers.date_helper import DateHelper

class TimestampModel(BaseModel):
    def __init__(self):
        self.timestamp = DateHelper.round_time()


    def get_timestamp(self):
        return self.timestamp


    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
