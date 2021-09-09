import board
import neopixel
import sleep

dot = neopixel.Neopixel(board.NEOPIXEL, 1)

while True:
    print("Make it red")
    dot.fill((0, 0, 255))
    time.sleep(.5)
    print("Make it blue")
    dot.fill((0, 255, 0))
    time.sleep(.5)
    print("Make it green")
    dot.fill((255, 0 ,0))
    time.sleep(.5)