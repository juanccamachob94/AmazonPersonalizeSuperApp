from abc import ABC, abstractmethod
from pj.models.dao.open_search.article_interactions_dao import ArticleInteractionsDAO
from pj.models.article_interaction import ArticleInteraction

class InteractionsInterfaceDAO(ABC):
    def create(self, interaction, article_id):
        if not(self._exists_item(interaction)):
            return None
        super().create(interaction)
        ArticleInteractionsDAO().create(
            ArticleInteraction.build(self.__build_article_interaction_dict(interaction, article_id))
        )


    def __build_article_interaction_dict(self, interaction, article_id):
        return {
            'user_id': interaction.get_user_id(),
            'article_id': article_id,
            'timestamp': interaction.get_timestamp()
        }


    @abstractmethod
    def _exists_item(_interaction):
        pass
