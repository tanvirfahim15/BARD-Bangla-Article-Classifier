# Uniquify all urls after classification
# File flow: bangladesh.csv -> _unique.txt.txt
import csv
import itertools
import sys

# configuration
fileMode = "w"

for i in range(1, len(sys.argv)):
    filename = sys.argv[i]

    # Unique urls fetched
    f = csv.reader(open(filename))
    processCount = 0
    col = set([])
    for row in itertools.islice(f, 0, 3000000):
        print(row[0])
        col.add(row[0])
        processCount = processCount+1
        print(processCount)

    col=list(col)
    print("Total unique:"+str(col.__len__()))

    # write to file
    file= open("unique_"+filename, fileMode)
    for item in col:
        file.write(item+"\n")
    file.close()

