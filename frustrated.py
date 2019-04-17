#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import time
import argparse
from inky import InkyPHAT
from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

try:
    import geocoder
except ImportError:
    exit("This script requires the geocoder module\nInstall with: sudo pip install geocoder")

try:
    from bs4 import BeautifulSoup
except ImportError:
    exit("This script requires the bs4 module\nInstall with: sudo pip install beautifulsoup4")


print("""Inky pHAT: Frustrated
Displays a notifcation when Barry is frustrated.
""")

# Command line arguments to set display colour

parser = argparse.ArgumentParser()
parser.add_argument('--colour', '-c', type=str, required=True, choices=["red", "black", "yellow"], help="ePaper display colour")
args = parser.parse_args()

# Set up the display

colour = args.colour
inky_display = InkyPHAT(colour)
inky_display.set_border(inky_display.BLACK)

# Create a new canvas to draw on
img = Image.open("frustrated-bg.png")
draw = ImageDraw.Draw(img)

# Load the FredokaOne font
font = ImageFont.truetype(FredokaOne, 22)

datetime = time.strftime("%d/%m %H:%M")
draw.text((104, 24), datetime, inky_display.WHITE, font=font)
draw.text((104, 48), "Test message", inky_display.WHITE, font=font)

# Display the weather data on Inky pHAT
inky_display.set_image(img)
inky_display.show()