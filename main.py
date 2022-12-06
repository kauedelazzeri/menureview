from xml2df import Converter

class Converter_xml2df:

    cardapio = Converter("items7")
    cardapio.find_file()
    cardapio.find_titles()
    cardapio.save_df()
    cardapio.sort_df()
    cardapio.sums_calories()
    cardapio.save_csv()
