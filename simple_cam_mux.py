import os, sys
import RPi.GPIO as GPIO
import time

# Pin Definitions
output_pin = 18  # BCM pin 18, BOARD pin 12  #cmd1

#output_pin = 17  # BCM pin 18, BOARD pin 11  #cmd0

# Pin Setup:
GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
# set pin as an output pin with optional initial state of HIGH
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)


def main():
    print("Start testing the camera 1_A")
    GPIO.output(output_pin, GPIO.LOW)
    time.sleep(0.5)
    
    capture(1)
    
    print("Start testing the camera 1_B")   
    GPIO.output(output_pin, GPIO.HIGH)
    time.sleep(0.5)    
    capture(2)
    
    GPIO.cleanup()

def capture(cam):
    #cmd = "raspistill -o capture_%d.jpg" % cam
    cmd0 = "nvgstcapture-1.0 -A --capture-auto -S 0 --orientation 2 --sensor-id 0 --image-res=3 --file-name=capture_%d.jpg" % cam
    cmd1 = "nvgstcapture-1.0 -A --capture-auto -S 0 --orientation 2 --sensor-id 1 --image-res=3 --file-name=capture_%d.jpg" % cam
    os.system(cmd1)


if __name__ == '__main__':
    main()
