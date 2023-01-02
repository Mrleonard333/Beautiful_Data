from bs4 import BeautifulSoup
import pandas as pd
import requests

URLS = [
        "https://lista.mercadolivre.com.br/informatica/armazenamento/discos-acessorios/hds-ssds/ssd-kingston-240gb_NoIndex_True", 
        "https://lista.mercadolivre.com.br/informatica/armazenamento/discos-acessorios/hds-ssds/ssd-kingston-240gb_Desde_49_NoIndex_True",
        "https://lista.mercadolivre.com.br/informatica/armazenamento/discos-acessorios/hds-ssds/ssd-kingston-240gb_Desde_97_NoIndex_True",
        "https://lista.mercadolivre.com.br/informatica/armazenamento/discos-acessorios/hds-ssds/ssd-kingston-240gb_Desde_145_NoIndex_True"
       ]

Data = dict()
for U in URLS:
    Response = requests.get(U) # < Will make a html request
    Content = BeautifulSoup(Response.content, "html.parser")
        # v Will store all the html content of the products
    Content = Content.find_all("div", attrs={"class":"ui-search-result__content-wrapper shops__result-content-wrapper"})

    for C in Content:       # v Will store the product title
        Title = C.find("div", attrs={"class":"ui-search-item__group ui-search-item__group--title shops__items-group"}).h2
        Price = C.find("span", attrs={"class":"price-tag-fraction"}) # < Will store the product price

        if "Kingston" in str(Title.text) and Price:
            try:
                Data["Title"].append(str(Title.text).strip()) # < Will add the values
                Data["Price"].append(float(Price.text))
            except:
                Data.update({"Title": [str(Title.text).strip()]}) # < Will create the values
                Data.update({"Price": [float(Price.text)]})

DF = pd.DataFrame(Data) # < Will format the data for pandas
print(DF)
DF.to_excel("Analisys.xlsx") # < Will create an Excel file
print("The Excel file has been created")