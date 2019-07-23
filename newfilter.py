# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    image = Image.open('C:\\Users\\Ash\\Documents\\'+ filename)
    return image

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(filename):
    filename.show(title=None)

def save_img(filename):
    filename.save(filename)


darkBlue = (49, 28, 118)
red = (112, 28, 118)
lightBlue = (25, 149, 129)
yellow = (202, 203, 148)

def colorchange(intensity):
    if intensity < 182:
        return darkBlue
    elif intensity < 364:
        return red
    elif intensity < 564:
        return lightBlue
    else:
        return yellow

def obamicon(filename1):
    filename = load_img(filename1)
    out = Image.new('RGB', filename.size, (0,0,0))
    width, height = filename.size
    for x in range(width):
        for y in range(height):
            r,g,b = filename.getpixel((x,y))
            inten = r+g+b
            newColor = colorchange(inten)
            out.putpixel((x,y), newColor)
    show_img(out)
