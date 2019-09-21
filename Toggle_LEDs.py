# Add your Python code here. E.g.
from microbit import *

x = 0
y = 0
while True:
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(200)
    x = x + 1
    if x > 4:
        x = 0
    
    