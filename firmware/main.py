from machine import Pin
import machine

speaker = machine.PWM(Pin(21))
button = Pin(0, Pin.IN)

speaker.freq(0)
speaker.duty(512)

while True:
    if (button.value() == 1):
        speaker.freq(500)
    else:
        speaker.freq(0)

    sleep(5)
