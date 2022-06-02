import os
from PIL import ImageColor
from PIL import Image, ImageDraw, ImageFont

# Colors and RGBA Values

# Name      RGBA value              Name        RGBA value
# White     (255, 255, 255, 255)    Red         (255, 0, 0, 255)
# Green     (0, 128, 0, 255)        Blue        (0, 0, 255, 255)
# Gray      (128, 128, 128, 255)    Yellow      (255, 255, 0, 255)
# Black     (0, 0, 0, 255)          Purple      (128, 0, 128, 255)

# print(ImageColor.getcolor('red', 'RGBA'))
# print(ImageColor.getcolor('RED', 'RGBA'))
# print(ImageColor.getcolor('Black', 'RGBA'))
# print(ImageColor.getcolor('chocolate', 'RGBA'))
# print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))

##########################################################################################

# Manipulating Images with Pillow

chaer = Image.open('chaer.jpg')
mina = Image.open('mina.jpg')
chaeryoung = Image.open('chaeryoung.jpg')

##########################################################################################

# Working with the Image Data Type

# print(chaer.size)
# width, height = chaer.size
# print(width)
# print(height)
# print(chaer.filename)
# print(chaer.format)
# print(chaer.format_description)
# chaer.save('chaer.png')

# im = Image.new('RGBA', (100, 200), 'purple')
# im.save('purple.png')
# im2 = Image.new('RGBA', (20, 20))
# im2.save('red.png')

##########################################################################################

# Cropping Images

# catIm = Image.open('chaer.jpg')
# croppedIm = catIm.crop((135, 145, 379, 560))
# croppedIm.save('cropped.png')

##########################################################################################

# Copying and Pasting Images onto Other Images

# catIm = Image.open('Chaer.jpg')
# catCopyIm = catIm.copy()
# faceIm = catIm.crop((135, 125, 259, 320))
# print(faceIm.size)
# catCopyIm.paste(faceIm, (0, 0))
# catCopyIm.paste(faceIm, (200, 400))
# catCopyIm.save('pasted.png')

# catImWidth, catImHeight = catIm.size
# faceImWidth, faceImHeight = faceIm.size
# catCopyTwo = catIm.copy()
# for left in range(0, catImWidth, faceImWidth):
#     for top in range(0, catImHeight, faceImHeight):
#         print(left, top)
#         catCopyTwo.paste(faceIm, (left, top))

# catCopyTwo.save('tiled.png')

##########################################################################################

# Resizing an Image

# catIm = Image.open('Mina.jpg')
# print(catIm.size)
# width, height = catIm.size # width and height
# quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
# print(quartersizedIm.size)
# quartersizedIm.save('quartersized.png')
# svelteIm = catIm.resize((width, height + 300))
# print(svelteIm.size)
# svelteIm.save('svelte.png')

##########################################################################################

# Rotating and Flipping Images

# catIm = Image.open('chaeryoung.jpg')
# catIm.rotate(90).save('rotated_images/rotated90.png')
# catIm.rotate(180).save('rotated_images/rotated180.png')
# catIm.rotate(270).save('rotated_images/rotated270.png')
# catIm.rotate(6).save('rotated_images/rotated6.png')
# catIm.rotate(6, expand=True).save('rotated_images/rotated6_expanded.png')
# catIm.transpose(Image.FLIP_LEFT_RIGHT).save('rotated_images/horizontal_flip.png')
# catIm.transpose(Image.FLIP_TOP_BOTTOM).save('rotated_images/vertical_flip.png')

##########################################################################################

# Changing Individual Pixels

# im = Image.new('RGBA', (100, 100))
# im.getpixel((0, 0))
# for x in range(100):
#     for y in range(50):
#         im.putpixel((x,y), (210, 210, 210))

# for x in range(100):
#     for y in range(50, 100):
#         im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

# print(im.getpixel((0, 0)))
# print(im.getpixel((0, 50)))
# im.save('putPixel.png')

##########################################################################################

# Drawing Example

# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)

# draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
# draw.rectangle((20, 30, 60, 60), fill='blue')
# draw.ellipse((120, 30, 160, 60), fill='red')
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
# for i in range(100, 200, 10):
#     draw.line([(i, 0), (200, i - 100)], fill='green')


# im.save('drawing.png')

##########################################################################################

# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# draw.text((20, 150), 'Hello', fill='purple')
# fontsFolder = 'font_bold' # e.g. '/Library/Fonts'
# arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'Poppins-Bold.ttf'))
# draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
# im.save('text.png')