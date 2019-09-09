####import RPi.GPIO as GPIO
from gpiozero import Button
import time

GPIO.setmode(GPIO.BCM)

# ISR
def my_callback():
  print('You pressed the button')

####GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
btn = Button(18)

# Asociando la funcion handler al evento de interrupcion 
# (cambio en estado del boton (de alto a bajo) presionado)
####GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback)
btn.when_pressed = my_callback

try:
  i = 0
  while True:
    i = i + 1
    print(i)
    time.sleep(1)
finally:
  print("Cleaning Up!")
  exit(0)  
  ####GPIO.cleanup()