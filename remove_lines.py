outputFile = open('UpdatedFile,txt', 'w')

inputFile = open("Repeated.txt", 'r')

lines_so_far = set()
print("Elimating duplicate lines...")
for line in inputFile:
    if line not in lines_so_far:
        outputFile.write(line)
        lines_so_far.add(line)

outputFile.close()
inputFile.close()
print("Done")