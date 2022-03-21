# CircuitPython

This is my repository for my Circuit Python assignments for Engineering 3. If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code

The assignment was to make the light flash back and forth between two colors. I used the while true function and dot fill to tell the metro board the color that correlates with the distance. 

```python
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness=0.2

while True:
    print("Make it Green!")
    dot.fill((255, 0, 0))
    time.sleep(.5)
    print("Make it White!")
    dot.fill((0, 0, 255))
    time.sleep(.5)

```


### Evidence

<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/IMG-202814240%20(1).gif?raw=true" alt="NeoPixel Demo" width="500" >

### Reflection

One mistake I made was forgeting to import time into the code. When I thought I had finished my code I plugged it into the Metro board and the lights were flashing at weird intervals. Then once I inserted time it flashed back and forth perfectly. 


## CircuitPython_Servo

### Description & Code

The goal of this assignment was to make a servo move back and forth 180 degrees. using the print function allows you to tell the servo what angle want it to got to.

```python
import pwmio
import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
print("hello")
while True:

    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        print(angle)
        time.sleep(0.05)
    for angle in range(180, 0, -5):   # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence

<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/IMG-94088208.gif?raw=true" alt="ServoDemo" width="500" >

### Wiring

<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/Capture.PNG?raw=true" alt="ServoDemo" width="500"> 

### Reflection

While uploading the code onto the Metro board I realized that I had been uploading it onto my computer and not to the board. I had to save it as "code.py" in my CircuitPython folder.


## CircuitPython_Distance

### Description & Code
     
This assignment was to make it so the distance on the ultrasonic sensor corresponds with the color displayed on the Metro board. I did this by using the try function.
     

```python
import adafruit_hcsr04
import time
import board
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness = 0.1

while True:
    try:
        dist = sonar.distance
        print((dist))
        r = max(min(15*(20-dist),255),0)
        g = max(min(15*(dist-20),255),0)
        b = max(min(-abs(15*(20-dist))+225,255),0)
        dot.fill((int(r), int(g), int(b)))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```

### Evidence
     
<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/IMG-86812912-3 (1).gif?raw=true" alt="CircuitPython_LCD" width="500">
     
### Wiring

<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/Capture7.PNG?raw=true" alt="CircuitPythonDistance" width="500">

### Reflection

I got this code online and when you import new code it is very important that you adjust your wiring to fit the code. For example, in this assignment I had my digital wire going out from D1 while the code said D2.

## CircuitPython_Photointerrupters

### Description & Code

The goal of this assignment was to make the serial moniter display how many times the photointerrupter was interrupted in a 4 second span. I used if statements to tell it when to add ot the counter. 

```python
interrupter.pull = Pull.UP

counter = 0

photo = False   
state = False

max = 4  #max = seconds
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("The number of interrupts is:", str(counter))
        max = time.time() + 4
        counter = 0

```

### Evidence

<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/IMG-182103440.gif?raw=true" alt="CircuitPython_LCD" width="500">

### Wiring

5v -> +

D1 -> Out

GND -> - 

### Reflection 

One mistake I made during this assignment was setting the max to 5. I did not realize that max correlates to seconds. 

## C,O,M:Fun with RGB LEDs

### Description and Code

The goal of this assignment was to uses classes to make a RGB led blink different colors.

Main Code - 

```import time
import board
from rgb import RGB

r1 = board.D8
b1 = board.D9
g1 = board.D10
r2 = board.D4
b2 = board.D5
g2 = board.D7 # D6 uses the same timer as D8,9,10.  Avoid!

full = 65535                # Max Brightness
half = int(65535/2)         # Half Brightness

myRGBled1 = RGB(r1, g1, b1) # create a new RGB object, using pins 8, 9, & 10
myRGBled2 = RGB(r2, g2, b2) # create a new RGB object, using pins 4, 5, & 7


while True:
    '''Shines two RGB LEDs in opposing colours, then rainbows!'''
    myRGBled1.blue(half)
    myRGBled2.yellow(half)
    time.sleep(1)
    myRGBled1.red()
    myRGBled2.cyan()
    time.sleep(1)
    myRGBled1.green()
    myRGBled2.magenta()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.blinky(.1) # Obviously you should replace "rate1" with a real number...
    myRGBled2.blinky(.2) # Sames
    time.sleep(3)

