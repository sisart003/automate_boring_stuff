# This script runs on Windows only, and you must have Word installed
import win32com.client # install with "pip install pywin32==224"
import docx
wordFilename = 'yourDocxFile.docx'
pdfFilename = 'yourPdfFile.pdf'

doc = docx.Document()
# Code to create Word document goes here.
doc.save(wordFilename)

wdFormatPDF = 17 # word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, fileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()