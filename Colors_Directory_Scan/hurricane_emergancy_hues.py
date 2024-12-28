## Required variables are below. If not needed, string to empty as:  ''
COLOR_NAME: str = "Emergency Classification"
CITATION: str = r"SOURCE: American Planning Association (APA). (1994). Land-Based Classification Standards (LBCS). [Retrieved from https://www.planning.org/lbcs/standards/]"
SUBHEADS: str = "SUBHEADS1,SUBHEADS2,SUBHEADS3"  # A later process will comma split strings into 3 parts


## Please set 3 list of tuples below.
## They cannot contain more than 14 items
## Method of CMYK is:  LIST = [ ('Color Name', C, M, Y, K), ('Color Name', C, M, Y, K),...]
##   ...where C, M, Y, K are integer values from 0-100

green_hues = [
 ('LimeGreen', 71, 0, 76, 20),
 ('GreenYellow', 31, 0, 81, 0),
 ('Chartreuse', 50, 0, 100, 0),
 ('SpringGreen', 100, 0, 50, 0),
 ('MediumSpringGreen', 100, 0, 38, 0),
 ('PaleGreen', 40, 0, 40, 0),
 ('SeaGreen', 67, 33, 0, 35),
 ('MediumSeaGreen', 66, 23, 0, 25),
 ('DarkSeaGreen', 24, 0, 24, 0),
 ('OliveDrab', 25, 41, 76, 10),
 ('YellowGreen', 25, 0, 76, 20),
 ('LawnGreen', 51, 0, 100, 0)]

yellow_hues = [
 ('Yellow', 0, 0, 100, 0),
 ('Gold', 0, 16, 100, 0),
 ('Goldenrod', 0, 24, 85, 15),
 ('DarkGoldenrod', 0, 27, 94, 28),
 ('Olive', 0, 0, 100, 50),
 ('Khaki', 0, 4, 42, 6),
 ('PaleGoldenrod', 0, 3, 29, 7),
 ('LemonChiffon', 0, 2, 20, 0),
 ('LightGoldenrodYellow', 0, 0, 16, 2),
 ('LightYellow', 0, 0, 12, 0),
 ('Ivory', 0, 0, 6, 0),
 ('Beige', 0, 0, 10, 4)]

orange_hues = [
 ('Orange', 0, 35, 100, 0),
 ('DarkOrange', 0, 45, 100, 0),
 ('OrangeRed', 0, 73, 100, 0),
 ('Coral', 0, 50, 69, 0),
 ('Tomato', 0, 61, 72, 0),
 ('Peru', 0, 35, 69, 20),
 ('Chocolate', 0, 50, 86, 45),
 ('SandyBrown', 0, 33, 61, 4),
 ('PeachPuff', 0, 15, 27, 0),
 ('Moccasin', 0, 11, 29, 0),
 ('Bisque', 0, 11, 23, 0),
 ('Burlywood', 0, 17, 39, 13)]


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
