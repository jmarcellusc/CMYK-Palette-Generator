## Required variables are below. If not needed, string to empty as:  ''
COLOR_NAME: str = "Land Based Classification Standards pg2"
CITATION: str = r"SOURCE: American Planning Association (APA). (1994). Land-Based Classification Standards (LBCS). [Retrieved from https://www.planning.org/lbcs/standards/]"
SUBHEADS: str = "Site,Structure,"  # A later process will comma split strings into 3 parts



site_colors = [
    ("Natural State", 39, 0, 39, 7),
    ("Developing Site", 0, 0, 10, 4),
    ("Developed - Crops, Grazing, Forest", 0, 11, 23, 20),
    ("Developed - No Buildings or Structures", 0, 9, 27, 45),
    ("Developed - Non Building Structures", 0, 35, 69, 45),
    ("Developed - with Buildings", 0, 75, 75, 45),
    ("Developed - with Parks", 76, 0, 76, 45),
    ("Not Applicable", 0, 0, 0, 17),
    ("Unclassifiable", 0, 0, 0, 0)
]

structure_colors = [
    ("Residential Buildings ", 0, 0, 100, 0),
    ("Commercial Buildings", 0, 100, 100, 0),
    ("Public Assembly Structures", 32, 87, 4, 6),
    ("Institutional or Community", 100, 100, 0, 0),
    ("Transportation -Related Structures", 21, 21, 21, 26),
    ("Utility -Related Structures", 0, 0, 0, 48),
    ("Military -Related Structures", 0, 25, 20, 0),
    ("Agricultural -Related Structures", 76, 0, 76, 45),
    ("No Structures", 0, 0, 0, 0)
]
