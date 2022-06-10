fileName1 = "tm_03a.txt"
fileName2 = "tm_03b.txt"
# 
try:
    file1 = open(fileName1,"r")
    note = file1.read()
    file1.close()
except:
    print("file 1 not found !")
# 
try:

    file2 = open(fileName2,"w")
    for i in range(len(note)):
        asc = ord(note[i])
        if(asc >= 65 and asc <= 90):
            file2.write(note[i])
            file2.write("\n")
    file2.close()
except:
    print("error in write !")
# 
try:
    file3 = open(fileName2,"r")
    note = file3.readlines()
    file3.close()
    for i in range(len(note)):
        line = note[i]
        if(line[0] == 'A'):
            print(f"in line {i+1} : {line[0]}")
except:
    print("file 2 not found !")