import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
	spi,
	cs=cs_pin,
	dc=dc_pin,
	rst=reset_pin,
	baudrate=BAUDRATE,
	width=135,
	height=240,
	x_offset=53,
	y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
padding = -2
top = padding
bottom = height - padding
x = 0

font = ImageFont.truetype("/usr/share/fonts/paskowy/paskowy/Paskowy.ttf", 50)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

from time import strftime, sleep
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
display = st7789.ST7789(
	board.SPI(),
	cs=cs_pin,
	dc=dc_pin,
	rst=reset_pin,
	baudrate=BAUDRATE,
	width=135,
	height=240,
	x_offset=53,
	y_offset=40,
)


# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
# Paskowy
# font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font = ImageFont.truetype("/usr/share/fonts/paskowy/paskowy/Paskowy.ttf", 50)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

import random 

while True:
	colors = ["red", "orange", "yellow","green", "blue", "indigo", "violet"]
	random_index = random.randint(0,len(colors)-1)
	color = (colors[random_index])
	#TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
	if buttonA.value and buttonB.value:
		backlight.value = False  # turn off backlight
	else:
		backlight.value = True  # turn on backlight
	if buttonB.value and not buttonA.value: #Button A Pressed
		# Make sure to create image with mode 'RGB' for full color.
		height = disp.width  # we swap height/width to rotate it to landscape!
		width = disp.height
		image = Image.new("RGB", (width, height))
		rotation = 90

		# Get drawing object to draw on image.
		draw = ImageDraw.Draw(image)

		# Draw a black filled box to clear the image.
		draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
		disp.image(image, rotation)
		# Draw a black filled box to clear the image.
		draw.rectangle((0, 0, width, height), outline=0, fill="white")
		font2 = ImageFont.truetype("/usr/share/fonts/paskowy/paskowy/Paskowy.ttf", 32)
		draw.text((10, 10), "Welcome to Bar-Code-A-Clock!", font=font2, fill=color)


		# Display image.
		disp.image(image, rotation)
		time.sleep(1)
	if buttonA.value and not buttonB.value:  # just button B pressed
		from time import strftime, sleep

		# Draw a black filled box to clear the image.
		draw.rectangle((0, 0, width, height), outline=0, fill="white")
		str_time = strftime("%m/%d/%Y %H:%M:%S")
		month_time = strftime("%m")
		day_time = strftime("%m")
		year_time = strftime("%m")
		hour_time = strftime("%H")
		minute_time = strftime("%m")
		second_time = strftime("%m")
		draw.text((10, 10), str_time, font=font, fill= color)


		# Display image.
		disp.image(image, rotation)
		time.sleep(1)
  # set the screen to white
	if not buttonA.value and not buttonB.value:  # none pressed
		display.fill(color565(*list(webcolors.name_to_rgb("blue")))) # set the screen to the users color
		# draw.rectangle((0, 0, width, height), outline=0, fill="white")
		# draw.text((10, 10), "Welcome to Bar-Code-A-Clock", font=font, fill="black")

