import numpy as np
import pandas as pd

from pj.values.db_entity_names import CSV_ENTITY_NAMES
from pj.factories.csv_manager_factory import CSVManagerFactory
from pj.lambdas.models.item_recommender import ItemRecommender

import os
from dotenv import load_dotenv

load_dotenv()

class RecommendationsService:
    @classmethod
    def perform(cls, user_id):
        return cls.__predicion_funcion(user_id)


    @classmethod
    def __predicion_funcion(cls, id_cliente, data_limit=ItemRecommender.DEFAULT_DATA_LIMIT):
        tabla_interacciones=pd.read_csv(cls.__get_csv_route())
        Posibilities=pd.read_csv(os.environ['AWS_ALGORITIA_PERSONALIZE_ENDPOINT'])
        try:
            l_v=[f'Vista_{x}' for x in range(1,7)]
            inter=tabla_interacciones[tabla_interacciones['USER_ID']==str(id_cliente)].tail(5)
            inter['Vista']=[f'Vista_{x+1}' for x in range(0,inter.shape[0])]
            inter=inter.pivot_table(index='USER_ID',columns='Vista',aggfunc=lambda x: x,values='ITEM_ID')
            inter.iloc[0]=np.sort(inter.iloc[0])
            inter[[x for x in l_v if x not in inter.columns]]='None'
            Recomendacion=inter.merge(Posibilities,on=l_v)[[f'Recomendacion_{x}' for x in range(1,data_limit+1)]]
            js_return={'itemList':[{'itemId':x,'score':np.random.randint(1,100)/100 } for x in list(Recomendacion.values[0])]}
            return js_return
        except:
            js_return={'itemList':[{'itemId':x,'score':np.random.randint(1,100)/100 } for x in ['Seguridad|ADN40', 'Internacional|ADN40', 'Estados|ADN40','Es tendencia|ADN40', 'Poder|ADN40', 'Salud|ADN40', 'Ciudad|ADN40','Pop|ADN40', 'Ciencia|ADN40', 'Deportes|ADN40'][0:data_limit]]}
            return js_return


    @classmethod
    def __get_csv_route(cls):
        return CSVManagerFactory.perform(CSV_ENTITY_NAMES['Interaction']) \
            .get_db_manager_client().get_absolute_input_route()
