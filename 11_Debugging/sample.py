# Raising Exceptions

# from tempfile import TemporaryFile


# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string')
#     if width <= 2:
#         raise Exception('Width must be greater than 2')
#     if height <= 2:
#         raise Exception('Height must be greater than 2')

#     print(symbol * width)

#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)

# for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#         print('An exception happened: ' + str(err))

##########################

# Getting the Traceback as a String

# def spam():
#     bacon()

# def bacon():
#     raise Exception('This is the error message.')

# spam()

# import traceback

# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('errorInfo.txt', 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt.')

#########################################

# Assertions
# ages = [16, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.reverse()
# print(ages)
# assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

# Assertion in a Traffic Light Simulation

# market_2nd = {'ns' : 'green', 'ew' : 'red'}
# mission_16th = {'ns' : 'red', 'ew' : 'green'}

# def switchLights(stoplight):
#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] == 'red'
#         elif stoplight == 'red':
#             stoplight[key] = 'green'

#         assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

# switchLights(market_2nd)

#########################################

# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of Program')

# def factorial(n):
#     logging.debug('Start of factorial(%s%%)' % (n))
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(%s%%)' % (n))
#     return total

# print(factorial(5))
# logging.debug('End of Program')

#########################################

# Logging Levels

# -----------------------------------------------------------------------------------
# | Level   |    Logging Function   |                   Description                 |
# -----------------------------------------------------------------------------------
# | DEBUG   |    logging.debug()    |   The lowest level. Used for small details.   |
# |         |                       |   Usually you care about these messages       |
# |         |                       |   only when diagnosing problems.              |
# -----------------------------------------------------------------------------------
# | INFO    |   logging.info()      |   Used to record information on general       |
# |         |                       |   events in your program or confirm that      |
# |         |                       |   things are working at their point in the    |
# |         |                       |   program.                                    |
# -----------------------------------------------------------------------------------
# | WARNING |   logging.warning()   |   Used to indicate a potential problem        |
# |         |                       |   that doesn’t prevent the program from       |
# |         |                       |   working but might do so in the future.      |
# -----------------------------------------------------------------------------------
# | ERROR   |   logging.error()     |   Used to record an error that caused the     |
# |         |                       |   program to fail to do something.            |
# -----------------------------------------------------------------------------------
# | CRITICAL|   logging.critical()  |   The highest level. Used to indicate a       |
# |         |                       |   fatal error that has caused or is about     |
# |         |                       |   to cause the program to stop running        |
# |         |                       |   entirely.                                   |
# -----------------------------------------------------------------------------------

# import logging

# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Some debugging details.')
# logging.info('The logging module is working.')
# logging.warning('An error message is about to be logged.')
# logging.error('An error has occurred.')
# logging.critical('The program is unable to recover!')

####################################################

# Disabling Logging

# import logging
# logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

# logging.critical('Critical error! Critical error!')
# logging.disable(logging.CRITICAL)
# logging.critical('Critical error!')
# logging.error('Error! Error!')

####################################################

# Logging to a File

# import logging
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# logging.debug('Start of Program')

# def factorial(n):
#     logging.debug('Start of factorial(%s%%)' % (n))
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(%s%%)' % (n))
#     return total

# print(factorial(5))
# logging.debug('End of Program')

#####################################################

# For debugging purposes

# print('Enter the first number to add: ')
# first = input()
# print('Enter the second number to add: ')
# second = input()
# print('Enter the third number to add: ')
# third = input()
# print('The sum is ' + first + second + third)

#####################################################

# Breakpoints

# import random
# heads = 0

# for i in range(1, 1001):
#     if random.randint(0, 1) == 1:
#         heads = heads + 1
#     if i == 500:
#         print('Halfway done!')

# print('Heads came up ' + str(heads) + ' times')

