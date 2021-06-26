import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Create the display (configuration for CS pin & DC pin)
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)

# config for display baudrate (default max is 24mhz)
BAUDRATE = 24000000

# set up SPI bus using hardware SPI:
spi = board.SPI()

# create the display
disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate = BAUDRATE)

# input pins
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT 

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT 

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT 

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

# Turn on the backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

# create blank image for drawing.
# Make sure to create image with mode 'rgb for color.
width = disp.width
height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image
draw = ImageDraw.Draw(image)

#clear display
draw. rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0)) # red
disp.image(image)

# get drawing object to draw on image
draw = ImageDraw.Draw(image)

# draw a black filled box to clear the image
draw.rectangle((0, 0, width, height), outline=0, fill=0)

#font
fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
fnt2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
fnt3 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)

## map part start
ROADWIDTH = 12
ROADHEIGHT = 12
ROW = 20
COL = 20
SCREENWIDTH = ROADWIDTH * COL
SCREENHEIGHT = ROADHEIGHT * ROW
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
DEEP_RED = (204, 0, 0)
ORANGE = (255, 153, 0)
PINK = (255, 102, 255)
PURPLE = (153, 0, 255)
GREEN = (0, 255, 0)
SKY = (0, 255, 255)
ROAD = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 3, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 2, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 4, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 5, 0, 0, 0, 0,
    0, 2, 1, 1, 1, 1, 1, 5, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
food = 160


# intro (rainbow)
def intro():
    cnt = 0
    while True:
        if cnt == 0:
            draw.text((0, 80), "Game Start", font=fnt, fill=WHITE)
        elif cnt == 1:
            draw.text((0, 80), "Game Start", font=fnt, fill=RED)
        elif cnt == 2:
            draw.text((0, 80), "Game Start", font=fnt, fill=ORANGE)
        elif cnt == 3:
            draw.text((0, 80), "Game Start", font=fnt, fill=YELLOW)
        elif cnt == 4:
            draw.text((0, 80), "Game Start", font=fnt, fill=GREEN)
        elif cnt == 5:
            draw.text((0, 80), "Game Start", font=fnt, fill=SKY)
        elif cnt == 6:
            draw.text((0, 80), "Game Start", font=fnt, fill=BLUE)
        elif cnt == 7:
            draw.text((0, 80), "Game Start", font=fnt, fill=PURPLE)
            cnt = -1

        cnt += 1
        draw.text((20, 140), "PRESS \"C\" BUTTON", font=fnt2, fill=WHITE)
        if not button_C.value: # center pressed
            break
        disp.image(image)
# if ghost eat pacman
def end():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 77), "GAME OVER", font=fnt, fill=WHITE)
    draw.text((0, 80), "GAME OVER", font=fnt, fill=RED)
    draw.text((0, 83), "GAME OVER", font=fnt, fill=DEEP_RED)
    disp.image(image)
# if pacman live and map empty
def happy_end():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((30, 80), "YOU WIN", font=fnt, fill=WHITE)
    draw.text((30, 83), "YOU WIN", font=fnt, fill=SKY)
    draw.text((30, 86), "YOU WIN", font=fnt, fill=BLUE)
    disp.image(image)


## about map
# return road's index
def gps(x1, y1):
    x1 = x1/12
    y1 = y1/12
    index = y1*20+x1
    return int(index)

def square(x, y): # draw blue road
    draw = ImageDraw.Draw(image)
    draw.rectangle((x, y, x+12, y+12), fill=BLUE, outline=BLUE)
    disp.image(image)

def eat(x, y):
    draw = ImageDraw.Draw(image)
    draw.ellipse((x+4, y+4, x+8, y+8), fill=WHITE, outline=WHITE)
    disp.image(image)

def fruit(x, y, color):
    draw = ImageDraw.Draw(image)
    draw.ellipse((x+1, y+1, x+9, y+9), fill=color, outline=color)
    disp.image(image)

