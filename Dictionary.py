di = {"sam": 451, "sim": 249, "rain": 873, "train": 468, "bicycle": 943}
#Using for loop
for k in di:
    print("key:", k, "value:", di[k])

print()

#using tuples
for e,f in di.items():
    print("key:",e, "value:", f)
