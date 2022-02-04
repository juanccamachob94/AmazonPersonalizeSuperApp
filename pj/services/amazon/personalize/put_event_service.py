import json

from pj.factories.amazon_personalize_solutions_factory import AmazonPersonalizeSolutionsFactory
from pj.services.amazon.personalize.put_service import PutService
from pj.helpers.string_helper import StringHelper

class PutEventService(PutService):
    DEFAULT_SESSION_ID = 'Session1'

    @classmethod
    def perform(cls, interaction):
        amazon_personalize_default_solution = \
            AmazonPersonalizeSolutionsFactory.get_instance('personalize-events')
        client = amazon_personalize_default_solution.get_client()
        section_type = StringHelper.first_substring(interaction.get_item_id(), '|')
        client.put_events(
            eventList=[{
                'eventId': str(interaction.get_timestamp()),
                'eventType': interaction.get_event_type(),
                # 'eventValue': interaction doesn't have the event_value,
                # 'impression': interaction doesn't have the event_value,
                'itemId': interaction.get_item_id(),
                'properties': json.dumps({ 'sectionType': cls._build_section_type(interaction) }),
                # 'recommendationId': interaction doesn't have the event_value,
                'sentAt': interaction.get_timestamp()
            }],
            sessionId=cls.DEFAULT_SESSION_ID,
            trackingId=amazon_personalize_default_solution.get_tacking_id(),
            userId=str(interaction.get_user_id())
        )


    @classmethod
    def _build_section_type(cls, interaction):
        return StringHelper.first_substring(interaction.get_item_id(), '|')
