from fpdf import FPDF

pdf = FPDF("p", "mm", "A4")

pdf.add_page()

pdf.set_font("Arial", "B", 16)

pdf.cell(200, 10, "Welcome to Python!", 0, 1, "C")

pdf.output("output.pdf")