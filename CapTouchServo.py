"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import servo
import touchio

touch_A0 = touchio.TouchIn(board.A0)
touch_A5 = touchio.TouchIn(board.A5)


pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
angle = 0
my_servo.angle = angle

while True:
    if angle <= 175 and touch_A0.value:
        print("Touched Pin0")
        angle = angle + 5
        my_servo.angle = angle

    if angle >= 5 and touch_A5.value:
        print("Touched Pin5")
        angle = angle - 5
        my_servo.angle = angle
    time.sleep(0.05)