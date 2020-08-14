#!/usr/bin/python
import os, time, spidev
import RPi.GPIO as GPIO
spi = spidev.SpiDev()

# Create a Toggle Function
def toggle_turbo(channel):
    turbo = not GPIO.input(27)
    if (turbo):
            GPIO.output(27, GPIO.HIGH)
            d66()
    else:
            GPIO.output(27, GPIO.LOW)
            d33()

def toggle_reset(channel):
    print("reset pressed")
    os.system("killall dosbox")

def d66():
    spi.xfer2([0x01, 0b01011111])
    spi.xfer2([0x02, 0b01011111])

def d33():
    spi.xfer2([0x01, 0b01111001])
    spi.xfer2([0x02, 0b01111001])

def dhi():
    spi.xfer2([0x01, 0b00000110])
    spi.xfer2([0x02, 0b00110111])

def dlo():
    spi.xfer2([0x01, 0b00011101])
    spi.xfer2([0x02, 0b00001110])

def drc():
    spi.xfer2([0x01, 0b01001110])
    spi.xfer2([0x02, 0b00000101])

def dpi():
    spi.xfer2([0x01, 0b00000110])
    spi.xfer2([0x02, 0b01100111])

if __name__ == "__main__":
    # Init GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27,GPIO.HIGH)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Turbo
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Reset

    # Init 7SEG
    spi.open(0,0)
    spi.max_speed_hz = 8000000
    spi.xfer2([0x0C, 0x01]) # turn on
    spi.xfer2([0x09, 0x00]) # decode mode none
    spi.xfer2([0x0B, 0x11]) # set intensity
    spi.xfer2([0x0F, 0x00]) # turn off displaytest
    d66()

    # Add events
    GPIO.add_event_detect(23, GPIO.RISING, callback=toggle_turbo)
    GPIO.add_event_detect(24, GPIO.RISING, callback=toggle_reset)

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        GPIO.cleanup()

