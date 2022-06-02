import shutil, os, zipfile

# Copying Files and Folders

# os.chdir('D:\\')
# shutil.copy('D:\\spam.txt', 'D:\\delicious')
# shutil.copy('eggs.txt', 'D:\\delicious\\eggs2.txt')

# os.chdir('D:\\')
# shutil.copytree('D:\\delicious', 'D:\\bacon_backup')

###########################

# Moving and Renaming Files and Folders

# shutil.move('D:\\bacon.txt', 'D:\\delicious')
# shutil.move('D:\\bacon.txt', 'D:\\delicious\\new_bacon.txt')
# shutil.move('D:\\spam.txt', 'D:\\eggs')

###########################

# Walking a Directory Tree

# for folderName, subfolders, filenames in os.walk('D:\\delicious'):
#     print('The current folder is ' + folderName)

#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    
#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': ' + filename)
    
#     print('')

#########################################

# Compressing Files and with the zipfile Module

# Reading ZIP Files

# os.chdir('D:\\') # move to the folder with example.zip
# exampleZip = zipfile.ZipFile('cats.zip')
# print(exampleZip.namelist())

# spamInfo = exampleZip.getinfo('cats/catnames.txt')
# print(spamInfo.file_size)
# print(spamInfo.compress_size)

# print('Compressed file is %sx smaller! ' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
# exampleZip.close()

#########################################

# Extracting from ZIP Files

# os.chdir('D:\\') # move to the folder with example.zip
# exampleZip = zipfile.ZipFile('cats.zip')
# exampleZip.extractall()
# exampleZip.extract('mina.jpg', 'D:\\delicious')
# exampleZip.close()

#########################################

# Creating and Adding to ZIP Files

# os.chdir('D:\\')
# newZip = zipfile.ZipFile('new.zip', 'w')
# newZip.write('catnames.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()