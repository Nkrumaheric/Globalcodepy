from gpiozero import LED,Button
from signal import pause
import time

led = LED(18)
button = Button(2)

button.when_pressed = led.on
time.sleep(5)
button = led.off()
time.sleep(5)

pause()
