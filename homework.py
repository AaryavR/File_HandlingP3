with open("Codingal.txt") as fp:
    data1 = fp.read()

with open("sample_doc.txt") as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2

print("Merging two files....")
with open ('MergedFile.txt', 'w') as fp:
    fp.write(data1)
fp.close()
print("Done")

outputFile = open('MergedFile,txt', 'w')

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