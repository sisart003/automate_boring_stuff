# while True:
#     print('Enter your age: ')
#     age = input()
#     try:
#         age = int(age)
#     except:
#         print('Please use numeric digits.')
#         continue
#     if age < 1:
#         print('Please enter a positive number.')
#         continue
#     break

# print(f'You age is {age}')

import pyinputplus as pyip

# response = pyip.inputNum()
# print('ok ' + str(response))

# response = pyip.inputInt(prompt='Enter a Number: ')

# print(help(pyip.inputChoice))

############################

# The min, max, greaterThan, and lessThan Keyword Arguments

# response = pyip.inputNum('Enter num: ', min=4)
# response = pyip.inputNum('Enter num: ', greaterThan=4)
# response = pyip.inputNum('Enter num: ', lessThan=4)
# response = pyip.inputNum('Enter num: ', max=4)

############################

# The blank Keyword Argument
# response = pyip.inputNum(blank=True)

############################

# The limit, timeout, and default Keyword Arguments

# response = pyip.inputNum(limit=2)
# response = pyip.inputNum(timeout=10)
# response = pyip.inputNum(limit=2, default='N/A')

#############################

# The allowRegexes and blockRegexes Keyword Arguments

# response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

# response = pyip.inputNum(blockRegexes=[r'[02468]$'])

# response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])

# Passing a Custom Validation Function to inputCustom()

# def addsUpToTen(numbers):
   # numbersList = list(numbers)
   # for i, digit in enumerate(numbersList):
       # numbersList[i] = int(digit)

   # if sum(numbersList) != 10:
       # raise Exception('The Digits must add up to 10, not %s.' %(sum(numbersList)))
  #  return int(numbers) # Return an int form of numbers.


# response = pyip.inputcustom(addsUpToTen) # No parenthese after addsUpToTen here.


