#open order .json file
# with open('2000-096.json') as file:
# inlezen data uit verhaal
#toevoegen bedrijsgegevens aan data
#openen factuur.jsonfile
#schrijf data naar json weg
import time
import json
import os

mappad = r"C:\school\code\project-2\json_order\test_set_PC"
factuurmap = r"C:\school\code\project-2\json_invoice"
procesedmap = r"C:\school\code\project-2\json_processed"

for bestand in os.listdir(mappad):
    print(f"Found file: {bestand}") #toets om te kijken of de data goed is
    if bestand.endswith(".json"): 
        bestandspad = os.path.join(mappad, bestand) 
        
        try:
            with open(bestandspad, "r", encoding="utf-8") as file:
                data = json.load(file)
                bron = bestandspad
        except Exception as e:
            print(f"Fout bij openen van {bestand}: {e}")
            continue

#inklosief btw bedrag berekenen per order regel
#totaal bedreg van factuur berekenen
#kijken hoe om het toe te voegen aan de factuur
try:
    producten = data['order']['producten']
except KeyError as e:
    producten = data['factuur']['producten']

totaal = 0
for product in producten:
    print(product)#toets om te kijken of de data goed is
    #btw berekenen
    if 'btw_percentage' in product:
        prijs_zon_btw = product['aantal']*product['prijs_per_stuk_excl_btw']
        btw = (product['btw_percentage'] /100 ) * prijs_zon_btw
        product['btw']= round(btw,2)
        #totaal berekenen
        totaal = round(prijs_zon_btw + btw,2)
    else:
        stuck_btw = product['btw_per_stuk'] * product['aantal']
        totaal = round(product['aantal'] * product['prijs_per_stuk_excl_btw'] + stuck_btw,2)
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

output_file_path = os.path.join(procesedmap, f"processed_{time.time()}_{bestand}")

try:
    # Write the modified data to a new JSON file in the processed directory
    with open(output_file_path, "w", encoding="utf-8") as out_file:
        json.dump(data, out_file, indent=4)
    print(f"Bestand succesvol opgeslagen als: {output_file_path}")
except Exception as e:
    print(f"Fout bij opslaan van {bestand}: {e}")

