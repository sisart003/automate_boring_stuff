# Escape character      Prints as
# \'                    Single quote
# \"                    Double quote
# \t                    Tab
# \n                    Newline (line break)
# \\                    Backslash

#######################################

# print('''Dear Alice,
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.

# Sincerely,
# Bob''')

#######################################

# print('How are you?')
# feeling = input()

# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')

#######################################

# while True:
#     print('Enter your age: ')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')

# while True:
#     print('Select a new password (letters and numbers only): ')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')

#######################################

# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# picnicItems = {'sandwiches' : 4, 'apples' : 12, 'cups' : 4, 'cookies' : 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 8)

#######################################