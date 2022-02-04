from pj.models.timestamp_model import TimestampModel
from pj.validators.interaction_validator import InteractionValidator

class Interaction(TimestampModel):
    EVENT_TYPE_DEFAULT_VALUE = 'view'

    @classmethod
    def build(cls, interaction_dict):
        interaction = cls()
        interaction.set_user_id(interaction_dict.get('user_id'))
        interaction.set_item_id(interaction_dict.get('item_id'))
        event_type = interaction_dict.get('event_type')
        if event_type:
            interaction.set_event_type(event_type)
        return interaction


    def __init__(self):
        super().__init__() # id attribute is included by default but it isn't considered
        self.user_id = None
        self.item_id = None
        self.event_type = self.EVENT_TYPE_DEFAULT_VALUE

    def is_valid(self):
        return InteractionValidator.is_valid(self)


    def to_dict(self):
        return {
            'user_id': self.user_id,
            'item_id': self.item_id,
            'event_type': self.event_type,
            'timestamp': self.timestamp
        }


    def to_uniq_dict(self):
        return {} # uniq id doesn't exists


    def get_user_id(self):
        return self.user_id


    def set_user_id(self, user_id):
        self.user_id = user_id


    def get_item_id(self):
        return self.item_id


    def set_item_id(self, item_id):
        self.item_id = item_id


    def get_event_type(self):
        return self.event_type


    def set_event_type(self, event_type):
        self.event_type = event_type
