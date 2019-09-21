# LPTC-CoderDojo-Microbits
Simple projects for introducing Python programming using BBC Microbit boards.


Online editor: https://python.microbit.org/v/1.1

API documentation: https://microbit-micropython.readthedocs.io/en/latest/microbit_micropython_api.html

## Hello World
Simple "Hello World" as found when starting the online editor:

	from microbit import *
	
	while True:
	    display.scroll('Hello, World!')
	    display.show(Image.HEART)
	    sleep(2000)


## Toggling LEDs
Use the *display.set_pixel(row, column, brightness)* function to turn on/off LEDs. Allowed values for function parameters are 0 to 9.

Introduce the notion of variables: x, y.

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

## Control LED brightness
Use display.set_pixel(x, y, value) to dim up and down an LED's brightness.

Increase the value of the brightness variable from 0 to 9 to increase the brighness of an LED.

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

	  
Modify the code above to decrease the brightness of the LED instead of increasing it.


