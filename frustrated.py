#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import json
import time
import urllib
import sys
from PIL import Image, ImageFont

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

import inkyphat


print("""Inky pHAT: Frustrated

Displays a notifcation when Barry is frustrated.

""")

if len(sys.argv) < 2:
    print("""Usage: {} <colour>
       Valid colours: red, yellow, black
""".format(sys.argv[0]))
    sys.exit(0)

colour = sys.argv[1]

try:
    inkyphat.set_colour(colour)
except ValueError:
    print('Invalid colour "{}" for V{}\n'.format(colour, inkyphat.get_version()))
    if inkyphat.get_version() == 2:
        sys.exit(1)
    print('Defaulting to "red"')

inkyphat.set_border(inkyphat.BLACK)

# Load the built-in FredokaOne font
font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 22)

# Load our backdrop image
inkyphat.set_image("resources/backdrop.png")

# Let's draw some lines!
#inkyphat.line((69, 36, 69, 81)) # Vertical line
#inkyphat.line((31, 35, 184, 35)) # Horizontal top line
#inkyphat.line((69, 58, 174, 58)) # Horizontal middle line
#inkyphat.line((169, 58, 169, 58), 2) # Red seaweed pixel :D

# And now some text

datetime = time.strftime("%d/%m %H:%M")
inkyphat.text((104, 24), datetime, inkyphat.WHITE, font=font)
inkyphat.text((104, 48), "Test message", inkyphat.WHITE, font=font)

# And show it!
inkyphat.show()