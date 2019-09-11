from gpiozero import Button, LED
from picamera import PiCamera
from datetime import datetime
from time import sleep
from signal import pause

button = Button(2)
led = LED(23)
camera = PiCamera()


def capture():
    i = 1
    while i<6:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
        i+=1
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/IoT-Rpi/%s.jpg' % timestamp, use_video_port=True)
    print("fotografia tomada")

button.when_pressed = capture
      

pause()
