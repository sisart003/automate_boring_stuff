import PyPDF2, docx

# Extracting Text from PDFs

# pdfFileObj = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())
# pdfFileObj.close()

############################################################

# Decrypting PDFs

# pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# print(pdfReader.isEncrypted)
# print(pdfReader.getPage(0)) # cause error
# pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# pdfReader.decrypt('rosebud')
# pageObj = pdfReader.getPage(0)

############################################################

# Copying Pages

# pdf1File = open('meetingminutes.pdf', 'rb')
# pdf2File = open('meetingminutes2.pdf', 'rb')
# pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
# pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
# pdfWriter = PyPDF2.PdfFileWriter()

# for pageNum in range(pdf1Reader.numPages):
#     pageObj = pdf1Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)

# for pageNum in range(pdf2Reader.numPages):
#     pageObj = pdf2Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)

# pdfOutputFile = open('combineminutes.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close()
# pdf1File.close()
# pdf2File.close()

############################################################

# Rotating Pages

# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# page = pdfReader.getPage(0)
# page.rotateClockwise(90)
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(page)
# resultPdfFile = open('rotatedPage.pdf', 'wb')
# pdfWriter.write(resultPdfFile)
# resultPdfFile.close()
# minutesFile.close()

############################################################

# Overlaying Pages

# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# minutesFirstPage = pdfReader.getPage(0)
# pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
# minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(minutesFirstPage)

# for pageNum in range(1, pdfReader.numPages):
#     pageObj = pdfReader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)

# resultPdfFile = open('watermarkedCover.pdf', 'wb')
# pdfWriter.write(resultPdfFile)
# minutesFile.close()
# resultPdfFile.close()

############################################################

# Encrypting PDFs

# pdfFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFile)
# pdfWriter = PyPDF2.PdfFileWriter()

# for pageNum in range(pdfReader.numPages):
#     pdfWriter.addPage(pdfReader.getPage(pageNum))

# pdfWriter.encrypt('swordfish')
# resultPdf = open('encryptedminutes.pdf', 'wb')
# pdfWriter.write(resultPdf)
# resultPdf.close()

############################################################

# Reading Word Documents

# doc = docx.Document('demo.docx')
# print(len(doc.paragraphs))
# print(doc.paragrapsh[0].text)
# print(doc.paragrapshs[1].text)
# print(len(doc.paragrpahs[1].runs))
# print(doc.paragraphs[1].runs[0].text)
# print(doc.paragraphs[1].runs[1].text)
# print(doc.paragraphs[1].runs[2].text)
# print(doc.paragraphs[1].runs[3].text)

############################################################

# Getting the Full Text from a .docx File

# import readDocx

# def getText(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     return '\n'.join(fullText)

# print(readDocx.getText('demo.docx'))

############################################################

# Run Attributes

# Attribute         Description
# bold              The text appears in bold.
# italic            The text appears in italic.
# underline         The text is underlined.
# strike            The text appears with strikethrough.
# double_strike     The text appears with double strikethrough.
# all_caps          The text appears in capital letters.
# small_caps        The text appears in capital letters, with lowercase letters two points smaller.
# shadow            The text appears with a shadow.
# outline           The text appears outlined rather than solid.
# rtl               The text is written right-to-left.
# imprint           The text appears pressed into the page.
# emboss            The text appears raised off the page in relief.

# doc = docx.Document('demo.docx')
# print(doc.paragraphs[0].text)
# print(doc.paragraphs[0].style) # The exact id may be different
# doc.paragraphs[0].style = 'Normal'
# doc.paragraphs[1].text
# print((doc.paragraphs[1].runs[0].text, doc.paragraphs[1].runs[1].text, doc.paragraphs[1].runs[2].text, doc.paragraphs[1].runs[3].text))
# doc.paragraphs[1].runs[0].style = 'QuoteChar'
# doc.paragraphs[1].runs[1].underline = True
# doc.paragraphs[1].runs[3].underline = True
# doc.save('restyled.docx')

############################################################

# Writing Word Documents

# doc = docx.Document()
# print(doc.add_paragraph('Hello World'))
# paraObj1 = doc.add_paragraph('This is a second paragraph.')
# paraObj2 = doc.add_paragraph('This is a yet another paragraph.')
# paraObj1.add_run(' This text is being added to the second paragraph.')
# doc.save('helloworld.docx')

############################################################

# Adding Headings

# doc = docx.Document()
# doc.add_heading('Header 0', 0)
# doc.add_heading('Header 1', 1)
# doc.add_heading('Header 2', 2)
# doc.add_heading('Header 3', 3)
# doc.add_heading('Header 4', 4)
# doc.save('headings.docx')

############################################################

# Adding Line and Page Breaks

# doc = docx.Document()
# doc.add_paragraph('This is on the first page!')
# doc.paragraphs[0].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
# doc.add_paragraph('This is on the second page!')
# doc.save('twoPage.docx')

############################################################

# Adding Pictures

# doc.add_picture('zophie.png', width=docx.shared.Inches(1), height=docx.shared.Cm(4))

############################################################

