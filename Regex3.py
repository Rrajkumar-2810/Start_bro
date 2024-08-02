# Scraping all the phone numbers from a webpage using Regular expression.

import urllib.request
import re
from re import findall

url1 ="https://www.summet.com/dmsi/html/codesamples/addresses.html" #This Link is active
response = urllib.request.urlopen(url1)
html = response.read()
htmlstr = html.decode()

tpn = re.findall("\(\d{3}\) \d{3}-\d{4}", htmlstr)
for numbers in tpn:
    print(numbers)
