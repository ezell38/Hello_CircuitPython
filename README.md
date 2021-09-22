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


## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
