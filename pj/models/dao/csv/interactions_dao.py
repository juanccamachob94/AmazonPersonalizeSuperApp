from pj.models.dao.csv_dao import CSVDAO
from pj.models.dao.interactions_interface_dao import InteractionsInterfaceDAO
from pj.models.dao.csv.users_dao import UsersDAO
from pj.models.dao.csv.items_dao import ItemsDAO
from pj.values.db_entity_names import CSV_ENTITY_NAMES

class InteractionsDAO(CSVDAO, InteractionsInterfaceDAO):
    DB_ENTITY_NAME = CSV_ENTITY_NAMES['Interaction']

    def _exists_user(self, interaction):
        return UsersDAO().find({ 'user_id': interaction.get_user_id() })


    def _exists_item(self, interaction):
        return ItemsDAO.find({ 'item_id': interaction.get_item_id() })
