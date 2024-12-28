FONT_BOLD: str = "PDF_Fonts/Futura_Bold.ttc"
FONT_NORMAL: str = "PDF_Fonts/Futura_Normal.ttc"

from PDF_Functions import gen_directory_functions as gdf
import os


######################################################
def check_ttc_file(font_file: str) -> None:

  if not os.path.exists(font_file) and font_file.lower().endswith(".ttc"):
      ## Checks if the ttc file exist and its extension is ttc, Will System Exit if not
      gdf.exit_with_message(f"ERROR: Font: {font_file} is not Installed.\n Exiting...\n\n")
      return


