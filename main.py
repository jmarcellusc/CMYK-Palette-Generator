import time

# Local Imports
from PDF_Functions import gen_pdf_color_palette as colorGen, immutable_SOP_terms as SOP, \
    gen_directory_functions as funcGen
from PDF_Fonts import PDF_Fonts as pdf_fonts

"""
AUTHOR:   Juan Marcel Campos
EMAIL:    jmarcel.campos@outlook.com
DATE:     12/15/2024
VERSION:  1.1.0
GITHUB:   https://github.com/jmarcellusc/Graphical_Design_Scheme/
GIT_IGNORE: *.pdf
CORE LIBRARIES: "reportlab", "PyPDF2"
CORE IMPORTS: 
    - from reportlab.lib.pagesizes import letter
    - from reportlab.pdfgen import canvas
    - import PyPDF2
MAIN GENERATOR: pdf_color_palette_Gen.py
PURPOSE:  Will generate a PDF of max(14 colors by 3 lists) from a list of 3 independent list of colors.
PARAMETERS: Color list and independent Variables are stored in "colors_directory", please import
PARAMETERS: 
    - color_lists: list  (list of 3 color lists)
    - colors_name: str  (string of colors name, used in PDF document name and within PDF)
    - doc_id: str  (string used within PDF for admin identification)
    - output_file="_palettes.pdf"  (NOT Modifiable but used as suffix for PDF name)
NOTES_1:  Code is very elemental and will be improved depending of better procedure method.
NOTES_2:  Each list must have 3 independent list. If a blank column is needed, please use the blank list
NOTES_#:  Each color list can not have more than 14 items (it can contain less)
NOTES_4:  Please format the entry as tuple ("NAME", C, M, Y, K),  
NOTES_5:  CMYK are integers only, from 0-100            (!!! AND NOT: 0-1 percentages !!!)
NOTES_6:  immutable_SOP_terms.py  has the official SOP ID reference.
NOTES_7:  Updated the Font path in 'immutable_SOP_terms.py'  !!!
"""


######################################################
## Examples....
paper_white_colors = [
    ("Bright White", 0, 0, 0, 0),
    ("Pure White", 0, 0, 0, 1),
    ("Snow White", 0, 0, 0, 2),
    ("White", 0, 0, 0, 3),
    ("Brilliant White", 0, 0, 0, 4),
    ("Dazzling White", 0, 0, 0, 6),
    ("Glistening White", 0, 0, 0, 7),
    ("Shimmering White", 0, 0, 0, 8),
    ("Sparkle White", 0, 0, 0, 9),
    ("Gleaming White", 0, 0, 0, 10),
    ("Radiant White", 0, 0, 0, 11),
    ("Luminous White", 0, 0, 0, 12),
    ("Opalescent White", 0, 0, 0, 13),
    ("Nacreous White", 0, 0, 0, 14)
]

ivory_colors = [
    ("Off-White Different", 0, 2, 2, 0),
    ("Soft White", 2, 4, 6, 0),
    ("Cloud White", 1, 2, 2, 0),
    ("Pearl", 0, 2, 4, 2),
    ("Pale Ivory", 0, 2, 4, 1),
    ("Vanilla", 0, 4, 8, 0),
    ("Lighter Antique White", 2, 5, 7, 0),
    ("Lighter Cream", 2, 6, 9, 0),
    ("Lighter Bone White", 2, 5, 7, 2),
    ("Lighter Oyster White", 2, 6, 6, 2),
    ("Lighter Warm White", 2, 4, 6, 2),
    ("Lighter Light Khaki", 2, 5, 10, 0),
    ("Lighter Ecru", 2, 5, 7, 1),
    ("Lighter Porcelain White", 0, 2, 3, 1)
]








############################################################################################################
############################################################################################################
## Create a list of tuples ["Name of Color" and (CMYK as C, M, Y, K)],  add this to the major list of palettes.
if __name__=="__main__":
    print("\n\n#####################################################")
    print("            Graphic Color Design Scheme         ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    print(f"--- Version: {SOP.VERSION}\n")
    time.sleep(1)

    # Blank Filler List
    blank_cmyk_list = [
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0),
        ("", 0, 0, 0, 0)
    ]

    ## Scan Directory for Python List
    print(" >> Initializing Parameters")
    counter: int = 0
    variables_from_python_file = ["COLOR_NAME", "CITATION", "SUBHEADS"]
    directory_to_scan = "./Colors_Directory_Scan"

    ## Check if Fonts are installed
    print(" >> Checking for Font Filess")
    FUTURA_BOLD = pdf_fonts.FONT_BOLD
    FUTURA_NORMAL = pdf_fonts.FONT_NORMAL
    pdf_fonts.check_ttc_file(FUTURA_BOLD)
    pdf_fonts.check_ttc_file(FUTURA_NORMAL)
    time.sleep(1)

    ## Scan Protocols
    print(" >> Scanning Directory")
    extracted_variables = funcGen.get_variable_values_from_files(directory_to_scan, variables_from_python_file)
    found_lists_directory = funcGen.scan_directory_for_lists(directory_to_scan)
    time.sleep(2)

    ## Results
    print(" >> Iterating...\n")
    time.sleep(1)
    for key_python_file, extract_list in found_lists_directory.items():
        # Update counter
        counter += 1

        # Iterate python file name
        print(f"\tPROCESSING #{counter} PYTHON FILE: {key_python_file[2:]}")
        # Screen list[list] to requirements
        extract_list = funcGen.process_list_screen(extract_list, blank_cmyk_list)

        # Extract Sub-Variables
        required_variables = extracted_variables[key_python_file]

        color_name: str = required_variables["COLOR_NAME"]
        citation: str = required_variables["CITATION"]
        subheads: str = required_variables["SUBHEADS"].replace(" ", "").split(',')

        # Initialize PDF Generator
        colorGen.create_color_pdf(extract_list, color_name, SOP.DOCUMENT_ID,
                                  additional_info=citation, subheaders=subheads)

        print("\n")
        time.sleep(1)

    print(" >> Directory Process Complete. \n\n")




