## Required variables are below.    If not needed, string to empty as:  ''
COLOR_NAME: str = "Land Based Classification Standards pg1"
CITATION: str = r"SOURCE: American Planning Association (APA). (1994). Land-Based Classification Standards (LBCS). [Retrieved from https://www.planning.org/lbcs/standards/]"
SUBHEADS: str = "Activity,Function,Ownership"  # A later process will comma split strings into 3 parts



activity_colors = [
    ("Residential ", 0, 0, 100, 0),
    ("Shopping, Business, or Trade", 0, 100, 100, 0),
    ("Industrial, Manufacture, & Waste", 32, 87, 4, 6),
    ("Social, institutional, or Infrastructure", 100, 100, 0, 0),
    ("Travel or Movement", 21, 21, 21, 26),
    ("Mass Assembly of People", 41, 0, 0, 69),
    ("Leisure", 40, 0, 40, 6),
    ("Natural Resources", 75, 0, 0, 45),
    ("No Human Activity or Unclassifiable", 0, 0, 0, 0)
]

function_colors = [
    ("Residence or Accommodations", 0, 0, 100, 0),
    ("General Sales & Services", 0, 100, 100, 0),
    ("Manufacture & Wholesale Trade", 32, 87, 4, 6),
    ("Transport, Communications, and Utilities", 21, 21, 21, 26),
    ("Arts, Entertainment, or Recreation", 39, 0, 39, 7),
    ("Education, Healthcare, & Public Admin", 100, 100, 0, 0),
    ("Construction", 100, 0, 0, 45),
    ("Mining & Extraction", 39, 81, 0, 45),
    ("Agriculture, Forestry, & Fishing", 76, 0, 76, 45)
]

ownership_colors = [
    ("No Constraints - Private or Related", 0, 0, 10, 4),
    ("Some Constraints - Easements or Related", 100, 100, 0, 0),
    ("Limited Restrictions - Leased or Related", 100, 100, 0, 45),
    ("Public Restrictions - Various Ownership", 39, 0, 39, 7),
    ("Other Public Use - Special", 100, 0, 100, 61),
    ("Nonprofit Ownership or Related", 25, 0, 75, 44),
    ("Joint Ownership Public", 0, 0, 0, 25),
    ("Joint Ownership Private", 0, 0, 0, 85), # Change from black to dark gray
    ("Not Applicable", 0, 0, 0, 0)
]
