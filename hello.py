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