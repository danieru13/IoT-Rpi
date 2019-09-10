# External module imports
from gpiozero import LED, PWMLED, Button
import time

# Pin Definitons:

dc = 0.95 # duty cycle (0-1) for PWM pin

pwm = PWMLED(18, frequency=50, initial_value=dc) # Broadcom pin 18 (P1 pin 12)

led = LED(23) # Broadcom pin 23 (P1 pin 16)

btn = Button(17) # Broadcom pin 17 (P1 pin 11)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if btn.is_pressed != True: # button is released
            pwm.value = dc       
            led.off()
        else: # button is pressed:
            pwm.value = 1-dc

            led.on()
            time.sleep(0.075)

            led.off()
            time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    exit(0)