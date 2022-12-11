from xml2df import Converter
from dbGenerate import DbGenerator

'''
cardapio = Converter("items7")
cardapio.find_file()
cardapio.find_titles()
cardapio.save_df()
cardapio.sort_df()
cardapio.sums_calories()
cardapio.save_csv()
'''

#Número de dias para gerar e semana fonte para dados
novo_cardapio = DbGenerator(100, "items2")
novo_cardapio.gera_dia()


#TODO: Aplicar melhorias indicadas pelo pylint: Your code has been rated at 0.00/10