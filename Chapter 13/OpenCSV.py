def countNumberOfLines(myfile):
    count = 0

    for file in myfile:
        count +=1
    return count

def main():
    file = open("file.CSV   ", 'r')
    print("Number of lines is ", countNumberOfLines(file))
    file.close()

main()
