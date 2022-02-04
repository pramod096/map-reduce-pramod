# Pramod Gonegari

import sys

# Iterating through Standard Input
for line in sys.stdin:
    csvData = line.strip().split(',')
    if (len(csvData) == 6):
        show_id, type, date_added, release_year, rating, duration = csvData

        # release year
        print(release_year, "\t", 1)
