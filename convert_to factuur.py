#open order .json file
# with open('2000-096.json') as file:
# inlezen data uit verhaal
#toevoegen bedrijsgegevens aan data
#openen factuur.jsonfile
#schrijf data naar json weg

import json

with open('2000-096.json') as file:
    data = json.load(file)

#inklosief btw bedrag berekenen per order regel
#totaal bedreg van factuur berekenen
#kijken hoe om het toe te voegen aan de factuur

producten = data['order']['producten']
totaal = 0
for product in producten:
    print(product)
    prijs_zon_btw = product['aantal']*product['prijs_per_stuk_excl_btw']
    btw = (product['btw_percentage'] /100 ) * prijs_zon_btw
    product['btw']= round(btw,2)
    totaal = round(prijs_zon_btw + btw,2)
    product["totaal"]= totaal
print(totaal)

# product['btw_bedrag'] = product['aantal'] * product['prijs'] * product['btw'] / 100
# product['totaal'] = product['aantal'] * product['prijs'] + product['btw_bedrag']

totalen = {"totaal_incld_btw": totaal}
bedrijfsgegevens = {"bedrijfsgegevens":
  {"bedrijfsnaam": 'Soft log',
    "adres": '1234 CK,Rottendam',
    "kvknummer": '123456789',
    "btwnummer": 'NL 12345678901',
    "telefoonnummer": '+088 98 73 87 32',
    "email": 'info@softlog.nl',}
    
  }

data['bedrijfsgegevens']= bedrijfsgegevens
out_file = open("myfile.json", "w")

y = json.dump(data, out_file, indent=4)

