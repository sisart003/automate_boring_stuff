#! python3
# Resizes all iamges in current working directory to fit in a 300x300 square, and adds catlogo.png to the lower-right corner.

# 1. Load the logo image.
# 2. Loop over all .png and.jpg files in the working directory.
# 3. Check whether the image is wider or taller than 300 pixels.
# 4. If so, reduce the width or height (whichever is larger) to 300 pixels and scale down the other dimension proportionally.
# 5. Paste the logo image into the corner.
# 6. Save the altered images to another folder.

# This means the code will need to do the following:

# 1. Open the catlogo.png file as an Image object.
# 2. Loop over the strings returned from os.listdir('.').
# 3. Get the width and height of the image from the size attribute.
# 4. Calculate the new width and height of the resized image.
# 5. Call the resize() method to resize the image.
# 6. Call the paste() method to paste the logo.
# 7. Call the save() method to save the changes, using the original filename.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'momoring.jpg'

logoIm = Image.open(LOGO_FILENAME).convert("RGBA")
logoWidth, logoHeight = logoIm.size

os.makedirs('widthLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue # Skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('widthLogo', filename))



# Ideas for Similar Programs
# Being able to composite images or modify image sizes in a batch can be useful
# in many applications. You could write similar programs to do the following:
# •	 Add text or a website URL to images.
# •	 Add timestamps to images.
# •	 Copy or move images into different folders based on their sizes.
# •	 Add a mostly transparent watermark to an image to prevent others from copying it.