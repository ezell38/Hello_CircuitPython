# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

The assignment was to make the light flash back and forth between two colors.

Here's how you make code look like code:

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
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.
<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/IMG-202814240%20(1).gif?raw=true" alt="NeoPixel Demo" width="500" >

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. 

One mistake I made was forgeting to import time into the code. When I thought I had finished my code I plugged it into the Metro board and the lights were flashing at wierd intervals. Then once I inserted time it flashed back and forth perfectly. 


## CircuitPython_Servo

### Description & Code

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

<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/Capture.PNG?raw=true" alt="ServoDemo" width="500" 

### Reflection

While uploading the code onto the Metro board I realized that I had it set to upload to my file and not to the board. I had to save it as "code" in my CircuitPython folder.


## CircuitPython_Distance

### Description & Code
     
This assignment was to make it so the distance on the ultrasonic sensor corresponds with the color displayed on the Metro board.

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

<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/Capture.1.PNG?raw=true" alt="CircuitPythonDistance" width="500">
Capture.1.PNG

### Reflection

This assignment was hard because I kept saving the code to a file on my computer and not my Metro board. I also used some code from another student and didn't adjust my wiring to fit their code which messed up my Ultrasonic sensor. 

## CircuitPython_Photointerrupters

### Description & Code

The goal of this assignment was to make the serial moniter display how many times the photointerrupter was interrupted in a 4 second span.

```python
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

max = 4
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

5v -> +,L
D1 -> Out
GND -> - 

### Reflection 

