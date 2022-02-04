from pj.models.base_model import BaseModel
from pj.validators.item_validator import ItemValidator

class Item(BaseModel):
    @classmethod
    def build(cls, item_data):
        item = cls()
        item.set_item_id(item_data.get('item_id'))
        item.set_site(item_data.get('site'))
        return item


    def __init__(self):
        self.item_id = None # <category>|<site> or <section>|<site> (section name belongs to BSP)
        self.site = None


    def to_dict(self):
        return {
            'item_id': self.item_id,
            'site': self.site
        }


    def to_uniq_dict(self):
        return { 'item_id': self.item_id }
    

    def is_valid(self):
        return ItemValidator.is_valid(self)


    def get_item_id(self):
        return self.item_id


    def set_item_id(self, item_id):
        self.item_id = item_id


    def get_site(self):
        return self.site


    def set_site(self, site):
        self.site = site
