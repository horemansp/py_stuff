from RPi import GPIO
from time import sleep

clk = 12
dt = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
prev_clk = GPIO.input(clk)
prev_dt = GPIO.input(dt)


while True:
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != prev_clk:
        if clkState ==0 and dtState ==1:
            counter=counter+1
            print(counter)
        if clkState ==0 and dtState ==0:
            counter=counter-1
            print(counter)
        prev_clk = clkState
