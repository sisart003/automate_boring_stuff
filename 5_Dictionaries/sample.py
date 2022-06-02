# birthdays = {'Alice': 'Apr 1', 'Bob' : 'Dec 12', 'Carol' : 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated')

####################################################

# spam = {'color' : 'red', 'age' : 32}

# for v in spam.values():
#     print(v)

# for k in spam.keys():
#     print(k)

# for i in spam.items():
#     print(i)


####################################################


# Get method
# picnicItems = {'apples' : 5, 'cups' : 2}
# print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')


####################################################


# setdefault() Method
# spam = {'name' : 'Pooka', 'age' : 4}
# spam.setdefault('color', 'black')

# if 'color' not in spam:
#     spam['color'] = 'black'

# print(spam['color'])


####################################################


# import pprint

# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# pprint.pprint(count)


####################################################


# theBoard = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
#             'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ', 
#             'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}

# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# turn = 'X'

# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn

#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'

# printBoard(theBoard)


####################################################


allGuests = {'Alice' : {'apples' : 5, 'pretzels' : 12},
                'Bob' : {'ham sandwiches' : 3, 'apples' : 2},
                'Carol' : {'cups' : 3, 'apple pies' : 1}}

def totalBrought(guests, item):
    numBrought = 0

    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    
    return numBrought

print('Number of things being brought: ')
print(' - Apples          ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups            ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes           ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches  ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies      ' + str(totalBrought(allGuests, 'apple pies')))