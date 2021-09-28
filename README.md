# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
The code turns the LED light on for the board corresponding to the RGB colors (R,G,B) with a .5 second delay between each color.

Here's how you make code look like code:
```
print("Make it work!")

while True:
    dot.fill((0,255,0))
    time.sleep(.5)
    dot.fill((255,0,0))
    time.sleep(.5)
    dot.fill((0,0,255))
    time.sleep(.5)
 ```
[Full Code Here](https://github.com/Adicesa05/circuitPython/blob/main/HelloCircuitPython.py)

### Evidence
![HelloWorldLED](https://github.com/Adicesa05/circuitPython/blob/main/VideosOrPhotos/HelloWorldLEDBlink.gif)

### Images
No wiring needed, metro board came with built in LED.

### Reflection
Had trouble with library, after updating the board it fixed the issue.




## CircuitPython_Servo

### Description & Code
Servo controlled by two loose wires, touching one wire rotates the servo clockwise and the other anti-clockwise.
```python
touch1 = touchio.TouchIn(touch_pad1)
touch2 = touchio.TouchIn(touch_pad2)

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

angle = 90

while True:
    if touch1.value:
        print("#1 Touched")
    if touch2.value:
        print("#2 Touched")

    if angle < 180 and touch1.value:

        angle = angle + 5
        my_servo.angle = angle
        print("angle: ", angle)
    if angle > 0 and touch2.value:
        angle = angle - 5
        my_servo.angle = angle
        print("angle: ", angle)

    time.sleep(0.05)

```
[Full Code Here](https://github.com/Adicesa05/circuitPython/blob/main/Servo.py)
### Evidence

### Images

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection
