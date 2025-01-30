from fpdf import FPDF
from create_table_fpdf2 import PDF

#create pdf object
#layout ('p','l')
#unit ('mm','cm','in')
#format ('A3','A4' (default),'A5','Letter','Legal')
pdf = FPDF("p", "mm", "A4")

#add a page
pdf.add_page()

#set font
#font ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
#style ('', 'B', 'I', 'U')

pdf.set_font("Arial", "B", 24)

#add a cell
#width, height, text, border, ln, align
#ln (0false, 1true - move to next line)
pdf.cell(140, 10, "factuur")
pdf.cell(40, 10, "Soft log", ln=True )
pdf.set_font("Arial", "", 12)
pdf.cell(25, 10, "Datum:",  border=True)
pdf.set_font("Arial", "B", 20)
pdf.cell(115, 10, "factuurnummer:", border = False, align="C")
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, "+088 98 73 87 32", ln=True)
pdf.cell(90, 10, "12-12-2020")
pdf.cell(50, 10, "f-0001")
pdf.cell(10,10 , "info@softlog.nl", ln=True)
pdf.cell(140, 10, "Factuur aan:")
pdf.cell(40, 10, "KVK nr: 12345678", ln=True)
pdf.cell(140, 10, "Klaas 6")
pdf.cell(40, 10, "BTW id: NL 12345678901", ln=True)
pdf.cell(70, 10, "1234 CK, Rotterdam", ln=True)
pdf.ln()

# data_as_dict = {"Naam" : ["lake"],
#                 "Omschrijving" : ["ja"],
#                 "Aantal" : ["7"],
#                 "Prijs" : ["19"],
#                 "Totaal" : ["90"]}
# pdf = PDF()
# pdf.add_page()
# pdf.set_font("Arial", "",  size=10)

# pdf.create_table(table_data = data_as_dict, title_size=10, title="factuur data", cell_width=[15,15,10,45], x_start='C', align_header='C', align_data='C', emphasize_data=["Totaal"], emphasize_color=[255,0,0], emphasize_style='B')
# pdf.ln()

# pdf.output("output.pdf")