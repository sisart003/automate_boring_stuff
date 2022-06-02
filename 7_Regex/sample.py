# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True

# print('415-555-4242 is a phone Number: ')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number: ')
# print(isPhoneNumber('Moshi moshi'))

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)

# print('Done')

################################################################################################################################################################

# http://regexpal.com/

################################################################################################################################################################

# Matching Regex Objects 
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242')
# print('Hone number found: ' + mo.group())

################################################################################################################################################################

# Grouping with Parentheses
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.groups())

################################################################################################################################################################

# Matching Multiple Groups with the Pipe
# heroRegex = re.compile (r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey')
# print(mo1.group())

# mo2 = heroRegex.search('Tina Fey and Batman')
# print(mo2.group())

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))

################################################################################################################################################################

# Optional Matching with the Question Mark
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())

################################################################################################################################################################

# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search('My Number is 415-555-4242')
# print(mo1.group())

# mo2 = phoneRegex.search('My Number is 555-4242')
# print(mo2.group())

################################################################################################################################################################

# Matching Zero or More with the Star
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group)

# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group)

# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo3.group())

################################################################################################################################################################

# Matching One or More with the Plus
# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batwoman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo2.group())

# mo3 = batRegex.search('The Adventures of Batman')
# print(mo3 == None)

################################################################################################################################################################

# Matching Specific Repetitions with Curly Brackets
# haRegex = re.compile(r'(Ha){3}')
# mo1 = haRegex.search('HaHaHa')
# print(mo1.group())

# mo2 = haRegex.search('Ha')
# print(mo2 == None)

################################################################################################################################################################

# Greedy and Nongreedy Matching
# greedyHaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
# print(mo1.group())

# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHaHa')
# print(mo2.group())

################################################################################################################################################################

# The findall() Method
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())

################################################################################################################################################################

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# print(phoneNumRegex.findall('Cell: 415-555-999 Work: 212-555-000'))

################################################################################################################################################################

# Shorthand character class     Represents
# \d                            Any numeric digit from 0 to 9.
# \D                            Any character that is not a numeric digit from 0 to 9.
# \w                            Any letter, numeric digit, or the underscore character.
#                               (Think of this as matching “word” characters.)
# \W                            Any character that is not a letter, numeric digit, or the
#                               underscore character.
# \s                            Any space, tab, or newline character. (Think of this as
#                               matching “space” characters.)
# \S                            Any character that is not a space, tab, or newline.

################################################################################################################################################################

# Character Classes
# xmasRegex = re.compile(r'\d+\s\w+')
# print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

################################################################################################################################################################

# Making Your Own Character Classes
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD'))

################################################################################################################################################################

# The Caret and Dollar Sign Characters
# beginsWithHello = re.compile(r'^Hello')
# print(beginsWithHello.search('Hello World'))

# endsWithNumber = re.compile(r'\d$')
# print(endsWithNumber.search('Your number is 42'))

# wholeStringIsNum = re.compile(r'^\d+$')
# print(wholeStringIsNum.search('123456789'))

################################################################################################################################################################

# Wildcard Character
# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))

################################################################################################################################################################

# Matching Everything with Dot-Star
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))

# nongreedyRegex = re.compile(r'<.*?>')
# mo = nongreedyRegex.search('<to serve man> for dinner.>')
# mo.group()

# greedyRegex = re.compile(r'<.*>')
# mo = greedyRegex.search('<To serve man> for dinner.>')

################################################################################################################################################################

# Matching Newlines with the Dot Character
# noNewlineRegex = re.compile('.*')
# print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# newlineRegex = re.compile('.*', re.DOTALL)
# print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nuphold the law.').group())

################################################################################################################################################################

# Review of Regex Symbols
# This chapter covered a lot of notation, so here’s a quick review of what
# you learned:
# •	 The ? matches zero or one of the preceding group.
# •	 The * matches zero or more of the preceding group.
# •	 The + matches one or more of the preceding group.
# •	 The {n} matches exactly n of the preceding group.
# •	 The {n,} matches n or more of the preceding group.
# •	 The {,m} matches 0 to m of the preceding group.
# •	 The {n,m} matches at least n and at most m of the preceding group.
# •	 {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# •	 ^spam means the string must begin with spam.
# •	 spam$ means the string must end with spam.
# •	 The . matches any character, except newline characters.
# •	 \d, \w, and \s match a digit, word, or space character, respectively.
# •	 \D, \W, and \S match anything except a digit, word, or space character,
# respectively.
# •	 [abc] matches any character between the brackets (such as a, b, or c).
# •	 [^abc] matches any character that isn’t between the brackets.

################################################################################################################################################################

# Case-Insensitive Matching
# robocop = re.compile(r'robocop', re.I) # re.IGNORECASE
# print(robocop.search('RoboCop is part man, part machine, all cop.').group())
# print(robocop.search('ROBOCOP protects the innocent.').group())
# print(robocop.search(Al, why does your programming book talk about robocop so much?).group())

################################################################################################################################################################

# Substituting Strings with the sub() Method
# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

################################################################################################################################################################

# Managing Complex Regexes
# import re
# phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# phoneRegex = re.compile(r'''
#         (\d{3}|\(\d{3}\))?              # area code
#         (\s|-|\.)?                      # separator
#         \d{3}                           # first 3 digits
#         (\s|-|\.)                       # separator
#         \d{4}                           # last 4 digits
#         (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
# ''', re.VERBOSE)

################################################################################################################################################################

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

