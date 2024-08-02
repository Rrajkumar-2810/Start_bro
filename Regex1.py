#Regular expression(RegEx): It is a special text string for describibg a search pattern.

import re
nameage = '''
Janice is 22 and jack is 25
Joey is 32 and Janet is 34
'''

ages = re.findall(r'\d{1,3}', nameage)
names = re.findall(r'[A-Z][a-z]*', nameage)
print(ages)
print(names)

nameageDict = {}
x=0
for eachname in names:
    nameageDict[eachname] = ages[x]
    x+=1
print(nameageDict)
