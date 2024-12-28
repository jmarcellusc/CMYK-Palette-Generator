# CMYK Palette Generator

#### Purpose: Creates a PDF page of CMYK color values and the color name for graphical design work. 

## Method
### Color Palette Files

For every PDF palette page, it requires a python script holding the following information:
- Variables:
  - COLOR_NAME: (require and used in filename)
  - CITATION: (optional)
  - SUBHEADS:  (optional, three strings for each color list)
- Color List (3 list, with each containing 14 tuples of color information)
  - Color Tuple Format:  "("Short Color Name", C, M, Y, K)", Each C,M,Y,K  is an integer value from 0-100
  - _If less than two Color List are needed, please use a blank color list to fill_
  - All processing Color List are stored in the /Colors_Directory_Scan, and will overwrite previous PDF files
  
### Fonts

- PDF Fonts
  - Font files ".ttc" stored in /PDF_Fonts directory and used to change the font within the PDF.
  - Please update teh "PDF_Fonts.py" to new font names
    - Update: Possible update in automatic font file read

### Run
Please run main.


## Project Information
Read Me requires more information and will be updated soon.






