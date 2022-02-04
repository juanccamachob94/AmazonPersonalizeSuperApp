from pj.factories.dao.dao_factory import DAOFactory
from pj.models.interaction import Interaction
from pj.services.amazon.personalize.put_event_service import PutEventService
from pj.values.db_entity_names import CSV_ENTITY_NAMES
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES

class InteractionsService:
    @classmethod
    def perform(cls, user_id, item_id, article_id):
        interaction = Interaction.build({ 'user_id': user_id, 'item_id': item_id })
        DAOFactory.perform('open-search', OPEN_SEARCH_ENTITY_NAMES['Interaction']) \
            .create(interaction, article_id)
        PutEventService.perform(interaction)
