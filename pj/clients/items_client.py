from pj.factories.dao.dao_factory import DAOFactory
from pj.values.db_entity_names import CSV_ENTITY_NAMES
from pj.models.item import Item

class ItemsClient:
    @classmethod
    def perform(cls):
        site = 'ADN40'
        item_id = f'Política|{site}'
        DAOFactory.perform('csv', CSV_ENTITY_NAMES['Item']) \
            .save(Item.build({ 'item_id': item_id, 'site': site }))
