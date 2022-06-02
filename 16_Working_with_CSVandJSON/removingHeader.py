#! python3
# Removes the header from all CSV files in the current working directory

# 1. Find all the CSV files in the current working directory.
# 2. Read in the full contents of each file.
# 3. Write out the contents, skipping the first line, to a new CSV file.

# At the code level, this means the program will need to do the following:

# 1. Loop over a list of files from os.listdir(), skipping the non-CSV files.
# 2. Create a CSV reader object and read in the contents of the file, using
# the line_num attribute to figure out which line to skip.
# 3. Create a CSV writer object and write out the read-in data to the new file.

import csv, os
os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)

    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip first row
        
        # Write out the CSV file
        csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
        csvWriter = csv.writer(csvFileObj)

        for row in csvRows:
            csvWriter.writerow(row)
        csvFileObj.close()

        csvRows.append(row)
    csvFileObj.close()

# Ideas for Similar Programs
# The programs that you could write for CSV files are similar to the kinds you
# could write for Excel files, since they’re both spreadsheet files. You could
# write programs to do the following:
# •	 Compare data between different rows in a CSV file or between multiple CSV files.
# •	 Copy specific data from a CSV file to an Excel file, or vice versa.
# •	 Check for invalid data or formatting mistakes in CSV files and alert the user to these errors.
# •	 Read data from a CSV file as input for your Python programs.    