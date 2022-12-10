import xml.etree.ElementTree as ET
import pandas as pd

class Converter:
    def __init__(self, filename) -> None:
        self.week_days = [] 
        self.titles = []
        self.k_calories = []
        self.file = filename
        self.ns = ''
        self.tree = ET.parse("Cardapio\\Real\\"+str(self.file)+".txt")
        self.root = self.tree.getroot()
        #week = '2022-11-14'

    def find_file(self):
        if '{' in self.root.tag:
            self.ns = '{'+self.root.tag.split('}')[0].strip('{')+'}'

    def find_titles(self):
        for entry in self.root.findall(f'{self.ns}entry'):
            properties = entry.find(f'{self.ns}content').find('{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties')
            self.week_days.append(properties.find('{http://schemas.microsoft.com/ado/2007/08/dataservices}DiaSemana').text)
            self.titles.append(properties.find('{http://schemas.microsoft.com/ado/2007/08/dataservices}Title').text)
            self.k_calories.append(int(properties.find('{http://schemas.microsoft.com/ado/2007/08/dataservices}Kcal').text))

    def save_df(self):
        df2 = pd.DataFrame({'week_day': self.week_days, 'title': self.titles, 'k_calories': self.k_calories})
        #print(df2)
        try:
            df1 = pd.read_csv(str(self.file)+'.csv')
            self.df = pd.concat([df1,df2],ignore_index=True).reset_index(drop=True)
        except:
            self.df = df2

    def sort_df(self):
        weekday_sort = {'Segunda':0, 'Terca':1, 'Quarta':2, 'Quinta':3, 'Sexta':4}

        self.df = self.df.sort_values(by=['week_day','k_calories'],key=lambda x: x.map(weekday_sort))
        #print(self.df[self.df['week_day']=='Segunda'])

    def category_item(self):
        '''
        TO DO
        colocar categoria, carne ou acompanhamento no df
        '''

    def sums_calories(self):
        sums = self.df.groupby("week_day").sum('k_calories')
        #print(sums)

    def total_calories_day(self):
        '''
        TO DO
        colocar o somatorio das calorias do dia no df
        '''

    def save_csv(self):
        try:
            self.df.to_csv("Cardapio\\Real\\"+str(self.file)+'.csv',index=False)
            #print(len(self.df))
            print("Sucesso ao salvar o CSV")
        except:
            print("Erro ao salvar")
        
