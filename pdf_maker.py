from fpdf import FPDF
import json

with open('2000-096.json') as file:#open the json file
    data = json.load(file)

ordernummer = data['order']['ordernummer']
orderdatum = data['order']['orderdatum']
betaaltermijn = data['order']['betaaltermijn']
naam = data['order']['klant']['naam']
adress= data['order']['klant']['adress']
postcode = data['order']['klant']['postcode']
stad = data['order']['klant']['stad']
kvknummer = data['order']['klant']['KVK-nummer']

# Define a class that extends FPDF to include the create_table method
class PDF(FPDF):
    def create_table(self, table_data, title_size, title, cell_width):
        # You need to define how to generate the table here.
        # Example: loop through the data and create cells
        
        self.set_font("Helvetica", "B", title_size)
        self.cell(0, 10, title, ln=True)  # Title of the table
        
        # Set the font for the table content
        self.set_font("Helvetica", "", 10)

        # Column headers
        headers = list(table_data.keys())
        self.cell(cell_width, 10, headers[0], border=1)
        self.cell(cell_width, 10, headers[1], border=1)
        self.cell(cell_width, 10, headers[2], border=1)
        self.cell(cell_width, 10, headers[3], border=1)
        self.cell(cell_width, 10, headers[4], border=1)
        self.ln()  # Move to the next line

        # Table data (values)
        rows = zip(*table_data.values())
        for row in rows:
            for item in row:
                self.cell(cell_width, 10, str(item), border=1)
            self.ln()

# Now create the main PDF document using this class
pdf = PDF("p", "mm", "A4")
pdf.add_page()

# Set font for text
pdf.set_font("Helvetica", "B", 24)

# Add a cell (no need for ln=True anymore, instead use new_x and new_y)
pdf.cell(140, 10, "factuur")
pdf.cell(40, 10, "Soft log", ln=1)

pdf.set_font("Helvetica", "", 12)
pdf.cell(25, 10, "Datum:",  border=1)
pdf.set_font("Helvetica", "B", 20)
pdf.cell(115, 10, "factuurnummer:", border=False, align="C")
pdf.set_font("Helvetica", "", 12)
pdf.cell(0, 10, "+088 98 73 87 32",ln=1)
pdf.cell(90, 10, "12-12-2020")
pdf.cell(50, 10, data['ordernummer'], ln=1)
pdf.cell(10, 10, "info@softlog.nl",ln=1)
pdf.cell(140, 10, "Factuur aan:")
pdf.cell(40, 10, "KVK nr: 12345678", ln=1)
pdf.cell(140, 10, "Klaas 6")
pdf.cell(40, 10, "BTW id: NL 12345678901", ln=1)
pdf.cell(70, 10, "1234 CK, Rotterdam")

# Insert a line break
pdf.ln(30)

# Add the table (using the create_table method from the PDF class)
data_as_dict = {
    "Naam": ["lake"],
    "Omschrijving": ["ja"],
    "Aantal": ["7"],
    "Prijs": ["19"],
    "Totaal": ["90"]
}

# Use the create_table method of the PDF class
pdf.create_table(table_data=data_as_dict, title_size=10, title="factuur data", cell_width=30)

# Save the output
pdf.output("output.pdf")
