from fpdf import FPDF
import json

with open('myfile.json') as file:#open the json file
    data = json.load(file)



# class maken voor de pdf file
class PDF(FPDF):
    def create_table(self, table_data, title_size, title, cell_width):
        # You need to define how to generate the table here.
        # Example: loop through the data and create cells
        
        self.set_font("Helvetica", "B", title_size)
        self.cell(0, 10, title, ln=True)  # Title van de tabel
        
        # maakt de font van het text
        self.set_font("Helvetica", "", 10)

        # Column headers
        headers = list(table_data.keys())
        self.cell(cell_width, 10, headers[0], border=1)
        self.cell(cell_width, 10, headers[1], border=1)
        self.cell(cell_width, 10, headers[2], border=1)
        self.cell(cell_width, 10, headers[3], border=1)
        self.cell(cell_width, 10, headers[4], border=1)
        self.cell(cell_width, 10, headers[5], border=1)
        self.ln()  # beweeg naar de volgende regel

        # Table data (values)
        print(table_data.values())	
        rows = zip(table_data.values())
        for row in rows:
            for item in row:
                self.cell(cell_width, 10, str(item), border=1)
                

# maakt een pdf file aan
pdf = PDF("p", "mm", "A4")
pdf.add_page()

# Set font voor text
pdf.set_font("Helvetica", "B", 24)



#data uit de json file halen
order = data['order']
klant = order['klant']

# ik maak een loop for de data van de klant
# en zet het in een dictionary
# ik gebruik de dictionary om de persoolijke data te behouden
# en de factuur te maken
klant_data = {
    "Naam": klant['naam'],
    "Adres": klant['adres'],
    "Postcode": klant['postcode'],
    "stad": klant['stad'],
    "KVk-nummer": klant['KVK-nummer'],
    }

informatie={
    "Datum":order["orderdatum"],
    "Factuurnummer":order["ordernummer"],
    "Betaaltermijn":order["betaaltermijn"],
    }

# Add a cell (no need for ln=True anymore, instead use new_x and new_y)
#factuur header info
pdf.cell(140, 10, "factuur")
pdf.cell(40, 10, "Soft log", ln=1)
pdf.set_font("Helvetica", "", 12)
pdf.cell(25, 10, "Datum:",  border=1)
pdf.set_font("Helvetica", "B", 20)
pdf.cell(115, 10, "factuurnummer:", border=False, align="C")

pdf.set_font("Helvetica", "", 12)
pdf.cell(0, 10, "+088 98 73 87 32",ln=1)

pdf.cell(90, 10, informatie["Datum"])
pdf.cell(50, 10, informatie["Factuurnummer"],)
pdf.cell(10, 10, "info@softlog.nl",ln=1)

pdf.cell(140, 10, "Factuur aan:")
pdf.cell(40, 10, klant_data["KVk-nummer"], ln=1)

pdf.cell(140, 10, klant_data["Naam"])
pdf.cell(40, 10, "BTW id: NL 12345678901", ln=1)

pdf.cell(70, 10, klant_data["Adres"])

# Insert a line break
pdf.ln(30)

# Add the table (using the create_table method from the PDF class)
# ik wil de data uit de json file halen en in een tabel zetten
# eerst ga ik een loop maken om de data uit de json file te halen
# en in een dictionary te zetten
# de dictionary ga ik gebruiken om de tabel te maken

for product in data['order']['producten']:
    producten = {
        "Productnaam": product['productnaam'],
        "Aantal": product['aantal'],
        "Prijs per stuk": product['prijs_per_stuk_excl_btw'],
        "BTW": product['btw'],
        "BTW_percentage": product['btw_percentage'],
        "Totaal": product['totaal'],
        }

# Use the create_table method of the PDF class
pdf.create_table(table_data = producten, title_size=20, title="Factuur data", cell_width=37)

# Save de output
pdf.output("output.pdf")
