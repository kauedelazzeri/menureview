#TAREFAS:
# importar CSV da semana
# Coletar carnes da semana
# Coletar acompanhamentos da semana
# Gerar novo cardapio com 2 carnes e entre 7 e 9 acompanhamentos

import pandas as pd

class DbGenerator:
    def __init__(self, filename) -> None:
        self.file = filename
        df = pd.read_csv(r'Cardapio\\'+str(self.file)+'.csv')
        #print(df)
        
    def coletar_carnes(self):
        pass

teste = DbGenerator("items1")