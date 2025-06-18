from PyPDF2 import PdfReader

# Load the PDF
reader = PdfReader("/home/emre/Desktop/marek pdf/raw stock table 24l 5s.pdf")
page = reader.pages[0]

# Get dimensions in points (1 point = 1/72 inch)
width = page.mediabox.width
height = page.mediabox.height

# Convert points to mm (1 point = 0.352778 mm)
width_mm = float(width) * 0.352778
height_mm = float(height) * 0.352778

# Check if dimensions match A4
print(f"Dimensions: {width_mm} mm × {height_mm} mm")
if (round(width_mm) == 210 and round(height_mm) == 297) or (round(width_mm) == 297 and round(height_mm) == 210):
    print("The PDF is A4.")
else:
    print(f"The PDF is not A4. Dimensions: {round(width_mm)} mm × {round(height_mm)} mm")
