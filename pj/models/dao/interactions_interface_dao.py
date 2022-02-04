from abc import ABC, abstractmethod

class InteractionsInterfaceDAO(ABC):
    def create(self, interaction):
        if not(self._exists_item(interaction)) or not(self._exists_user(interaction)):
            return None
        return super().create(interaction)

    @abstractmethod
    def _exists_user(_interaction):
        pass

    @abstractmethod
    def _exists_item(_interaction):
        pass
