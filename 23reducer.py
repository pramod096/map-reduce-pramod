# Pramod Gonegari
# Reducer

import sys

thisKey = ""
thisValue = 0.0

for line in sys.stdin:
    data = line.strip().split('\t')
    if(data != ['']):
        year, count = data
        if year != thisKey:
            if thisKey:

                # output the last key value pair result
                print('---------------------------------')
                finalValue = "| " + \
                    thisKey.ljust(16) + " | " + \
                    "{:.2f}".format(thisValue).ljust(10) + " |"
                print(finalValue)

            # start over when changing keys
            thisKey = year
            thisValue = 0.0

    # apply the aggregation function
    thisValue += float(count)

# output the final entry when done

print('---------------------------------')
print("| " +
      thisKey.ljust(18) + " | " +
      "{:.2f}".format(thisValue).ljust(10) + " |")
print('---------------------------------')
