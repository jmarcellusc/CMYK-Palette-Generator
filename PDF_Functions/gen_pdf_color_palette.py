import os
import time

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from PDF_Fonts import PDF_Fonts as pdf_Fonts
import PyPDF2

# Local Import (fonts Directory)
from PDF_Functions import immutable_SOP_terms as SOP

# Required to set Font Family to a File
from reportlab.pdfbase.ttfonts import TTFont


######################################################
def create_color_pdf(color_lists: list, colors_name: str,doc_id: str, additional_info="", subheaders=[], output_file="_PALETTES.pdf") -> None:
    # Set up PDF canvas
    output_file = "_" + colors_name.replace(" ", "_") + output_file
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Set Font Family (Might Require local file reference)
    pdfmetrics.registerFont(TTFont('Futura-Bold', pdf_Fonts.FONT_BOLD))
    pdfmetrics.registerFont(TTFont('Futura-Light', pdf_Fonts.FONT_NORMAL))
    FONT_BOLD: str = "Futura-Bold"
    FONT_NORMAL = "Futura-Light"
    x = pdf_Fonts.FONT_NORMAL

    # Add title on the color boxes page
    y_top_margin = 792 - 72
    x_right_margin = 612 - 72
    c.setFont(FONT_BOLD, 16) # Should be Bold
    c.drawString(72, y_top_margin, "Houston Galveston Area Council")

    # Add subtitle on the color boxes page
    c.setFont(FONT_NORMAL, 12)
    c.drawString(72, y_top_margin-15, f"Cartography GIS Color CMYK Palettes |  \"{colors_name}\"")

    # Add subtitle on the color boxes page
    c.setFont(FONT_NORMAL, 8)
    c.drawString(x_right_margin-100, y_top_margin+40, f"Document: {doc_id}")

    # Adds Sub-headers Above Title
    if subheaders:
        # Add subtitle on the color boxes page
        c.setFont(FONT_NORMAL, 8) # Should be Bold
        c.drawString(140, y_top_margin - 40, f"{subheaders[0]}")
        c.drawString(300, y_top_margin - 40, f"{subheaders[1]}")
        c.drawString(480, y_top_margin - 40, f"{subheaders[2]}")

    # Add Footer on the color boxes page
    c.line(72, 55, 540, 55)
    c.setFont(FONT_NORMAL, 11)
    c.drawString(72, 40, "Houston Galveston Area Council")
    c.drawString(360, 40, "Data Analytics and Research Group")

    # Adds additional text information, if needed.
    if additional_info:
        # Define a paragraph style
        style = ParagraphStyle(
            name='Normal',
            fontSize=8,
            leading=14,  # Adjust leading for line spacing
            alignment=0  # Left-aligned
        )
        #c.setFont("Helvetica", 8)
        p = Paragraph(additional_info, style)
        p.wrapOn(c, 470, 700)  # Adjust width as needed
        p.drawOn(c, 72, 80)
        #c.drawString(72, 80, f"{additional_info}")

    # Box dimensions
    box_size = 24  # 0.5 inches in points (72 points per inch)
    margin = 72  # 1-inch margin around the page (previously 36)
    column_spacing = 144  # Spacing between columns
    x_offset = margin
    y_offset = height - margin - box_size - 50  # Adjust y_offset for title spacing and 1-inch margin

    # Vertical spacing between boxes (increased by 30%)
    vertical_spacing = 13  # 13 points of spacing

    # Iterate over each list of colors, one list per column
    for color_list in color_lists:
        # Reset y_offset for each column
        y_offset = height - margin - box_size - 50  # Reset to 1-inch margin

        for color in color_list:
            if len(color) != 5:
                continue  # Skip invalid entries

            color_name, c_value, m_value, y_value, k_value = color
            # Convert CMYK values to 0-1 scale for ReportLab
            c.setFillColorCMYK(c_value / 100, m_value / 100, y_value / 100, k_value / 100)

            # Draw the box
            c.rect(x_offset, y_offset, box_size, box_size, fill=1, stroke=0)

            # Draw the label with color name and CMYK values
            if color_name != "":
                label_text = f"{color_name}\nCMYK: ({c_value}, {m_value}, {y_value}, {k_value})"
            else:
                label_text = ""
            c.setFillColorRGB(0, 0, 0)  # Black text
            text_object = c.beginText(x_offset + box_size + 10, (y_offset + box_size / 4)+6)
            text_object.setFont(FONT_NORMAL, 7)
            text_object.textLines(label_text)
            c.drawText(text_object)

            # Update position for the next box
            y_offset -= box_size + vertical_spacing

            # If there's not enough room for another box, move to the next page
            if y_offset < margin + box_size:
                c.showPage()  # Start a new page
                # Add title to subsequent pages
                c.setFont(FONT_BOLD, 18)
                c.drawCentredString(width / 2, height - 50, "Color Boxes and Their CMYK Values")
                x_offset = margin
                y_offset = height - margin - box_size - 50  # Reset y_offset for the new page

        # Move to next column
        x_offset += box_size + column_spacing

        # If there's not enough room for the next column, move to a new page
        if x_offset + box_size > width - margin:
            c.showPage()  # Start a new page
            # Add title to subsequent pages
            c.setFont(FONT_BOLD, 18)
            c.drawCentredString(width / 2, height - 50, "Color Boxes and Their CMYK Values")
            x_offset = margin
            y_offset = height - margin - box_size - 50  # Reset y_offset for the new page

    c.save()

    # Remove the last page using PyPDF2
    remove_last_page(output_file)


######################################################
def remove_last_page(pdf_file):
    # Open the PDF to remove the last page
    output_pdf_name = f"PDF{pdf_file}"

    with open(pdf_file, "rb") as input_pdf:
        reader = PyPDF2.PdfReader(input_pdf)
        writer = PyPDF2.PdfWriter()

        # Add all pages except the last one
        for page_num in range(len(reader.pages) - 1):  # Exclude last page
            writer.add_page(reader.pages[page_num])

        # Write the output file (without the last page)
        with open(output_pdf_name, "wb") as output_pdf:
            writer.write(output_pdf)

    # Delete the original file after modification
    os.remove(pdf_file)

    print(f"\t  ~~ Color Palette PDF Saved:  \"{output_pdf_name}\"")
    time.sleep(1.2)



