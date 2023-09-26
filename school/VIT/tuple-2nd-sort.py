def keysort(tup):
    return tup[1]

tup = (('a',23),('b',22),('c',25))

newtup = sorted(tup, key=keysort)
print(newtup)