# extra spicy (optional):
# myRGB1.rainbow(rate1) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
# myRGB2.rainbow(rate2) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
# time.sleep(5)
``` 
RGB Class Code - 

```import time
import board
import pwmio
import digitalio

lightBulb = digitalio.DigitalInOut(board.D13)       # I moved my RGBLED power wire from 5v
lightBulb.direction = digitalio.Direction.OUTPUT    # and plugged it into D13.  I'll explain later.

class LED:      # It's propper coding to always write a line explaining a class
                # with a "docstring."   Like this:
    '''LED is a class designed for a single color LED to fade in and out'''

    def __init__(self, ledpin, name):
        # init is like void Setup() from arduino.  Initialize your pins here
        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)
        self.name = name

    def fadedown(self): # Fades LED from bright to dim
        for i in range(255):
            if i < (255/2):
                self.led.duty_cycle = int(i * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def fadeup(self):  # Fades LED from dim to bright
        for i in range(255):
            if i > (255/2):
                self.led.duty_cycle = 65535 - int((i - (255/2)) * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def on(self, brightness=65535):  # Remember "on" means duty cycles < 65535
        self.led.duty_cycle = 65535 - brightness
        lightBulb.value = 65535

    def off(self): # "off" means duty cycle should be full.
        self.led.duty_cycle = 65535

class RGB:
    '''this class should impliment all 3 pins together to control an RGB LED'''
    from rgb import LED
        # Let's take a second to appreciate that we're using a class to call a class!
        # Let LED do all the nitty gritty work, this RGB class will be the "manager"


    def __init__(self, redPin, greenPin, bluePin):
        # To initialize an RGB LED, we need to initialize 3 LED pins.
        self.myRedLED = LED(redPin, "red")
        self.myBlueLED = LED(bluePin, "blue")
        self.myGreenLED = LED(greenPin, "green")

    def blue(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.off()

    def red(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myRedLED.on(brightness)
        self.myGreenLED.off()
        self.myBlueLED.off()

    def green(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myGreenLED.on(brightness)
        self.myBlueLED.off()
        self.myRedLED.off()

    def yellow(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.off()
        self.myGreenLED.on(brightness)
        self.myRedLED.on(brightness)

    def cyan(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.on(brightness)
        self.myRedLED.off()

    def magenta(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.on(brightness)

    def white(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.on(brightness)
        self.myRedLED.on(brightness)

    def off(self):
        # This turns off all 3 LEDs, but my LEDs were still glowing a tiny bit.
        # To fix this, i took the RGB power wire out of 5V , and plugged it into D13.
        # Now when I want the LED to be off, it's truly off!
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.off()
        lightBulb.value = 0

    def blinky(self, rate,  brightness=65535):
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.off()

        for i in range(20):
            self.myBlueLED.on(brightness)
            self.myGreenLED.off()
            self.myRedLED.on(brightness)
            time.sleep(rate)
            self.myBlueLED.off()
            self.myGreenLED.off()
            self.myRedLED.on(brightness)
            time.sleep(rate)
            self.myBlueLED.on(brightness)
            time.sleep(rate)
            self.myBlueLED.off()
            time.sleep(rate)
            self.myBlueLED.on(brightness)
            self.myGreenLED.on(brightness)
            self.myRedLED.off()
            time.sleep(rate)
            self.myBlueLED.off()
            self.myGreenLED.off()
            self.myRedLED.off()
            time.sleep(rate)
            self.myGreenLED.on(brightness)
            time.sleep(rate)
            self.myGreenLED.off()
            time.sleep(rate)
            self.myBlueLED.off()
            self.myGreenLED.on(brightness)
            self.myRedLED.on(brightness)
            time.sleep(rate)
            self.myBlueLED.off()
            self.myGreenLED.off()
            self.myRedLED.off()
            time.sleep(rate)
            self.myRedLED.on(brightness)
            time.sleep(rate)
            self.myRedLED.off()
            time.sleep(rate)

```

### Wiring 

<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Capture20.PNG?raw=true" alt="RGB LED" width="500" >

### Evidence 





