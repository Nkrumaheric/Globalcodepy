from gpiozero import LED
from time import sleep

led = LED(18)#white
led1 = LED(17)#green
led2 = LED(27)#blue
led3 = LED(22)#red
led4 = LED(23)#yellow

while True:
    led.on()
    sleep(0.02)
    led.off()
    sleep(0.02)
    
    led3.on()
    sleep(0.02)
    led3.off()
    sleep(0.02)
    
    led1.on()
    sleep(0.02)
    led1.off()
    sleep(0.02)
    
    led4.on()
    sleep(0.02)
    led4.off()
    sleep(0.02)
    
    led2.on()
    sleep(0.02)
    led2.off()
    sleep(0.02)