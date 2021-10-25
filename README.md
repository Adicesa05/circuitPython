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
![Servo](https://github.com/Adicesa05/circuitPython/blob/main/VideosOrPhotos/ServoTouchCircuit.png)

### Images
![ServoVideo](https://github.com/Adicesa05/circuitPython/blob/main/VideosOrPhotos/LooserWireServoVideo.gif)

### Reflection
At fist it did not work because I did not set the angle to not go over 180 and not less that 0. The if command of angle < 180 and angle > 0 fixed the problem.



## Distance_Sensor

### Description & Code
An LED controlled by an ultra sonic sensor, the LED changes color based on the distance the ultra sonic detects.
```python
while True:
    try:
        cm = sonar.distance
        print((cm,))
        if cm < 5: #If it's too close, turns off LED
         dot.fill((0, 0, 0))
        elif cm < 20: #Range 5-14 cm
         redValue = simpleio.map_range(cm, 5, 20, 255, 0) #Red value of RGB increases the closer it is.
         greenValue = 0
         blueValue = simpleio.map_range(cm, 5, 20, 0, 255) #Blue value of RGB increases the further it is.
         print("RGB: (", redValue, ", ", greenValue, ", ", blueValue, ")")
         dot.fill((int(redValue), int(greenValue), int(blueValue)))
        elif cm < 35: #Range 21-34 cm
         redValue = 0
         greenValue = simpleio.map_range(cm, 20, 35, 0, 255) #Green value of RGB increases the further it is.
         blueValue = simpleio.map_range(cm, 20, 35, 255, 0) #Blue value of RGB increases the closer it is.
         print("RGB: (", redValue, ", ", greenValue, ", ", blueValue, ")")
         dot.fill((int(redValue), int(greenValue), int (blueValue)))
        else:
          dot.fill((0, 0, 0))
        time.sleep(0.1)
    except RuntimeError:
        print("Retrying!")  #Prints an error code when not detecting distance.

```
``
Code made by: Johnny Krosby
``
[Full Code Here](https://github.com/jkrosby51/CircuitPython/blob/main/DistanceRGB.py)

### Evidence
![DistanceSensorCircuit](https://github.com/Adicesa05/circuitPython/blob/main/VideosOrPhotos/DistanceSensor.png)

### Images
![DistanceSensorGIF](https://github.com/Adicesa05/circuitPython/blob/main/VideosOrPhotos/gabyD-DistanceRGB.gif)

[Gif Credit](https://github.com/gdaless20/Circuitpython#CircuitPython_Distance_Servo)
### Reflection
Learning the simpleio mapping tool is essential for this project. Simpleio mappping tool essentially converts the distance produced by the Ultra sonic distance sensor into RGB values for the board to produce cool lights.


