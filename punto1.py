# External module imports
####import RPi.GPIO as GPIO
from gpiozero import LED, PWMLED, Button
import time

dc = 0.95 # duty cycle (0-1) for PWM pin
# Pin Definitons:
####pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
pwm = PWMLED(18, frequency=50, initial_value=dc)
####ledPin = 23 # Broadcom pin 23 (P1 pin 16)
led = LED(23)
####butPin = 17 # Broadcom pin 17 (P1 pin 11)
btn = Button(17)

# Pin Setup:
####GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
####pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
####GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for LEDs:
####GPIO.output(ledPin, GPIO.LOW)
####pwm.start(dc)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if btn.is_pressed != True: #GPIO.input(butPin): # button is released
            ####pwm.ChangeDutyCycle(dc)
            pwm.value = dc
            ####GPIO.output(ledPin, GPIO.LOW)
            led.off()
        else: # button is pressed:
            ####pwm.ChangeDutyCycle(100-dc)
            led.value = 1-dc
            ####GPIO.output(ledPin, GPIO.HIGH)
            led.on()
            time.sleep(0.075)
            ####GPIO.output(ledPin, GPIO.LOW)
            led.off()
            time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    ####pwm.stop() # stop PWM
    ####GPIO.cleanup() # cleanup all GPIO
    exit(0)