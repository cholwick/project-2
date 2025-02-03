from fpdf import FPDF
import json
import os

# Directory containing JSON files
json_folder = "json_files"  # Change this to your folder name

# List to store all product data
producten = []

# Loop through all JSON files in the folder
for filename in os.listdir(json_folder):
    if filename.endswith(".json"):  # Ensure it's a JSON file
        with open(os.path.join(json_folder, filename)) as file:
            data = json.load(file)

            # Extract product data and append to the list
            for product in data['order']['producten']:
                producten.append({
                    "Productnaam": product['productnaam'],
                    "Aantal": product['aantal'],
                    "Prijs per stuk": product['prijs_per_stuk_excl_btw'],
                    "BTW": product['btw'],
                    "BTW_percentage": product['btw_percentage'],
                    "Totaal": product['totaal'],
                })


# PDF Class with Pagination Support
class PDF(FPDF):
    def create_table(self, table_data, title_size, title, cell_width):
        self.set_font("Helvetica", "B", title_size)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

        if not table_data:
            print("ERROR: table_data is empty!")
            return

        # Headers
        headers = list(table_data[0].keys())

        # Print column headers
        for header in headers:
            self.cell(cell_width, 10, str(header), border=1)
        self.ln()

        # Print each row with pagination
        for row in table_data:
            if self.get_y() > 260:  # Check if we reached the bottom (adjust if needed)
                self.add_page()
                # Reprint headers
                for header in headers:
                    self.cell(cell_width, 10, str(header), border=1)
                self.ln()

            # Print row data
            for key in headers:
                self.cell(cell_width, 10, str(row[key]), border=1)
            self.ln()


# Create a PDF instance
pdf = PDF("P", "mm", "A4")
pdf.add_page()

# Set font for the title
pdf.set_font("Helvetica", "B", 24)

# Add a title
pdf.cell(140, 10, "Factuur")
pdf.cell(40, 10, "Soft log", ln=1)
pdf.ln(10)  # Line break

# Generate the table
pdf.create_table(table_data=producten, title_size=20, title="Factuur data", cell_width=37)

# Save output
pdf.output("output.pdf")
