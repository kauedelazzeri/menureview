import pandas as pd
from random import randint
from datetime import datetime

#Input deve ser sempre de somente uma semana
class DbGenerator:

    def __init__(self, gerar_dias, filename) -> None:
        self.weekday = ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta']
        self.df_carne = pd.DataFrame()
        self.df_acompanhamento = pd.DataFrame()
        self.df_sobremesa = pd.DataFrame()
        self.df_gerado = pd.DataFrame()
        self.filename = filename
        self.dias = gerar_dias

    # importar CSV da semana
    def importa_csv_semana(self):
        self.df = pd.read_csv(r'Cardapio\\Real\\'+str(self.filename)+'.csv')
        
    #TODO permitir mais semanas ou db completo
    def importa_csv(self):
        #self.df = 
        pass 
        
    # Coletar carnes e acompanhamentos 
    def coletar_categorias(self):
        DbGenerator.importa_csv_semana(self)

        for day in self.weekday:
            df_temp = self.df.loc[self.df["week_day"] == day]
            cardapio_len = len(df_temp.index)

            category = ["Acompanhamento"] * cardapio_len
            category[0] = "Carne"
            category[1] = "Carne"
            category[cardapio_len-1] = "Sobremesa"

            df_temp["category"] = category

            df_carne = df_temp.loc[df_temp["category"] == "Carne"]
            df_acompanhamento = df_temp.loc[df_temp["category"] == "Acompanhamento"]
            df_sobremesa = df_temp.loc[df_temp["category"] == "Sobremesa"]

            self.df_carne = pd.concat([self.df_carne, df_carne], ignore_index=True)
            self.df_acompanhamento = pd.concat([self.df_acompanhamento, df_acompanhamento], ignore_index=True)
            self.df_sobremesa = pd.concat([self.df_sobremesa, df_sobremesa], ignore_index=True)

    # Gerar novo cardapio com 2 carnes e entre 7 e 9 acompanhamentos
    def gera_dia(self):
        #randomiza os dados
        DbGenerator.coletar_categorias(self)

        #Gera novo cardapio com 2 carnes e entre 7 e 9 acompanhamentos
        for n in range(self.dias):
            n_acompanhamentos = randint(6,8)
            self.df_gerado = pd.concat([self.df_gerado,self.df_carne.sample(n=2),  self.df_acompanhamento.sample(n=n_acompanhamentos), self.df_sobremesa.sample(n=1)], ignore_index=True)
            #df = df.drop('week_day', axis=1)
            self.df_gerado.iloc[-(n_acompanhamentos+3): , self.df.columns.get_loc('week_day')] = n
      
        DbGenerator.save_csv(self)

    def save_csv(self):
        try:
            self.df_gerado.to_csv("Cardapio\\Gerado\\"+str(self.filename)+'_{}.csv'.format(pd.datetime.now().strftime("%d-%m-%Y %H%M%S")),index=False)  
            #print(len(self.df))
            print("Sucesso ao salvar o CSV")
        except:
            print("Erro ao salvar")

teste = DbGenerator(2, "items1")
teste.gera_dia()
