import time
import board
import pwmio
import touchio
import servo

touch_pad1 = board.A3
touch_pad2 = board.A5

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