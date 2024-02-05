# Import the Pillow library
# from PythonTerminalSprites import *
from PIL import Image, ImageChops
import os
import re
from AnsiiEscapeColors import *
# from numpy import  array, reshape, asarray, ndarray
import numpy as np

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
pixel_to_ansicode = {}
class pixelImage:
    @staticmethod
    def trim_image(img):
    # Convert the image to RGB if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Create a background image of the same color as the corner pixel
        bg = Image.new('RGB', img.size, img.getpixel((0,0)))

        # Find the difference between the input image and the background image
        diff = ImageChops.difference(img, bg)

        # The difference is zero for all pixels that match the background color,
        # so we need to find the bounding box of the non-zero regions
        bbox = diff.getbbox()

        # If the bounding box is not None, crop the image to that bounding box
        if bbox:
            img = img.crop(bbox)

        return img
    def __init__(self, img : list , scaleRatio = False):
        imageList = []
        self.ImageAnscii = []
        for image in img:
            imageList.append(self.trim_image(Image.open(image)))
            # imageList.append(Image.open(image))
        for rgb in imageList:
            self.ImageAnscii.append(self.getPixelToAnscii(rgb, scaleRatio))

    def getAnsciiList(self):
        return self.ImageAnscii
    def size(self, image):
        width, height = image.size
        return width, height
    def rgb_to_anscii(self, r, g, b):
        def distance(c1, c2):
            return sum((x1-x2)**2 for x1,x2 in zip(c1, c2))
        rgb_color = (r, g, b)
        # Find the index of the closest color in the ansi_colors list
        closest_color = min(range(len(ansi_colors)), key=lambda index: distance(rgb_color, ansi_colors[index]))
        # Return the ANSI color code
        pixel_to_ansicode[rgb_color] = "\033[48;5;{}m".format(closest_color)
        return "\033[48;5;{}m".format(closest_color)
    def getPixelToAnscii(self, image, scaleRatio = False):
        # Convert the image to RGB if it's not already
        if image.mode != 'RGB':
            image = image.convert('RGB')
        sizes = self.size(image)
        ansi_codes = []
        for x in range(sizes[1]):
            row = []
            for y in range(sizes[0]):
                r, g, b = image.getpixel((y, x))
                if (r,g,b) in pixel_to_ansicode:
                    row.append(pixel_to_ansicode[(r,g,b)] + ' ')
                    if scaleRatio:
                        row.append(pixel_to_ansicode[(r,g,b)] + ' ')
                else:
                    row.append(self.rgb_to_anscii(*(r,g,b)) + ' ')
                    if scaleRatio:
                        row.append(self.rgb_to_anscii(*(r,g,b)) + ' ')
            ansi_codes.append(row)
        # ansi_codes = list(map(lambda pixel: (self.rgb_to_anscii(*pixel) + ' ') *(2 if scaleRatio else 1), pixels))
        # Convert the list of ANSI codes to a 2D numpy array and return it
        return ansi_codes
        # return [ansi_codes[i*width:(i+1)*width] for i in range(height)]
        # return np.array(ansi_codes).reshape(img.size[1], img.size[0])
    def printOutImage(self, imageAnscii : list):
        # drawing = self.colors.tolist()  
        print('\033[0m\n'.join(''.join(row) for row in imageAnscii), end=reset)
    def printOutNumpy(self, imageAnscii : list):
        print(np.array(imageAnscii))
    def getPixelArray(self, imageAtSpot):
        return self.ImageAnscii[imageAtSpot]

# Convert the 2D array to a string



# Check if the operating system is Windows
is_windows = os.name == 'nt'
dir_sep = '\\' if is_windows else '/'

#declare all the images
humanList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human1.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human2.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human3.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human4.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human5.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human6.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human7.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human8.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human9.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human10.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human11.png']
bulletList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Bullet1.png',
f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Bullet2.png']
heartList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Heart.png']
healthList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Health1.png',
              f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Health2.png',
              f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Health3.png',]
BackgroundList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Background.png']

Human  = pixelImage(humanList, True)
Bullet = pixelImage(bulletList, True)
Heart  = pixelImage(heartList,True)
Health = pixelImage(healthList,True)
Background = pixelImage(BackgroundList,False)

# SurlColors     = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Surl.png'), True)
# SlugThing      = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}SlugThing1.png'), True)
# HumanIdle      = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human1.png'))
# HumanWalkRight = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human2.png'))
# HumanWalkLeft  = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human3.png'))
# HumanDown      = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human4.png'))
# HumanJump      = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human5.png'))
# HumanRightAttack = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human6.png'))
# HumanLeftAttack = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human7.png'))
# HumanForceFieldStage1 = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human8.png'))
# HumanForceFieldStage2 = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human9.png'))
# HumanForceFieldStage3 = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human10.png'))
# HumanForceFieldStage4 = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human11.png'))
# bulletRight = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Bullet1.png'))
# bulletLeft = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Bullet2.png'))

# ZarnDog        = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ZarnDog.png'), True)



