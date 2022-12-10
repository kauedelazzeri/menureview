#TAREFAS:
# importar CSV da semana
# Coletar carnes da semana
# Coletar acompanhamentos da semana
# Gerar novo cardapio com 2 carnes e entre 7 e 9 acompanhamentos

import pandas as pd

class DbGenerator:
    def __init__(self, filename) -> None:
        self.file = filename
        self.df = pd.read_csv(r'Cardapio\\'+str(self.file)+'.csv')
        #print(df)
        
    def coletar_carnes(self):
        weekday = ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta']
        for day in weekday:
            df_temp = self.df.loc[self.df["week_day"] == day]
            len = len(df_temp.index)

            category = ["Acompanhamento"] * len
            category[0] = "Carne"
            category[1] = "Carne"

            df_temp["category"] = category

            #select the rows with category Carne and append in a new df_carne
            #df_carne = df_temp.loc[df_temp["category"].isin(category)]
            #df_carne = df_carne.append(df_temp, ignore_index=True)
            #print(df_carne)

            #self.df_carne = self.df.loc[self.df["category"] == "Carne"]





teste = DbGenerator("items1")
