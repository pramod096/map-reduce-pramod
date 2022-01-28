# Pramod Gonegari
# Reduce

input = open("sortedOutput.txt", "r")
output = open("finalOutput.txt", "w")

thisKey = ""
thisValue = 0.0

for line in input:
    data = line.strip().split('\t')
    store, amount = data
    if store != thisKey:
        if thisKey:

            # output the last key value pair result
            output.write('---------------------------------\n')
            finalValue = "| " + \
                thisKey.ljust(16) + " | " + \
                "{:.2f}".format(thisValue).ljust(10) + " |\n"
            output.write(finalValue)

        # start over when changing keys
        thisKey = store
        thisValue = 0.0

    # apply the aggregation function
    thisValue += float(amount)

# output the final entry when done

output.write('---------------------------------\n')
output.write("| " +
             thisKey.ljust(18) + " | " +
             "{:.2f}".format(thisValue).ljust(10) + " |\n")
output.write('---------------------------------\n')

input.close()
output.close()
