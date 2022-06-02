#! python3
# A simple countdown script

# 1. Count down from 60.
# 2. Play a sound file (alarm.wav) when the countdown reaches zero.

# This means your code will need to do the following:

# 1. Pause for 1 second in between displaying each number in the countdown by calling time.sleep().
# 2. Call subprocess.Popen() to open the sound file with the default application.

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file
subprocess.Popen(['start', 'icant.mp3'], shell=True)

