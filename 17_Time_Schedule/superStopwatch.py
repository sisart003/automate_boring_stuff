#! python3
# A simple stopwatch program.

# 1. Track the amount of time elapsed between presses of the enter key, with each key press starting a new “lap” on the timer.
# 2. Print the lap number, total time, and lap time.

# This means your code will need to do the following:

# 1. Find the current time by calling time.time() and store it as a timestamp at the start of the program, as well as at the start of each lap.
# 2. Keep a lap counter and increment it every time the user presses enter.
# 3. Calculate the elapsed time by subtracting timestamps.
# 4. Handle the KeyboardInterrupt exception so the user can press ctrl-C to quit

import time

# Display the program's instructions.
print('Press Enter to begin. After ward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')


# Ideas for Similar Programs
# Time tracking opens up several possibilities for your programs. Although
# you can download apps to do some of these things, the benefit of writing
# programs yourself is that they will be free and not bloated with ads and useless features. You could write similar programs to do the following:
# •	 Create a simple timesheet app that records when you type a person’s name and uses the current time to clock them in or out.
# •	 Add a feature to your program to display the elapsed time since a process started, such as a download that uses the requests module. (See Chapter 12.)
# •	 Intermittently check how long a program has been running and offer the user a chance to cancel tasks that are taking too long.