def world():
    for i in range(len(ROAD)):
        road = ROAD[i]

        if road != 0:
            x = (i % 20) * 12
            y = (i//20) * 12
            square(x, y)

            if road == 2: # green apple
                fruit(x, y, GREEN)
            elif road == 3: # apple
                fruit(x, y, RED)
            elif road == 4: # grape
                fruit(x, y, PURPLE)
            elif road == 5: #peach
                fruit(x, y, PINK)
            else:
                eat(x, y)
## map part end


## pacman part start
x1 = 96
y1 = 156
x2 = x1+12
y2 = y1+12

def pacman(button):
    if button == 'none':
        draw.rectangle((x1, y1, x2, y2), fill=BLUE, outline=BLUE)
        draw.ellipse((x1+5.5, y1+5.5, x2-5.5, y2-5.5), fill=WHITE, outline=WHITE)
    if button == 'U':
        draw.pieslice((x1, y1, x2, y2), start=300, end=240, fill=YELLOW)
    if button == 'D':
        draw.pieslice((x1, y1, x2, y2), start=120, end=60, fill=YELLOW)
    if button == 'L':
        draw.pieslice((x1, y1, x2, y2), start=210, end=150, fill=YELLOW)
    if button == 'R' or button == 'start':
        draw.pieslice((x1, y1, x2, y2), start=30, end=330, fill=YELLOW)

## pacman part end   


## ghost part
# ghost position
gx1 = 12 * random.randrange(2, 16)
gy1 = 12 * random.randrange(2, 18)

# draw ghost
def ghost(gx, gy, color):
    #ghost random move
    g_index = gps(gx, gy)

    if ROAD[g_index] > 0:

        draw.pieslice((gx, gy, gx+12, gy+12), start=135, end=35, fill=color)
        draw.polygon(((gx+3, gy+6),(gx+9, gy+6),(gx+6, gy+12)), fill=color, outline=color)
        draw.ellipse((gx+1, gy+1, gx+6, gy+5), fill=WHITE, outline=WHITE)
        draw.ellipse((gx+6, gy+1, gx+11, gy+5), fill=WHITE, outline=WHITE)
        draw.ellipse((gx+3, gy+2, gx+6, gy+4), fill=BLACK, outline=BLACK)
        draw.ellipse((gx+9, gy+2, gx+12, gy+4), fill=BLACK, outline=BLACK)

#remove ghost
def remove(gx, gy):
    i = gps(gx, gy)
    if ROAD[i] > 0:
        square(gx, gy)

        if ROAD[i] == 1: # food
            eat(gx, gy)
        elif ROAD[i] == 2: # green apple
            fruit(gx, gy, GREEN)
        elif ROAD[i] == 3: # apple
            fruit(gx, gy, RED)
        elif ROAD[i] == 4: # grape
            fruit(gx, gy, PURPLE)
        elif ROAD[i] == 5: #peach
            fruit(gx, gy, PINK)
        else:
            draw.ellipse((gx+5.5, gy+5.5, gx+12-5.5, gy+12-5.5), fill=WHITE, outline=WHITE)


## play game
intro()  

# draw map
draw.rectangle((0, 0, width, height), outline=0, fill=0)       
world()   

# make pacman
button = 'start'
init = 'none'
pacman(button)
#food -= 1 # eat food in start position

cnt = 15 # control ghost time
flag = 0
score = 0

while True:
    p_index = gps(x1, y1)
    
    # game over
    if x1 == gx1 and y1 == gy1:
        break

    # Happy end
    if score == 18000:
        flag = 1
        break


    # pacman move
    if ROAD[p_index] > 0:   
        if not button_U.value:  # up pressed
            if ROAD[p_index-20] > 0:
                pacman(init)
                y1 -= 12
                y2 -= 12
                button = 'U'

        if not button_D.value:
            if ROAD[p_index+20] > 0:
                pacman(init)
                y1 += 12
                y2 += 12
                button = 'D'

        if not button_L.value:
            if ROAD[p_index-1] > 0:
                pacman(init)
                x1 -= 12
                x2 -= 12
                button = 'L'

        if not button_R.value:
            if ROAD[p_index+1] > 0:
                pacman(init)
                x1 += 12
                x2 += 12
                button = 'R'

        #score
        if ROAD[p_index] != 10:
            score += ROAD[p_index] * 100

        ROAD[p_index] = 10
            

    pacman(button)

    # score
    draw.text((200, 6), "SCORE", font=fnt3, fill=WHITE)
    draw.line((200, 24, 240, 24), fill=WHITE, width=2)
    draw.rectangle((200, 30, 240, 40), outline=0, fill=0)
    draw.text((200, 30), '{0:05d}'.format(score), font=fnt3, fill=WHITE)

    #make ghost
    if cnt % 15 == 0:
        # ghost reposition
        gx1 = 12 * random.randrange(2, 16)
        gy1 = 12 * random.randrange(2, 18)

        ghost(gx1, gy1, ORANGE)
        cnt -= 1
    else:
        if cnt % 15 == 1:
            cnt += 14
            remove(gx1, gy1)
        else:
            cnt -= 1      
    
    # display the image
    disp.image(image)

    time.sleep(0.001)
    

#ending
if flag == 0:
    end()
else:
    happy_end()