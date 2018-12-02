import re

hash = '&hash = 5558238940j239ee8923re92'
detail = r"\s[0-9,a-z]+"

filter = re.findall(detail, hash)
print(filter[0].lstrip())
