import time, datetime, subprocess, threading

# The time.time() Function

# print(time.time())

# def calcProd():
#     # Calculate the product of the first 100,000 numbers.
#     product = 1
#     for i in range(1, 100000):
#         product = product * i
#     return product

# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The Result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))

# print(time.ctime())
# thisMoment = time.time()
# print(time.ctime(thisMoment))

#################################################################################

# The time.sleep() Function

# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)

#################################################################################

# Rounding Numbers

# now = time.time()
# print(round(now, 2))

#################################################################################

# The datetime Module

# etad = datetime.datetime.now()
# print(etad)
# dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
# print(dt.year, dt.month, dt.day)
# print(dt.hour, dt.minute, dt.second)

# print(datetime.datetime.fromtimestamp(1000000))
# print(datetime.datetime.fromtimestamp(time.time()))

# halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
# oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)

# print(halloween2019 == oct31_2019)
# print(halloween2019 > newyears2020)
# print(newyears2020 > halloween2019)
# print(newyears2020 != oct31_2019)

#################################################################################

# The timedelta Data Type

# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(str(delta))

# dt = datetime.datetime.now()
# print(dt)
# thousandDays = datetime.timedelta(days=1000)
# print(dt + thousandDays)

# oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
# aboutThirtyYears = datetime.timedelta(days=365 * 30)
# print(oct21st)
# print(oct21st - aboutThirtyYears)
# print(oct21st - (2 * aboutThirtyYears))

#################################################################################

# Pausing Until a Specific Date

# halloween2016 = datetime.datetime(2016, 10, 21, 0, 0, 0)
# while datetime.datetime.now() < halloween2016:
#     time.sleep(1)

#################################################################################

# Converting datetime Objects into Strings

# strftime() directive          Meaning
# %Y                            Year with century, as in '2014'
# %y                            Year without century, '00' to '99' (1970 to 2069)
# %m                            Month as a decimal number, '01' to '12'
# %B                            Full month name, as in 'November'
# %b                            Abbreviated month name, as in 'Nov'
# %d                            Day of the month, '01' to '31'
# %j                            Day of the year, '001' to '366'
# %w                            Day of the week, '0' (Sunday) to '6' (Saturday)
# %A                            Full weekday name, as in 'Monday'
# %a                            Abbreviated weekday name, as in 'Mon'
# %H                            Hour (24-hour clock), '00' to '23'
# %I                            Hour (12-hour clock), '01' to '12'
# %M                            Minute, '00' to '59'
# %S                            Second, '00' to '59'
# %p                            'AM' or 'PM'
# # %%                          Literal '%' character

# oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
# print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
# print(oct21st.strftime('%I:%M %p'))
# print(oct21st.strftime("%B of '%y"))

#################################################################################

# Converting String into datetime Objects

# print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
# print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# print(datetime.datetime.strptime("October of '19", "%B of '%y"))
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))

#################################################################################

# Multithreading

# startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < startTime:
#     time.sleep(1)

# print('Program now starting on Halloween 2029')
###
# import threading
# print('Start of Program')

# def takeANap():
#     time.sleep(5)
#     print('Wake up!')

# threadObj = threading.Thread(target=takeANap)
# threadObj.start()

# print('End of Program')

#################################################################################

# Passing Arguments to the Thread's Target Function

# print('Cats', 'Dogs', 'Frogs', sep=' & ')

# import threading
# threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep' : ' & '})
# print(threadObj.start())

#################################################################################


# subprocess.Popen('C:\\Windows\\System32\\calc.exe')

# paintProc = subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
# paintProc.poll() == None
# paintProc.wait() # Doesn't return until MS Paint closes.
# paintProc.poll()

#################################################################################

# Passing Command Line Arguments to the Popen() Function

# subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\Users\\tess\\hello.txt'])

#################################################################################

# Opening Files with Default Applications

# fileObj = open('hello.txt', 'w')
# fileObj.write('Hello, world!')
# fileObj.close()

# import subprocess.Popen(['start', 'hello.txt'], shell=True)