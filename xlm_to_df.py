from bs4 import BeautifulSoup as bs
content = []

# Read the XML file
with open("Cardapio\items1.txt", "r", encoding="utf8") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    bs_content = bs(content, "lxml")
    result = bs_content.find("d:title")
    print(result)