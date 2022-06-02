# 1. Reads the data from the Excel spreadsheet
# 2. Counts the number of census tracts in each county
# 3. Counts the total population of each county
# 4. Prints the results

# This means your code will need to do the following:

# 1. Open and read the cells of an Excel document with the openpyxl module.
# 2. Calculate all the tract and population data and store it in a data structure.
# 3. Write the data structure to a text file with the .py extension using the pprint module.

#! python3
# Tabulates population and number of census tracts for each country.

import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

# Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exists.
    countyData.setDefault(state, {})

    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {'tracts' : 0, 'pop' : 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1

    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)
# Open a new text file and write the contens of countyData to it.
print('Writing Results...')
resultFile = open('censys2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')



# Ideas for Similar Programs
# Many businesses and offices use Excel to store various types of data, and
# it’s not uncommon for spreadsheets to become large and unwieldy. Any
# program that parses an Excel spreadsheet has a similar structure: it loads
# the spreadsheet file, preps some variables or data structures, and then loops
# through each of the rows in the spreadsheet. Such a program could do
# the following:
# •	 Compare data across multiple rows in a spreadsheet.
# •	 Open multiple Excel files and compare data between spreadsheets. Working with Excel Spreadsheets 313
# •	 Check whether a spreadsheet has blank rows or invalid data in any cells and alert the user if it does.
# •	 Read data from a spreadsheet and use it as the input for your Python programs.