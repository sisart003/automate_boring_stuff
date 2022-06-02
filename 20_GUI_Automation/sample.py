import pyautogui, time

# wh = pyautogui.size() # Obtain the screen resolution.
# print(wh)
# print(wh[0])
# print(wh.width)

###########################################################################################################

# Moving the mouse

# for i in range(10): # Move mouse in a square.
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# for i in range(10):
#     pyautogui.move(100, 0, duration=0.25)   # right
#     pyautogui.move(0, 100, duration=0.25)   # down
#     pyautogui.move(-100, 0, duration=0.25)  # left
#     pyautogui.move(0, -100, duration=0.25)  # up

###########################################################################################################

# Getting the Mouse Position

# print(pyautogui.position()) # Get current mouse position.
# print(pyautogui.position()) # Get current mouse position again.
# p = pyautogui.position() # And again
# print(p)
# print(p[0])
# print(p.x)

###########################################################################################################

# Clicking the Mouse

# pyautogui.click(100, 550)

###########################################################################################################

# Dragging the Mouse

# time.sleep(5)
# pyautogui.click()   # Click to make the window active.
# distance = 300
# change = 20

# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2)   # Move right
#     distance = distance - change
#     pyautogui.drag(0, distance, duration=0.2)   # Move down
#     pyautogui.drag(-distance, 0, duration=0.2)  # Move left
#     distance = distance - change
#     pyautogui.drag(0, -distance, duration=0.2)  # Move up

###########################################################################################################

# Scrolling the Mouse

# pyautogui.scroll(200)

###########################################################################################################

# Planning Your Mouse Movements

# pyautogui.mouseInfo()

###########################################################################################################

# Getting a Screenshot

# im = pyautogui.screenshot()

###########################################################################################################

# Analyzing the Screenshot

# print(pyautogui.pixel(0, 0))
# print(pyautogui.pixel(50, 200))
# print(pyautogui.pixel(100, 200))

# print(pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)))
# print(pyautogui.pixelMatchesColor(50, 200, (255, 135, 144)))

###########################################################################################################

# Image Recognition

# b = pyautogui.locateOnScreen('submit.PNG')

# print(b)
# print(b[0])
# print(b.left)
# print(list(pyautogui.locateAllOnScreen('submit.PNG')))
# pyautogui.click('submit.PNG')

# try:
#     location = pyautogui.locateOnScreen('submit.PNG')
# except:
#     print('Image could not be found.')

###########################################################################################################

# Obtaining the Active Window

# fw = pyautogui.getActiveWindow()
# print(fw)
# print(str(fw))
# print(fw.title)
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)
# print(fw.topleft)
# print(fw.area)
# pyautogui.click(fw.left + 10, fw.top + 20)

###########################################################################################################

# Other Ways of Obtaining Windows

# pyautogui.getAllWindows()             Returns a list of Window objects for every visible window on the screen.
# pyautogui.getWindowsAt(x, y)          Returns a list of Window objects for every visible window that includes the point (x, y).
# pyautogui.getWindowsWithTitle(title)  Returns a list of Window objects for every visible window that includes the string title in its title bar.
# pyautogui.getActiveWindow()           Returns the Window object for the window that is currently receiving keyboard focus.

###########################################################################################################

# Manipulating Windows

# fw = pyautogui.getActiveWindow()
# print(fw.width)             # Gets the current widfth of the window.
# print(fw.topleft)           # Gets the current position of the window.
# fw.width = 1000             # Resizes the width.
# fw.topleft = (800, 400)     # Move the window.

# fw.isMaximized  # Returns True if window is maximized.
# fw.isMinimized  # Returns True if window is minimized.
# fw.isActive     # Returns True if window is the active window.
# fw.maximize()   # Maximizes the window.
# fw.isMaximized
# fw.restore()    # Undoes a minimize/maximize action.
# fw.minimize()   # Minimizes the window.
# time.sleep(5); fw.activate() # Wait 5 seconds while you activate a different window
# fw.close()

###########################################################################################################

# Controlling the Keyboard

