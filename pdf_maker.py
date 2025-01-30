from fpdf2 import FPDF
from create_table_fpdf2 import PDF  # Ensure this is compatible with fpdf2

# Create pdf object (same as fpdf)
pdf = FPDF("p", "mm", "A4")

# Add a page
pdf.add_page()

# Set font (use 'Helvetica' in fpdf2)
pdf.set_font("Helvetica", "B", 24)

# Add normal data
pdf.cell(140, 10, "factuur")
pdf.cell(40, 10, "Soft log", ln=True)  # Adds a new line after this cell
pdf.set_font("Helvetica", "", 12)
pdf.cell(25, 10, "Datum:", border=True)
pdf.set_font("Helvetica", "B", 20)
pdf.cell(115, 10, "factuurnummer:", border=False, align="C")
pdf.set_font("Helvetica", "", 12)
pdf.cell(0, 10, "+088 98 73 87 32", ln=True)
pdf.cell(90, 10, "12-12-2020")
pdf.cell(50, 10, "f-0001")
pdf.cell(10, 10, "info@softlog.nl", ln=True)
pdf.cell(140, 10, "Factuur aan:")
pdf.cell(40, 10, "KVK nr: 12345678", ln=True)
pdf.cell(140, 10, "Klaas 6")
pdf.cell(40, 10, "BTW id: NL 12345678901", ln=True)
pdf.cell(70, 10, "1234 CK, Rotterdam", ln=True)

# Add some space before the table
pdf.ln(10)  # Adds a line break, which is useful for spacing

# Table Data
data_as_dict = {
    "Naam": ["lake"],
    "Omschrijving": ["ja"],
    "Aantal": ["7"],
    "Prijs": ["19"],
    "Totaal": ["90"]
}

# Now add the table using the custom PDF class
# Ensure that the 'create_table_fpdf2' class is compatible with fpdf2
pdf_table = PDF()  # Call the custom class for the table
pdf_table.add_page()  # Add a new page if needed
pdf_table.set_font("Helvetica", "", size=10)

# Add the table to the pdf
pdf_table.create_table(table_data=data_as_dict, title_size=10, title="factuur data", cell_width="even")

# Output the pdf
pdf_table.output("output.pdf")
