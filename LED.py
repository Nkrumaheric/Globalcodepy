from gpiozero import LED
import time
led = LED(18)
 
led.on()
time.sleep(10)
led.off()