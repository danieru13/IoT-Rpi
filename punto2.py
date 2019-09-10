from gpiozero import Button
import time

# ISR
def my_callback():
  print('You pressed the button')

btn = Button(18)

# Asociando la funcion handler al evento de interrupcion 
# (cambio en estado del boton (de alto a bajo) presionado)
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