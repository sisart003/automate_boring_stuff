# Creating, Uploading and Listing Spreadsheets
import ezsheets

# ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
# print(ss.title)

# ss = ezsheets.createSpreadsheet('Title of My New Spreadsheet')
# print(ss.title)

# ss = ezsheets.upload('my_spreadsheet.xlsx')
# print(ss.title)

# ezsheets.listSpreadsheets()

##################################################################

# Spreadsheet Attributes

# ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
# print(ss.title)
# ss.title = 'Class Data' # Change the title.
# ss.spreadsheetId # The unique ID (this is a read-only attribute)
# print(ss.url) # The original URL (this is a read-only attribute)
# print(ss.sheetTitles) # The titles of all the Sheet objects
# print(ss.sheets) # The Sheet objects in this Spreadsheet, in order.
# print(ss[0]) # The first Sheet object in this Spreadsheet.
# print(ss['Students']) # Sheets can also be accessed by title.
# del ss[0] # Delete the first Sheet object in this Spreadsheet
# print(ss.sheetTitle) # The "Students" Sheet object has been deleted:
# ss.refresh()

##################################################################

# Downloading and Uploading Spreadsheets

# ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
# print(ss.title)
# ss.downloadAsExcel() # Downloads the spreadsheet as an Excel file.
# ss.downloadAsODS() # Downloads the spreadsheet as an OpenOffice file.
# ss.downloadAsCSV() # Only downloads the first sheet as a CSV file.
# ss.downloadAsTSV() # Only downloads the first sheet as a TSV file.
# ss.downloadAsPDF() # Downloads the spreadsheet as a PDF.
# ss.downloadAsHTML() # Downloads the spreadsheet as a ZIP of HTML files.
# ss.downloadAsExcel('different_filename.xlsx')

##################################################################

# Deleting Spreadsheets

# ss = ezsheets.createSpreadsheet('Delete me') # Create the spreadsheet.
# ezsheets.listSpreadsheets() # Confirm that we've created a spreadsheet.
# ss.delete() # Delete the Spreadsheet.
# ss.delete(permanent=True) # Permenent Delete
# ezsheets.listSpreadsheets()

##################################################################

# Sheet Objects

# ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
# ss.sheets # The Sheet objects in this Spreadsheet, in order.
# ss.sheets[0] # Gets the first Sheet object in this Spreadsheet.
# ss[0]
# ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet.
# ss['Classes'] # Sheets can also be accessed by title.

##################################################################

# Reading and Writing Data

# ss = ezsheets.createSpreadsheet('My Spreadsheet')
# sheet = ss[0] # Get the first sheet in this spreadsheet.
# sheet.title
# sheet = ss[0]
# sheet['A1'] = 'Name' # Set the value in cell A1
# sheet['B1'] = 'Age'
# sheet['C1'] = 'Favorite Movie'
# sheet['A1'] # Read the value in cell A1.
# sheet['A2'] # Empty cells return a blank string.
# sheet[2, 1] # Column 2, Row 1 is the same address as B1.
# sheet['A2'] = 'Alice'
# sheet['B2'] = 30
# sheet['C2'] = 'RoboCop'
# sheet.refresh()

##################################################################

# Column and Row Addressing

# ezsheets.convertAddress('A2') # Converts Addresses...
# ezsheets.convertAddress(1, 2) # ...and converts them back, too.
# ezsheets.getColumnLetterOf(2)
# ezsheets.getColumnNumberOf('B')
# ezsheets.getColumnLetterOf(999)
# ezsheets.getColumnNumberOf('ZZZ')

##################################################################

# Reading and Writing Entire Columns and Rows

#               A                 B                       C                       D
# 1           PRODUCE           COST PER POUND          POUNDS SOLD             TOTAL
# 2           Potatoes          0.86                    21.6                    18.58
# 3           Okra              2.26                    38.6                    87.24
# 4           Fava beans        2.69                    32.8                    88.23
# 5           Watermelon        0.66                    27.3                    18.02
# 6           Garlic            1.19                    4.9                     5.83
# 7           Parsnips          2.27                    1.1                     2.5
# 8           Asparagus         2.49                    37.9                    94.37

# ss = ezsheets.upload('produceSales.xlsx')
# sheet = ss[0]
# print(sheet.getRow(1)) # The first row is row 1, not row 0
# print(sheet.getRow(2))
# columnOne = sheet.getColumn(1)
# print(sheet.getColumn(1))
# print(sheet.getColumn('A')) # Same result as getColumn(1)
# print(sheet.getRow(3))
# sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
# print(sheet.getRow(3))
# columnOne = sheet.getColumn(1)
# for i, value in enumerate(columnOne):
#     # Make the Python list contain uppercase strings:
#     columnOne[i] = value.upper()

# sheet.updateColumn(1, columnOne) # Update the entire column in one request

# rows = sheet.getRows() # Get every row in the spreadsheet.
# print(rows[0]) # Examine the values in the first row.
# print(rows[1])
# rows[1][0] = 'PUMPKIN' # Change the produce name.
# print(rows[1])
# print(rows[10])
# rows[10][2] = '400' # Change the pounds sold.
# rows[10][3] = '904' # change the total
# print(rows[10])
# sheet.updateRows(rows) # Update the online spreadsheet with the changes.

# print(sheet.rowCount) # The number of rows in the sheet.
# print(sheet.columnCount) # The number of columns in the sheet.
# sheet.columnCount = 4 # Change the number of columns to 4.
# print(sheet.columnCount) # Now the number of columns in the sheet is 4.

##################################################################

# Creating and Deleting Sheets

# ss = ezsheets.createSpreadsheet('Multiple Sheets')
# print(ss.sheetTitles)
# print(ss.createSheet('Spam')) # Create a new sheet at the end of the list of sheets.
# print(ss.createSheet('Eggs')) # Create another new sheet.
# print(ss.sheetTitles)
# print(ss.createSheet('Bacon', 0)) # Create a sheet at index 0 in the list of sheets.
# print(ss.sheetTitles)

# print(ss.sheetTitles)
# ss[0].delete()
# print(ss.sheetTitles)
# ss['Spam'].delete() # Delete the "Spam" sheet.
# print(ss.sheetTitles)
# sheet = ss['Eggs'] # Assign a variable to the "Eggs" sheet.
# sheet.delete() # Delete the "Eggs" sheet.
# print(ss.sheetTitles)
# ss[0].clear() # Clear all the cells on the "Sheet1" sheet.
# print(ss.sheetTitles) # The "Sheet1" sheet is empty but still exists.

##################################################################

# Copying Sheets

# ss1 = ezsheets.createSpreadsheet('First Spreadsheet')
# ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')
# print(ss1[0])
# ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
# ss1[0].copyTo(ss2) # Copy the ss1's Sheet1 to the ss2 spreadsheet.
# print(ss2.sheetTitles) # ss2 now contains a copy of ss1's Sheet1