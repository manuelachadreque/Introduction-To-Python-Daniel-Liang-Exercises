def ReadFile(file):
    with open(file) as file:
        data = file.read()
    return data


def ReadFile1(file, NLines):
    count = 1
    with open(file) as file:
        for file in file:
            if count <= NLines:
                print(file)
            count += 1


def ReadFile2(file, NLines):
    count = 1
    with open(file) as file:
        while count <= NLines:
            print(file.readline())
            count += 1


def ReadVar(file):
    with open(file, 'r') as file:
        data = file.readlines()
    return data


# print(ReadVar('source1.txt'))

r = ReadVar('source1.txt')

print(r)
import pandas as pd

data = pd.DataFrame(r)
print(data)

