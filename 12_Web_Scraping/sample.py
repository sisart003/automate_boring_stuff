import webbrowser, requests, bs4
# webbrowser.open('https://inventwithpython.com/')

# Downloading a Web Page with the requests.get() Function
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
# print(res.status_code == requests.codes.ok)
# print(len(res.text))
# print(res.text[:250])

#########################################################

# Checking for Errors

# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

#########################################################

# Saving Downloaded Files to the Hard Drive

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# playFile = open('RomeoAndJuliet.txt', 'wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()

#########################################################

# Creating a BeautifulSoup Object from HTML

# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.beautifulSoup(res.text, 'html.parser')
# type(noStarchSoup)
# exampleFile = open('example.html')
# exampleSoup = bs4.beautifulSoup(exampleFile, 'html.parser')
# type(exampleSoup)

#########################################################

#Finding an Element with the select() Method

# Table 12-2: Examples of CSS Selectors
# Selector passed to the select() method   |    Will match . . .
# -----------------------------------------|------------------------------------
# soup.select('div')                       |    All elements named <div>
# soup.select('#author')                   |    The element with an id attribute of author
# soup.select('.notice')                   |    All elements that use a CSS class attribute named notice
# soup.select('div span')                  |    All elements named <span> that are within an element named <div>
# soup.select('div > span')                |    All elements named <span> that are directly within an element named <div>, with no other element in between
# soup.select('input[name]')               |    All elements named <input> that have a name attribute with any value
# soup.select('input[type="button"]')      |    All elements named <input> that have an attribute named type with value button

# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# elems = exampleSoup.select('#author')
# print(type(elems)) # elems is a list of Tag objects
# print(len(elems))
# print(elems[0])
# print(str(elems[0])) # The Tag object as a string
# print(elems[0].getText())
# print(elems[0].attrs)
# pElems = exampleSoup.select('p')
# print(str(pElems[0]))
# print(pElems[0].getText())
# print(str(pElems[1]))
# print(pElems[1].getText())
# print(str(pElems[2]))
# print(pElems[2].getText())

#########################################################

# Getting Data from an Element's Attributes

# soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
# spanElem = soup.select('span')[0]
# print(str(spanElem))
# print(spanElem.get('id'))
# print(spanElem.get('some_noneexistent_addr') == None)
# print(spanElem.attrs)

#########################################################

# Starting a selenium-Controlled Browser

# from selenium import webdriver
# browser = webdriver.Firefox()
# print(type(browser))
# browser.get('https://inventwithpython.com')

#########################################################

# Finding Elements on the Page

# Method name WebElement object/list returned
# browser.find_element_by_class_name(name)              Elements that use the CSS class name
# browser.find_elements_by_class_name(name)

# browser.find_element_by_css_selector(selector)        Elements that match the CSS selector
# browser.find_elements_by_css_selector(selector)

# browser.find_element_by_id(id)                        Elements with a matching id attribute value
# browser.find_elements_by_id(id)

# browser.find_element_by_link_text(text)               <a> elements that completely match the text provided
# browser.find_elements_by_link_text(text)
# 
# browser.find_element_by_partial_link_text(text)       <a> elements that contain the text provided
# browser.find_elements_by_partial_link_text(text)
# 
# browser.find_element_by_name(name)                     Elements with a matching name attribute value
# browser.find_elements_by_name(name)
# 
# browser.find_element_by_tag_name(name)                 Elements with a matching tag name (case-insensitive; an <a> element is matched by 'a' and 'A')
# browser.find_elements_by_tag_name(name)              

#########################################################

# Attribute or method                                   Description
# tag_name                                              The tag name, such as 'a' for an <a> element
# get_attribute(name)                                   The value for the element’s name attribute
# text                                                  The text within the element, such as 'hello' in <span>hello</span>
# clear()                                               For text field or text area elements, clears the text typed into it
# is_displayed()                                        Returns True if the element is visible; otherwise returns False
# is_enabled()                                          For input elements, returns True if the element is enabled; otherwise returns False
# is_selected()                                         For checkbox or radio button elements, returns True if the element is selected; otherwise returns False
# location                                              A dictionary with keys 'x' and 'y' for the position of the element in the page

#########################################################

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://inventwithpython.com')

# try:
#     elem = browser.find_element_by_class_name(' cover-thumb')
#     print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')

#########################################################

# Clicking the Page

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://inventwithpython.com')
# linkElem = browser.find_element_by_link_text('Read Online for Free')
# print(linkElem) # follows the "Read Online for Free" link

#########################################################

# Filling Out and Submitting Forms

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://login.metafilter.com')
# userElem = browser.find_element_by_id('user_name')
# userElem.send_keys('your_real_username_here')

# passwordElem = browser.find_element_by_id('user_pass')
# passwordElem.send_keys('Your_real_password_here')
# passwordElem.submit()

#########################################################

# Sending Special Keys

# Attributes                                        Meanings
# Keys.DOWN, Keys.UP, Keys.LEFT,                    The keyboard arrow keys
# Keys.RIGHT

# Keys.ENTER, Keys.RETURN                           The enter and return keys
# Keys.HOME, Keys.END, Keys.PAGE_DOWN,              The home, end, pagedown, and pageup keys
# Keys.PAGE_UP

# Keys.ESCAPE, Keys.BACK_SPACE,                     The esc, backspace, and delete keys
# Keys.DELETE

# Keys.F1, Keys.F2, . . . ,                         Keys.F12 The F1 to F12 keys at the top of the keyboard
# Keys.TAB                                          The tab key

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# browser = webdriver.Firefox()
# browser.get('https://nostartch.com')
# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END)    # scrolls to bottom
# htmlElem.send_keys(Keys.HOME)   # scrolls to top

#########################################################

# Clicking Browser Buttons

# browser.back()          Clicks the Back button.
# browser.forward()       Clicks the Forward button.
# browser.refresh()       Clicks the Refresh/Reload button.
# browser.quit()          Clicks the Close Window button.