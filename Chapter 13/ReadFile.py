infile =open("file.CSV", 'r')
newfile = open("newFile.txt", 'w')
for line in infile:
    if line.startswith('T') !=True:
        newfile.write(line)
infile.close()
newfile.close()



