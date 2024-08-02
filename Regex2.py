#Regular Expression Operations:-
#1.Find a word in a string.
#2.Generate an iterator.
#3.Match one of any of several letters.
#4.Match series of range of characters.
#5.Replace string.
#6.Match a single character.

import re
s = 'we need to inform him with the latest information'

#1 Finding words in a string
findall = re.findall("inform",'we need to inform him with the latest information')
for i in findall:
    print(i)

#or

f = re.findall('inform', s)
print(f)
for j in f:
    print(j)
print()

#2. Gets the starting and ending index of a particular string
for b1 in re.finditer("inform", s): 
    ioctuple = b1.span()
    print(ioctuple)
print()

#3. Match words with a particular pattern
s2 = "Sat, Hat, Cat, Bat, Lad, Boy, Man, Ban"
for b2 in re.findall("[SHCBLM]at", s2):
    print(b2)
print()

#4. Match series of range of characters
s3 = "sat, bat, mat, pat, put, rid, bid, gig, jam, gun, bun, dad, bad, aim"
for b3 in re.findall("[a-p]at",s3):
    print(b3)
print()

#5. Replace a string
s4 = "hat rat mat bat"
reg1 = re.compile("[r]at")
s4 = reg1.sub("cat", s4)
print(s4)
print()

#6. Matching a single character
s5 = "12345"
b4 = len(re.findall("\d{5}", s5))
print(b4)
print()

# Search a particular pattern is present or not
s6 = "This is double \\comment in java."
b5 = re.search(r"\\comment", s6)
print(b5)

# Continuing new lines with whitespaces
s7 = '''
Can you feel the new day rising
Climbing up the east horizon
They can't stop us
'''
print(s7)
reg2 = re.compile("\n")
s7 = reg2.sub(" ", s7)
print(s7)

print("matches:", len(re.findall('\d', '12345')))
print("matches:", len(re.findall('\D', '12345')))
print("matches:", len(re.findall('\d{6}', '12345')))

num = "123 1234 12345 123456 12345567"
print("Matches:", len(re.findall('\d{5,7}', num)))

#checking a telephone number
phn = "678-392-0451"
if re.search("\w{3}-\w{3}-\w{4}", phn): #instaed of 'w' you can use 'd' as well
    print("Telephone number")

# \w [a-zA-Z0-9_]
# \W [^a-zA-Z0-9]
# \s [\f\n\r\t\v]
# \S [\f\n\r\t\v]

if re.search("\w{2,20}\s\w{2,20}", "Gaurav Ganguly"): # matching a valid name
    print("Valid name")

email = "seo@.com example.com testing@gmail.com @bold.com sk@aol.com" # matching valid email addresses
print("Matches=", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)))

