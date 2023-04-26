import GenerateCharacters

NUMBER_OF_CHARS =175
CHAR_PERlINE =25

for i in range(NUMBER_OF_CHARS):
    print(GenerateCharacters.generateLowerCase(), end ='')
    if(i+1) % CHAR_PERlINE == 0:
        print()
