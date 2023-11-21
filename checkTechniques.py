import csv

technique_set = set()

with open('piecesOld.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        curList = row[5].split(',')
        for item in curList:
            if item == '':
                print(row[0])
            technique_set.add(item)

    file.close()

with open('techniques.csv', 'w', newline='') as writeFile:
    csv_writer = csv.writer(writeFile)
    for technique in technique_set:
        csv_writer.writerow([technique, 'placeholder', 'placeholder'])

    writeFile.close()
