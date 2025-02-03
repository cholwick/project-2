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

# Loop door alle bestanden in de map
for bestand in os.listdir(mappad):
    print(f"Found file: {bestand}")  # toets om te kijken of de data goed is
    if bestand.endswith(".json"):  
        bestandspad = os.path.join(mappad, bestand)

        try:
            # Open en lees het JSON-bestand
            with open(bestandspad, "r", encoding="utf-8") as file:
                data = json.load(file)  # inlezen data uit verhaal
        except Exception as e:
            print(f"Fout bij openen van {bestand}: {e}")
            continue  # Als er een fout optreedt, ga verder met het volgende bestand

        # inclusief btw bedrag berekenen per order regel
        # totaal bedrag van factuur berekenen
        # kijken hoe om het toe te voegen aan de factuur
        try:
            producten = data['order']['producten']
        except KeyError:
            producten = data['factuur']['producten']

        totaal = 0
        for product in producten:
            print(product)  # toets om te kijken of de data goed is
            
            # btw berekenen
            if 'btw_percentage' in product:
                prijs_zon_btw = product['aantal'] * product['prijs_per_stuk_excl_btw']
                btw = (product['btw_percentage'] / 100) * prijs_zon_btw
                product['btw'] = round(btw, 2)
                totaal_product = round(prijs_zon_btw + btw, 2)
            else:
                stuck_btw = product['btw_per_stuk'] * product['aantal']
                totaal_product = round(product['aantal'] * product['prijs_per_stuk_excl_btw'] + stuck_btw, 2)
            
            product["totaal"] = totaal_product
            totaal += totaal_product  # Correct optellen van totaalbedrag

        print(totaal)  # Controleer totaalbedrag

        # totalen berekenen en opslaan
        totalen = {"totaal_incld_btw": totaal}

        # bedrijfsgegevens toevoegen aan data
        bedrijfsgegevens = {
            "bedrijfsgegevens": {
                "bedrijfsnaam": 'Soft log',
                "adres": '1234 CK, Rottendam',
                "kvknummer": '123456789',
                "btwnummer": 'NL 12345678901',
                "telefoonnummer": '+088 98 73 87 32',
                "email": 'info@softlog.nl',
            }
        }
        
        data.update(bedrijfsgegevens)  # bedrijfsgegevens toevoegen aan JSON

        # Zorg ervoor dat de bestandsnaam uniek blijft in de verwerkte map
        output_file_path = os.path.join(procesedmap, f"processed_{time.time()}_{bestand}")

        try:
            # maakt een nieuwe json file aan met de nieuwe data
            with open(output_file_path, "w", encoding="utf-8") as out_file:
                json.dump(data, out_file, indent=4)
            print(f"Bestand succesvol opgeslagen als: {output_file_path}")
        except Exception as e:
            print(f"Fout bij opslaan van {bestand}: {e}")


