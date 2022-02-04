from pj.values.db_entity_names import CSV_ENTITY_NAMES
from pj.values.db_entity_names import DYNAMO_ENTITY_NAMES
from pj.values.db_entity_names import OPEN_SEARCH_ENTITY_NAMES
from pj.factories.dao.dao_factory import DAOFactory
from pj.models.item import Item

class SubItemRecorder:
    @classmethod
    def perform(cls, article):
        site = cls.__build_site(article)
        DAOFactory.perform('csv', CSV_ENTITY_NAMES['SubItem']) \
            .create(Item.build({ 'item_id': f'{article.get_category()}|{site}', 'site': site }))


    @classmethod
    def __build_site(cls, article):
        if article.get_url():
            if 'aztecadeportes/' in article.get_url():
                return 'Azteca Deportes'
            elif 'www.adn40.mx' in article.get_url():
                return 'ADN40'
            elif 'vertigopolitico/' in article.get_url():
                return 'Vértigo Político'
            elif 'aztecanoticias/' in article.get_url():
                return 'Azteca Noticias'
            elif 'aztecauno/' in article.get_url():
                return 'Azteca UNO'
        return 'APP SuperApp'
