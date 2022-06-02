#! python3
# Combines all the PDFs in the current working directory into a single PDF.


# 1. Find all PDF files in the current working directory.
# 2. Sort the filenames so the PDFs are added in order.
# 3. Write each page, excluding the first page, of each PDF to the output file.

# In terms of implementation, your code will need to do the following:

# 1. Call os.listdir() to find all the files in the working directory and
# remove any non-PDF files.
# 2. Call Python’s sort() list method to alphabetize the filenames.
# 3. Create a PdfFileWriter object for the output PDF.
# 4. Loop over each PDF file, creating a PdfFileReader object for it.
# 5. Loop over each page (except the first) in each PDF file.
# 6. Add the pages to the output PDF.
# 7. Write the output PDF to a file named allminutes.pdf


import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (Except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

# Ideas for Similar Programs
# Being able to create PDFs from the pages of other PDFs will let you make
# programs that can do the following:
# •	 Cut out specific pages from PDFs.
# •	 Reorder pages in a PDF.
# •	 Create a PDF from only those pages that have some specific text,
# identified by extractText().