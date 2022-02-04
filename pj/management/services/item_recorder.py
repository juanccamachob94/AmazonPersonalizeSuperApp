from pj.factories.dao.dao_factory import DAOFactory
from pj.services.amazon.personalize.put_item_service import PutItemService
from pj.models.item import Item
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class ItemRecorder:
    @classmethod
    def perform(cls, article_category, site):
        item = Item.build({ 'item_id': f'{article_category}|{site}', 'site': site })
        itemsDAO = DAOFactory.perform('open-search', OPEN_SEARCH_ENTITY_NAMES['Item'])
        if not itemsDAO.find(item.to_uniq_dict()):
            itemsDAO.create(item)
            PutItemService.perform(item)
