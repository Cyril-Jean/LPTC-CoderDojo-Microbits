# Use display.set_pixel(x, y, value) to dim up and down an LED's brightness
from microbit import *

x = 2
y = 2
dim = 0
display.clear()
while True:
    display.set_pixel(x, y, dim)
    sleep(200)
    dim = dim + 1
    if dim > 9:
        dim = 0
    
    