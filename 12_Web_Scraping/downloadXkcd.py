# Here’s what your program does:
# 1. Loads the XKCD home page
# 2. Saves the comic image on that page
# 3. Follows the Previous Comic link
# 4. Repeats until it reaches the first comic

# This means your code will need to do the following:

# 1. Download pages with the requests module.
# 2. Find the URL of the comic image for a page using Beautiful Soup.
# 3. Download and save the comic image to the hard drive with iter_content().
# 4. Find the URL of the Previous Comic link, and repeat

#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'            # starting url
os.makedirs('xkcd', exist_ok=True)  # stor comics in ./xkcd
while not url.endswith('#'):
    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.beautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    # Save the image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

    for chunk in res.iter_content(1000000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev Button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done')

# Ideas for Similar Programs
# Downloading pages and following links are the basis of many web crawling
# programs. Similar programs could also do the following:
# •	 Back up an entire site by following all of its links.
# •	 Copy all the messages off a web forum.
# •	 Duplicate the catalog of items for sale on an online store.