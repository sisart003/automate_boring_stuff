# 1. Gets search keywords from the command line arguments
# 2. Retrieves the search results page
# 3. Opens a browser tab for each result

# This means your code will need to do the following:

# 1. Read the command line arguments from sys.argv.
# 2. Fetch the search result page with the requests module.
# 3. Find the links to each search result.
# 4. Call the webbrowser.open() function to open the web browser.

#! python3
# searchpypi.py - Opoens several search results.

import requests, sys, webbrowser, bs4

print('Searching...')   # display text while downloading the search result page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrive top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Opoen a browser tab for each result
linkElems = soup.select('.package-snippet')
numOpen = min(4, len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

# Ideas for Similar Programs
# The benefit of tabbed browsing is that you can easily open links in new tabs
# to peruse later. A program that automatically opens several links at once
# can be a nice shortcut to do the following:
# •	 Open all the product pages after searching a shopping site suchas Amazon.
# •	 Open all the links to reviews for a single product.
# •	 Open the result links to photos after performing a search on a photo site such as Flickr or Imgur.