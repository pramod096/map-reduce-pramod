# Pramod Gonegari
# Learning Mapper


input = open("purchases.txt", "r")  # open file, read-only
output = open("out01.txt", "w")  # open file, write
for line in input:
    rowList = line.strip().split("    ")
    print(rowList)
    print(len(rowList))
    if len(rowList) == 6:
        date, time, location, dept, amount, payType = rowList  # assign names
        print("{0}\t{1}".format(location, amount))
        output.write("{0}\t{1}\n".format(location, amount))
input.close()
output.close()