# pyautogui.click(400, 400)
# pyautogui.write('Hello, World!', 0.25)

###########################################################################################################

# Key Names

# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

# Keyboard key string                                                                   Meaning
# 'a', 'b', 'c', 'A', 'B', 'C', '1', '2', '3', '!', '@', '#', and so on                 The keys for single characters
# 'enter' (or 'return' or '\n')                                                         The enter key
# 'esc'                                                                                 The esc key
# 'shiftleft', 'shiftright'                                                             The left and right shift keys
# 'altleft', 'altright'                                                                 The left and right alt keys
# 'ctrlleft', 'ctrlright'                                                               The left and right ctrl keys
# 'tab' (or '\t')                                                                       The tab key
# 'backspace', 'delete'                                                                 The backspace and delete keys
# 'pageup', 'pagedown'                                                                  The page up and page down keys
# 'home', 'end'                                                                         The home and end keys
# 'up', 'down', 'left', 'right'                                                         The up, down, left, and right arrow keys
# 'f1', 'f2', 'f3', and so on                                                           The F1 to F12 keys
# 'volumemute', 'volumedown', 'volumeup'                                                The mute, volume down, and volume up keys (some keyboards do not have these keys, but your operating system will still be able to understand these simulated keypresses)
# 'pause'                                                                               The pause key
# 'capslock', 'numlock', 'scrolllock'                                                   The caps lock, num lock, and scroll lock keys
# 'insert'                                                                              The ins or insert key
# 'printscreen'                                                                         The prtsc or print screen key
# 'winleft', 'winright'                                                                 The left and right win keys (on Windows)
# 'command'                                                                             The Command () key (on macOS)
# 'option'                                                                              The option key (on macOS)

###########################################################################################################

# Pressing and Releasing the Keyboard

# pyautogui.keyDown('shift')
# pyautogui.press('4')
# pyautogui.keyUp('shift')

###########################################################################################################

# Hotkey Combinations

# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('c')
# pyautogui.keyUp('c')
# pyautogui.keyUp('ctrl')

# pyautogui.hoykey('ctrl', 'c')

###########################################################################################################

# Setting Up Your GUI Automation Scripts

# pyautogui.sleep(3)  # Pauses the program for 3 seconds.
# pyautogui.countdown(10) # Counts down over 10 seconds.
# print('Starting in ', end=''); pyautogui.countdown(3)

###########################################################################################################

# Review of the PyAutoGUI Functions

# moveTo(x, y)                                  Moves the mouse cursor to the given x and y coordinates.
# move(xOffset, yOffset)                        Moves the mouse cursor relative to its current position.
# dragTo(x, y)                                  Moves the mouse cursor while the left button is held down.
# drag(xOffset, yOffset)                        Moves the mouse cursor relative to its current position while the left button is held down.
# click(x, y, button)                           Simulates a click (left button by default).
# rightClick()                                  Simulates a right-button click.
# middleClick()                                 Simulates a middle-button click.
# doubleClick()                                 Simulates a double left-button click.
# mouseDown(x, y, button)                       Simulates pressing down the given button at the position x, y.
# mouseUp(x, y, button)                         Simulates releasing the given button at the position x, y.
# scroll(units)                                 Simulates the scroll wheel. A positive argument scrolls up; a negative argument scrolls down.
# write(message)                                Types the characters in the given message string.
# write([key1, key2, key3])                     Types the given keyboard key strings.
# press(key)                                    Presses the given keyboard key string.
# keyDown(key)                                  Simulates pressing down the given keyboard key.
# keyUp(key)                                    Simulates releasing the given keyboard key.
# hotkey([key1, key2, key3])                    Simulates pressing the given keyboard key strings down in order and then releasing them in reverse order.
# screenshot()                                  Returns a screenshot as an Image object.
# getActiveWindow(), getAllWindows(),           These functions return Window objects that can resize and reposition application windows on the desktop.
# getWindowsAt(), and getWindowsWithTitle()
# getAllTitles()                                Returns a list of strings of the title bar text of every window on the desktop.

