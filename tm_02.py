fileName1 = "tm_02a.txt"
fileName2 = "tm_02b.txt"
fileName3 = "tm_02c.txt"
try:
    file1 = open(fileName1,"r")
    file3 = open(fileName3,"a")
    note = file1.readlines()
    for i in range(len(note)):
        file3.write(note[i])
    file3.write("\n")
except:
    print("error !")
file1.close()
try:
    file2 = open(fileName2,"r")
    note = file2.readlines()
    for i in range(len(note)):
        file3.write(note[i])
except:
    print("error !")
file2.close()
file3.close()