import csv, json

# reader Objects

# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)

# print(exampleData[0][0])
# print(exampleData[0][1])
# print(exampleData[0][2])
# print(exampleData[1][1])
# print(exampleData[6][1])

############################################################

# Reading Data from reader Objects in a for Loop

# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

############################################################

# writer Objects

# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))
# print(outputWriter.writerow(['Hellow, world!', 'eggs', 'bacon', 'ham']))
# print(outputWriter.writerow([1, 2, 3.141592, 4]))
# outputFile.close()

############################################################

# The delimiter and lineterminator Keyword Arguments

# csvFile = open('example.tsv', 'w', newline='')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# print(csvWriter.writerow(['apples', 'oranges', 'grapes']))
# print(csvWriter.writerow(['eggs', 'bacon', 'ham']))
# print(csvWriter.writerow(['span', 'span', 'span', 'span', 'span', 'span']))
# csvFile.close()

############################################################

# DictReader and DictWriter CSV Objects

# exampleFile = open('exampleWithHeader.csv')
# exampleDictReader = csv.DictReader(exampleFile)

# for row in exampleDictReader:
#     print(row['Timestamp'], row['Fruit'], row['Quantity'])

# DictReader without header

# exampleFile = open('example.csv')
# exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])

# for row in exampleDictReader:
#     print(row['time'], row['name'], row['amount'])

# outputFile = open('output.csv', 'w', newline='')
# outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
# outputDictWriter.writeheader()
# print(outputDictWriter.writerow({'name' : 'Alice', 'Pet' : 'cat', 'Phone' : '555-1234'}))
# print(outputDictWriter.writerow({'Name' : 'Bob', 'Phone' : '555-9999', 'Pet' : 'dog'}))
# outputFile.close()

############################################################

# Reading JSON with the loads() Function

# stringOfJsonData = '{"name" : "Zophie", "isCat" : true, "miceCaught" : 0, "felineIQ" : null}'
# pythonValue = '{"name" : "Zophie", "isCat" : true, "miceCaught" : 0, "felineIQ" : null}'

# jsonDataAsPythonValue = json.loads(stringOfJsonData)
# print(jsonDataAsPythonValue)

# stringOfJsonData = json.dumps(pythonValue)
# print(stringOfJsonData)