import RPi.GPIO as GPIO          
from time import sleep


class RCcontrol:
    def __init__(self, m1_pin1, m1_pin2, m1_en, m2_pin1, m2_pin2, m2_en):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.motor1_pin1 = m1_pin1
        self.motor1_pin2 = m1_pin2
        self.motor1_en = m1_en
        self.motor2_pin1 = m2_pin1
        self.motor2_pin2 = m2_pin2
        self.motor2_en = m2_en
        self.pwm = 100

        GPIO.setup(self.motor1_pin1, GPIO.OUT)
        GPIO.setup(self.motor1_pin2, GPIO.OUT)
        GPIO.setup(self.motor1_en, GPIO.OUT)
        GPIO.output(self.motor1_pin1, False)
        GPIO.output(self.motor1_pin2,False)

        GPIO.setup(self.motor2_pin1, GPIO.OUT)
        GPIO.setup(self.motor2_pin2, GPIO.OUT)
        GPIO.setup(self.motor2_en, GPIO.OUT)
        GPIO.output(self.motor2_pin1, False)
        GPIO.output(self.motor2_pin2, False)

        self.motor1_pwm=GPIO.PWM(self.motor1_en, 1000)
        self.motor1_pwm.start(self.pwm-1)

        self.motor2_pwm=GPIO.PWM(self.motor2_en, 1000)
        self.motor2_pwm.start(self.pwm)

    def forward(self, duration):
        GPIO.output(self.motor1_pin1, True)
        GPIO.output(self.motor1_pin2, False)
        GPIO.output(self.motor2_pin1, True)
        GPIO.output(self.motor2_pin2, False)
        sleep(duration)
        self.stop()

    def backward(self, duration):
        GPIO.output(self.motor1_pin1, False)
        GPIO.output(self.motor1_pin2, True)
        GPIO.output(self.motor2_pin1, False)
        GPIO.output(self.motor2_pin2, True)
        sleep(duration)
        self.stop()

    def left(self, duration):
        GPIO.output(self.motor1_pin1, True)
        GPIO.output(self.motor1_pin2, False)
        GPIO.output(self.motor2_pin1, False)
        GPIO.output(self.motor2_pin2, True)
        sleep(duration)
        self.stop()

    def right(self, duration):
        GPIO.output(self.motor1_pin1, False)
        GPIO.output(self.motor1_pin2, True)
        GPIO.output(self.motor2_pin1, True)
        GPIO.output(self.motor2_pin2, False)
        sleep(duration)
        self.stop()

    def stop(self):
        GPIO.output(self.motor1_pin1, False)
        GPIO.output(self.motor1_pin2, False)
        GPIO.output(self.motor2_pin1, False)
        GPIO.output(self.motor2_pin2, False)
