from pj.services.interactions_service import InteractionsService

class InteractionsClient:
    @classmethod
    def perform(cls):
        user_id = 350
        item_id = 'Internacional|ADN40'
        section_type = 'ADN40'
        for i in range(10):
            InteractionsService.perform(user_id, item_id, section_type)
