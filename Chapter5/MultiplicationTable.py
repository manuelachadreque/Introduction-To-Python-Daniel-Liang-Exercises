print("          Multiplication Table")
print("   ", end=' ')

for i in range(1, 10):
    print("  ", i, end= ' ')
print()
print("------------------------------------------------")

# Display the table
for i in range(1,10):
    print(i, "|", end =' ')
    for j in range(1,10):
        print(format(i*j, "4d"), end = ' ')
    print()