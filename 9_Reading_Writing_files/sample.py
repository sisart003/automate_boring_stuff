import os

##########################################################################

# Backslash on Windows and Forward Slash on OS X and Linux

# pant = os.path.join('usr', 'bin', 'spam')
# print(pant)

# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

# for filename in myFiles:
#     print(os.path.join('C:\\Users\\Tess', filename))

##########################################################################

# The Current Working Directory

# print(os.getcwd())
# os.chdir('C:\\Windows\\System32')

# print(os.getcwd())

##########################################################################

# print(os.makedirs('C:\\sisart\\chris\\hart'))

##########################################################################

# The os.path Module

# print(os.path.abspath('.'))
# print(os.path.abspath('.\\Scripts'))
# print(os.path.isabs('.'))
# print(os.path.isabs(os.path.abspath('.')))
# print(os.path.relpath('C:\\Windows', 'C:\\'))
# print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
# print(os.getcwd())

# path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path))
# print(os.path.dirname(path))

# calcFilePath = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.split(calcFilePath))
# print(calcFilePath.split(os.path.sep))

##########################################################################

# Finding Files Sizes and Folder Contents

# print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
# print(os.listdir('C:\\Windows\\System32'))

# totalSize = 0
# for filename in os.listdir('C:\\Windows\\System32'):
#     totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

# print(totalSize)

##########################################################################

# Checking Path Validity

# print(os.path.exists('C:\\Windows'))
# print(os.path.exists('C:\\some_made_up_folder'))
# print(os.path.isdir('C:\\Windows\\System32'))
# print(os.path.isfile('C:\\Windows\\System32'))
# print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
# print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))
# print(os.path.exists('D:\\'))

##########################################################################

# helloFile = open('C:\\Users\\Tess\\Desktop\\hello.txt')

# Reading the Contents of Files

# helloContent = helloFile.read()
# print(helloContent)

# sonnetFile = open('sonnet29.txt')
# print(sonnetFile.readlines())

# baconFile = open('bacon.txt', 'w')
# baconFile.write('Hello world!\n')

# baconFile.close()
# baconFile = open('bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable.')

# baconFile.close()
# baconFile = open('bacon.txt')
# content = baconFile.read()
# baconFile.close()
# print(content)

##########################################################################

# Saving Variables with the shelve Module

import shelve
# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats

# print(type(shelfFile))
# print(shelfFile['cats'])

# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))

# shelfFile.close()

##########################################################################

# Saving Variables with the pprint.pformat() Function

import pprint
# cats = [{'name' : 'Zophie', 'desc' : 'chubby'}, {'name' : 'Pooka', 'desc' : 'fluffy'}]
# pprint.pformats(cats)

# fileObj = open('myCats.py', 'w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')

# fileObj.close()