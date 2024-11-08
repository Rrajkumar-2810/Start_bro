s = "rishi"
print(s[len(s): 0: -1])

lst = ["jam", "butterscooth",123,25.2,"78","75.13","stop","break"]
print(lst[1: len(lst)])

def reverse(s):
    str=""
    for i in range(len(s)):
        str = s[i]+str
    return str
#print(reverse("madam", "1221", "raj", "stop", "break", "leave", "continue"))
print(reverse("madam"))
print(reverse(s))

def rever(st):
    if st == "":
        return st
    else:
        return rever(st[1:])+ st[0]
print(rever("1221"))
#print(rever(input("Enter a string: ")))

rj = "abcdscdccdc"
print(rj.count("cdc"))

