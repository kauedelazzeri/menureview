import pandas as pd

# importar CSV

# Cortar strings, mudar palavras para identificadores...

# PCA, LDA...

class Preprocessing:

    def __init__(self):
        self.data = []

    def importa_csv_semana(self):
        #self.df = pd.read_csv(r'Cardapio\\Gerado\\'+str(self.filename)+'.csv')
        pass


df = pd.read_csv(r'Cardapio\\Gerado\\items2_10-12-2022 201016.csv')

#limpar title
char_to_replace = {' de ' : ' ', ' e '  : ' ', ' com ': ' ', ' no ' : ' ', ' à '  : ' ', ' a '  : ' ', ' ao ' : ' ', ' na ' : ' '}

# Iterate over all key-value pairs in dictionary 
for key, value in char_to_replace.items():
    # Replace key character with value character in string
    for n in range(len(df)):
        df['title'][n] = df["title"][n].replace(key, value)

#retirar colunas desnecesárias

#String 2 code
#change each word from the colums df["title"] to a number for IA identification

for n in range(len(df)):
    df['title'][n] = df['title'][n].astype(int)

#print(df['title'])


#cardapio do dia para string
primeiro = 0
for n in len(df):
    if df["week_day"].loc[n] != df["week_day"].loc[n+1]:     
        df_temp = df.loc[primeiro:n]
        
        df_temp = df_temp.drop(['week_day'], axis=1)
        df_temp = df_temp.drop(['category'], axis=1)

        df_temp = df_temp.to_string(header=False, index=False)
        df_temp = df_temp.replace('\n', ' ')


        
        #pd.get_dummies(dados, columns = ['variavel'])

        df_temp.to_numpy()
        primeiro = n

        



#X = [[0, 0], [1, 1]]
#y = [0, 1]