# convertedSurlColors     = SurlColors.getPixelArray()
# convertedSlugThing      = SlugThing.getPixelArray()
# convertedHumanIdle      = HumanIdle.getPixelArray()
# convertedHumanWalkRight = HumanWalkRight.getPixelArray()
# convertedHumanWalkLeft  = HumanWalkLeft.getPixelArray()
# convertedHumanDown      = HumanDown.getPixelArray()
# convertedHumanJump      = HumanJump.getPixelArray()
# convertedHumanRightAttack = HumanRightAttack.getPixelArray()
# convertedHumanLeftAttack = HumanLeftAttack.getPixelArray()
# convertedHumanForceFieldStage1 = HumanForceFieldStage1.getPixelArray()
# convertedHumanForceFieldStage2 = HumanForceFieldStage2.getPixelArray()
# convertedHumanForceFieldStage3 = HumanForceFieldStage3.getPixelArray()
# convertedHumanForceFieldStage4 = HumanForceFieldStage4.getPixelArray()

# convertedBulletRight = bulletRight.getPixelArray()
# convertedBulletLeft = bulletLeft.getPixelArray()

# convertedZarnDog        = ZarnDog.getPixelArray()


# HumanIdle.printOutImage()
    


# def rgb_to_anscii(r, g, b):
#         def distance(c1, c2):
#             return sum((x1-x2)**2 for x1,x2 in zip(c1, c2))
#         rgb_color = (r, g, b)

#         # Find the index of the closest color in the ansi_colors list
#         closest_color = min(range(len(ansi_colors)), key=lambda index: distance(rgb_color, ansi_colors[index]))

#         # Return the ANSI color code
#         return "\033[48;5;{}m".format(closest_color)
# #Gets the rgb values of each pixel in the image
# def getPixelInImage(img : Image):
#     img = img.convert('RGBA')
#     colors = []
#     width, height = img.size
#     for y in range(height):
#   # Create an empty row to store the colors of the current row
#         row = []
#         for x in range(width):
#             # Get the color of the pixel at (x, y) as an RGB tuple
#             r, g, b, a = img.getpixel((x, y))
#             # Append the color to the row
#             row.append((r, g, b))
#             if (r, g, b) not in ansi_colors:
#                 ansi_colors.append((r, g, b))
#         # Append the row to the colors array
#         colors.append(row)
#     return colors
# #gets ansi color code from rgb values
# # def rgb_to_ansi(r, g, b):
# #     min_distance = float('inf')
# #     closest_colors = []    
# #     for i, (r2, g2, b2) in enumerate(ansi_colors):
# #         distance = (r - r2)**2 + (g - g2)**2 + (b - b2)**2
# #         if distance < min_distance:
# #             min_distance = distance
# #             closest_colors = [i]
# #         elif distance == min_distance:
# #             closest_colors.append(i)  
# #     # i = rgb_to_anscii(r,g,b)  # Convert the indices to ANSI escape codes
# #     return [("\033[48;5;{}m".format(i)) for i in closest_colors]
# #Converts rgb values to ascii color codes

# def convertPixeltoArray(colors, scaleRatio = False):
#     if scaleRatio:
#         scaled = " "
#     else:
#         scaled = ""
#     new_drawing = []
#     for row in colors:
#         rows = []
#         for color in row:
#             # color_name = rgb_to_ansi(*color)
#             color_name = rgb_to_anscii(*color)
#             # if color_name is None:
              
#             #     # print(color_name[1], color_name[0], end="\033[0m")
#             #     rows.append(color_name + " " + scaled + reset)
#             # else:
#                 # print(color_name[1], color_name[0], end="\033[0m")
          
#             rows.append(color_name+ " " + scaled)
#             # if scaleRatio:
#             #     rows.append(color_name[0] + " " + reset)
#             # print()
#         new_drawing.append(rows)
#     return new_drawing

# def printOutImage(drawing ):
#     print('\033[0m\n'.join(''.join(row) for row in drawing), end=reset)



#heart = Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}TestSprite.png')
# heartColors = pixelImage(heart, True)
# heartSize = heartColors.size()
# heartColors.printOutImage()
# print('')
# # heartColors.printOutNumpy()

# surl = Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}surl.png')
# surlColors = pixelImage(surl, False)
# print(surlColors.size())
# surlColors.printOutImage()
# print('')
# # surlColors.printOutNumpy()

# surlColors = getPixelInImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}surl1.png'))
# convertedSurl = convertPixeltoArray(surlColors, False)
# printOutImage(convertedSurl)
# # print(np.array(convertedSurl))
# print('')

# dog = pixelImage(Image.open(f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ZarnDog.png'), True).printOutImage()

# convertedHumanIdle = convertPixeltoArray(HumanIdle, True)
# convertedHumanWalkRight = convertPixeltoArray(HumanWalkRight, True)
# convertedHumanWalkLeft = convertPixeltoArray(HumanWalkLeft, True)
# convertedHumanJump = convertPixeltoArray(HumanJump, True)
# convertedHumanDown = convertPixeltoArray(HumanDown, True)
#  Print the heart to the terminal
#  printOutImage(convertedHeart)
#  printOutImage(convertedSurl)
#  printOutImage(convertedSlugThing)

