import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it wokr!")

while True:
    dot.fill((0,255,0))
    time.sleep(.5)
    dot.fill((255,0,0))
    time.sleep(.5)