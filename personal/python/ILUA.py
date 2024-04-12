import math
import os

def sizeconverter(size):
    if size < 1024:
        return str(size) + " B"
    elif size < 1024**2:
        return str(round(size/1024, 2)) + " KB"
    elif size < 1024**3:
        return str(round(size/(1024**2), 2)) + " MB"
    elif size < 1024**4:
        return str(round(size/(1024**3), 2)) + " GB"
    else:
        return str(round(size/(1024**4), 2)) + " TB"

n = 10**16
loopervar = math.floor(n/math.log2(n))
string = "i love you"
try:
    f = open('ILUA.txt', 'w')
    f.write(string+"\n")
    f.close()
    filesize = os.path.getsize('ILUA.txt')
    print(sizeconverter(filesize))
    try:
        for i in range(loopervar):
            reader = open('ILUA.txt', 'r')
            writer = open('ILUA.txt', 'a')
            print("total number of lines in the file:", reader.readlines())
            writer.write(reader.read())
            writer.close()
            reader.close()
            filesize = os.path.getsize('ILUA.txt') 
            print("total number of bytes in the file:",sizeconverter(filesize))
    except:
        print('Error reading file')
        quit()
except:
    print('Error opening file')
    quit()