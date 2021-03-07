# import required libs
import time
import RPi.GPIO as GPIO


# initialize variables and constants -------------------------
gpio_port1 = 5 #BMC numbering
gpio_pindefinition=[[5,0]] #1=output, 0=input
counter = 0
# Function definitions-----------------------------------------------------
def gpio_init(pin_list):
    GPIO.cleanup()
    for pin in range(len(pin_list)):
        if pin_list[pin][1] == 1:
            GPIO.setup(pin_list[pin][0],GPIO.OUT)
            GPIO.output(pin_list[pin][0], False)
        else:
            GPIO.setup(pin_list[pin][0],GPIO.IN, pull_up_down=GPIO.PUD_UP)
def gpio_end():
    GPIO.cleanup()

    
# Initialize (run once)----------------------------------------------------

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # gebruik BCM nummering (Makkelijker met T-cobbler)
gpio_init(gpio_pindefinition)


# Start van de main loop---------------------------------------------------

while True:
    p1_state = GPIO.input(gpio_port1)
    print(p1_state)
    time.sleep(0.1)


#end of loop finish (run once after loop)-----------------------------------
 
gpio_end()
