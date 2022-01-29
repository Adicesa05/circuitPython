# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Skateboard](#Skateboard)
* [Lego_Block](#Lego_Block)
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



## CircuitPython_LCD

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

# OnShape / CAD

## Skateboard

### Description

A skatebaord consisting of the deck, truck baseplate, truck hanger, bushing, wheels, and bearings.

### Images and steps

![SkateBoardDeck](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/Skateboard%20Deck.png)

The deck consists of 8 small holes of countersink, through, ASNI, Clearence, size#10, free fit holes.

![SkateboardDeckSketch](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/SkateboardSketch.png)

The deck's sketch is made from 2 circles and a rectangle, the circles have to be equal. 

![TruckBasePlate](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/Baseplate.png)

This may look complicated but looking from the side, the sketch is very simple. The sketch consists of a square on top which is where you put the screws in as a base/hat followed by 2 rectangle sketches extruded under in the middle of the base symmetrically. Then cover the baseplate with fillets.

![TruckHanger](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/TruckHanger.png)

The hanger is made from a circle extruded down to the pipe which is made from a circle (not connected) extruded from the sketch of the baseplate. The wing hanging out is just an extruded circle + rectangle. 

![Bushing](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/Bushing.png)

The bushing is super easy, it's just an extruded circle with the hole equal to the truck hanger wing. It resides right on top of the hanger wing.

![Wheel](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/Wheel.png)

The wheel is made from using the revolve tool then extruding a center circle (Pro tip: UseTool) symmetrically.

![Bearing](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/Bearings.png)

The bearing is just two circles extruded equal to the center hole in the wheel.

![Skatebaord](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/Skateboard.png)

The finished product should look similar to this. 

### Reflection

-A problem I ran into is when trying to extrude the circle to make the pipe from the hanger is that I forgot to make the sketch visible costing me a bit of time and confusion. Making a sketch visible can give the option to extrude involving that visible sketch.

-A shortcut in the assembly is after attaching the baseplate,hanger,bushing together to the deck you can copy all 3 parts and paste it to connect to the other 4 holes under the deck.

-A very great tip that I learnt from my [awesome engineering teacher](https://github.com/Helmstk1) is that holding shift while selecting parts to mate locks the specific part you are mating making you able to move into a better angle to select that part to mate. 

## Lego_Block

### Description

This part teaches you mainly about configurations, the configurations help you create different variations of the same part you are creating without wasting so much time creating 10 similar parts.

### Images and steps

![Lego](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/LEgoblock.png)
![Variables](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/CoolVariable.png)
I created a lego block, really really really important to make sure you set your variables as they are ESSENTIAL for configurations.

![Configs](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/Congfi.png)
The configurations tab is located on the right side of the screen, to create a configurations you have to click on the configurations features and click on the values you want to configurate an example would be sizing, you can assign different values changing the variables you created earlier. You can customize a lot of things with configurations such as size, type, color, name, etc.

![PArtsw](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/parts.png)

These parts are custom features where it is created by someone else, you can add these custom features by just clicking on the one you want to add.

[PartName](https://cvilleschools.onshape.com/documents/f4d470584fdeef9603415532/v/0c632933b6aca3d2608fda5d/e/acddbbed81af3772a07adf21)

[PartColor](https://cvilleschools.onshape.com/documents/d997b0ffc30f659113b10c00/v/347f7240ed6eefd77e80907e/e/a59f52547080e509330b02f7)

### Reflection

A very important thing that I got confused on was the suppressions, the suppressions are there to remove the features that overlaps when it shouldn't be there. A 4x2 block would have a feature that a 1x1 block wouldn't and by suppressing the feature you can exclude it for the parts that shouldn't have them.

Creating variables are extremely important and the sooner you create them in your project the better, variables can help with a lot of things even outside of configurations. Imagine you wanted to change the height of the object or an angle, you can easily change the variable instead of going into the specific part and changing it.

## Lego_Duck

### Description

Build a lego duck using lego bricks from [Lego_Block](#Lego_Block) and also create a drawing diagram. This assignment puts the configurations that you've created into use and in this assignment you get to learn how to put the blocks together and how to mate them.

### Images and steps
![ducklego](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/ducklego.png)

The duck is made up of 2 2x2 bricks, 2 3x2 half bricks, 1 4x2 brick, and 1 1x2 brick.

![guidelego](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/guidelego.png)

Click "Insert" then from the menu, you can generate the types of bricks that you need for building. This is where the configurations from earlier came in handy, it saves us a lot of time from creating all the individual bricks.
You then want to fasten mate the blocks together creating the duck.

An example on how configurations can be useful is how many combinations you can mess around with, I made a gigantic 25x25 base brick then filled in specific parts with legos to create a qr code.

![SCANME](https://github.com/Adicesa05/circuitPython-OnShape/blob/main/VideosOrPhotos/SCANME.png)

### Reflection

The most important thing before you start putting the blocks together are your mate connectors, make sure they are visible so that when mating you can mate freely on all the lego pillars.

Pro tip: The replicate tool can greatly reduce time on generating duplicate bricks.
