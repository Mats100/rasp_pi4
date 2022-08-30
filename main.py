import RPi.GPIO as GPIO
import time
def setup():
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(20, GPIO.OUT)       #relay1
     GPIO.setup(21, GPIO.OUT)       #relay2
     GPIO.setup(22, GPIO.OUT)       #red
     GPIO.setup(23, GPIO.OUT)       #yellow
     GPIO.setup(24, GPIO.OUT)       #green

def control_traffic_lights():
    GPIO.output(24, 1)
    time.sleep(4)
    GPIO.output(24, 0)

    GPIO.output(23, 1)
    time.sleep(3)
    GPIO.output(23, 0)

    GPIO.output(22, 1)
    time.sleep(5)
    GPIO.output(22, 0)

    GPIO.output(23, 1)
    time.sleep(3)
    GPIO.output(23, 0)

response = None
while not (response == "on" or response == "off"):
    response = input("Do you want to turn on relay?").lower()
setup()
try:
    while True:
        if response == "on":
            control_traffic_lights()
            print("Its On")
            time.sleep(3)
        else:
            GPIO.setup(20, GPIO.HIGH)
            GPIO.setup(21, GPIO.HIGH)
            GPIO.setup(22, GPIO.HIGH)
            GPIO.setup(23, GPIO.HIGH)
            GPIO.setup(24, GPIO.HIGH)
            print("Its Off")
            time.sleep(3)

except:
    print("You Have Exited The Program")
finally:
    GPIO.cleanup()