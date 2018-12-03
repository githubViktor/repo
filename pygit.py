
import re
"""
modul re filtre hashline with keywords

hashline is the email parsing data

"""
hash = open('data/Email_Parsing_Data.html', "r").read()
detail = r"[\w.-0-9]+@[\w]+.[\w]+"

filter = re.findall(detail, hash)
print(filter)

