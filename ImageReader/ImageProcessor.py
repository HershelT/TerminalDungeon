# Import the Pillow library
# from PythonTerminalSprites import *
from PIL import Image
import re
reset = "\033[0m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
bright_black = "\033[90m"
bright_red = "\033[91m"
bright_green = "\033[92m"
bright_yellow = "\033[93m"
bright_blue = "\033[94m"
bright_magenta = "\033[95m"
bright_cyan = "\033[96m"
bright_white = "\033[97m"
background_red = "\033[41m"
background_green = "\033[42m"
background_yellow = "\033[43m"
background_blue = "\033[44m"
background_magenta = "\033[45m"
background_cyan = "\033[46m"
background_white = "\033[47m"
background_bright_black = "\033[100m"
background_bright_red = "\033[101m"
background_bright_green = "\033[102m"
background_bright_yellow = "\033[103m"
background_bright_blue = "\033[104m"
background_bright_magenta = "\033[105m"
background_bright_cyan = "\033[106m"
background_bright_white = "\033[107m"
background_black = "\033[40m"
# background_light_blue = "\033[38;5;117m"
background_purple = "\033[48;5;54m"  # ANSI code for light purple background


ansi_escape = re.compile(r'\033\[\d+m')
# asncii color codes and rgb values
ansi_to_rgb = {
    (0, 0, 0): ["black", background_black, "\033[30m"],
    (205, 0, 0): ["red", background_red, "\033[31m"],
    (0, 205, 0): ["green", background_green, "\033[32m"],
    (205, 205, 0): ["yellow", background_yellow, "\033[33m"],
    (0, 0, 238): ["blue", background_blue, "\033[34m"],
    (205, 0, 205): ["magenta", background_magenta, "\033[35m"],
    (0, 205, 205): ["cyan", background_cyan, "\033[36m"],
    (229, 229, 229): ["white", background_white, "\033[37m"],
    (127, 127, 127): ["bright_black", background_bright_black, "\033[90m"],
    (255, 0, 0): ["bright_red", background_bright_red, "\033[91m"],
    (0, 255, 0): ["bright_green", background_bright_green, "\033[92m"],
    (255, 255, 0): ["bright_yellow", background_bright_yellow, "\033[93m"],
    (92, 92, 255): ["bright_blue", background_bright_blue, "\033[94m"],
    (255, 0, 255): ["bright_magenta", background_bright_magenta, "\033[95m"],
    (0, 255, 255): ["bright_cyan", background_bright_cyan, "\033[96m"],
    (255, 255, 255): ["bright_white", background_bright_white, "\033[97m"],
    # (48, 5, 117): ["light_blue", background_light_blue, "\033[38;5;117m"],
    (48, 5, 117): ["purple", background_purple, "\033[48;5;54m"],

}

def generate_ansi_colors():
    basic_colors = [(0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0),
                    (0, 0, 128), (128, 0, 128), (0, 128, 128), (192, 192, 192),
                    (128, 128, 128), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                    (0, 0, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255)]

    levels = [0, 95, 135, 175, 215, 255]
    extended_colors = [(r, g, b) for r in levels for g in levels for b in levels]

    return basic_colors + extended_colors
ansi_colors = generate_ansi_colors()
# print(ansi_colors)
def rgb_to_ansi(r, g, b):
    min_distance = float('inf')
    closest_colors = []

    for i, (r2, g2, b2) in enumerate(ansi_colors):
        distance = (r - r2)**2 + (g - g2)**2 + (b - b2)**2
        if distance < min_distance:
            min_distance = distance
            closest_colors = [i]
        elif distance == min_distance:
            closest_colors.append(i)

    # Convert the indices to ANSI escape codes
    return [("\033[48;5;{}m".format(i)) for i in closest_colors]
# Open the .gpl file
# Open the .gpl file
# with open("ansi_colors.gpl", "w") as file:
#     # Write the header
#     file.write("GIMP Palette\n")
#     file.write("Name: ANSI Colors\n")
#     file.write("Columns: 4\n")
#     file.write("#\n")
#     # Write the colors
#     for rgb in ansi_colors:
#         file.write(f"{rgb[0]} {rgb[1]} {rgb[2]} Color\n")
# Loop through each pixel in the image to get the rgb value
def getPixelInImage(img : Image):
    img = img.convert('RGBA')
    colors = []
    width, height = img.size
    for y in range(height):
  # Create an empty row to store the colors of the current row
        row = []
        for x in range(width):
            # Get the color of the pixel at (x, y) as an RGB tuple
            r, g, b, a = img.getpixel((x, y))
            # Append the color to the row
            row.append((r, g, b))
            if (r, g, b) not in ansi_colors:
                ansi_colors.append((r, g, b))
        # Append the row to the colors array
        colors.append(row)
    return colors

#Converts rgb values to ascii color codes
def convertPixeltoArray(colors, scaleRatio = False):
    new_drawing = []
    for row in colors:
        rows = []
        for color in row:
            # color_name = rgb_to_ansi(*color)
            color_name = rgb_to_ansi(*color)
            # if color_name is None:
                
            #     # print(color_name[1], color_name[0], end="\033[0m")
            #     rows.append(color_name + " " + scaled + reset)
            # else:
                # print(color_name[1], color_name[0], end="\033[0m")
            
            rows.append(color_name[0]+ " ")
            if scaleRatio:
                rows.append(color_name[0] + " " + reset)
            # print()
        new_drawing.append(rows)
    return new_drawing

def printOutImage(drawing : list):
    print('\033[0m\n'.join(''.join(row) for row in drawing))
# Convert the 2D array to a string

#heart 
heart = Image.open('ImageReader\\PythonTerminalSprites\\TestSprite.png')
heartColors = getPixelInImage(heart)
convertedHeart = convertPixeltoArray(heartColors, True)

surlColors = getPixelInImage(Image.open('ImageReader\\PythonTerminalSprites\\Surl.png'))
convertedSurl = convertPixeltoArray(surlColors, True)

SlugThing = getPixelInImage(Image.open('ImageReader\\PythonTerminalSprites\\SlugThing1.png'))
convertedSlugThing = convertPixeltoArray(SlugThing, True)

HumanIdle = getPixelInImage(Image.open('ImageReader\\PythonTerminalSprites\\Human1.png'))
HumanWalkRight = getPixelInImage(Image.open('ImageReader\\PythonTerminalSprites\\Human2.png'))
HumanWalkLeft = getPixelInImage(Image.open('ImageReader\\PythonTerminalSprites\\Human3.png'))
HumanDown = getPixelInImage(Image.open('ImageReader\\PythonTerminalSprites\\Human4.png'))
HumanJump = getPixelInImage(Image.open('ImageReader\\PythonTerminalSprites\\Human5.png'))
convertedHumanIdle = convertPixeltoArray(HumanIdle, True)
convertedHumanWalkRight = convertPixeltoArray(HumanWalkRight, True)
convertedHumanWalkLeft = convertPixeltoArray(HumanWalkLeft, True)
convertedHumanJump = convertPixeltoArray(HumanJump, True)
convertedHumanDown = convertPixeltoArray(HumanDown, True)

# Print the heart to the terminal
# printOutImage(convertedHeart)
# printOutImage(convertedSurl)
# printOutImage(convertedSlugThing)

