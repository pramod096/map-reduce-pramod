# Pramod Gonegari
# Sorting

input = open("out01.txt", "r")  # passing mapped data as input
output = open("sortedOutput.txt", "w") # sorted data will be written to this file
lines = input.readlines()
lines.sort()

for line in lines:
    output.write(line)

input.close()
output.close()
