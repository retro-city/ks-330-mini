LED and Button Input/Output:


### Enable HDD LED:
```
sudo nano /boot/config.txt
```

Add the following `dtoverlay`
```
dtoverlay=act-led,gpio=17
```

### Turbo Button and LED:

```python
import RPi.GPIO as GPIO

# Use BCM-style pin referencing
GPIO.setmode(GPIO.BCM)

# Activate Turbo LED
GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.HIGH)

# Activate Turbo Button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create a Toggle Function
def toggle_turbo(channel):
    turbo = not GPIO.input(27)
    if (turbo):
            GPIO.output(27, GPIO.HIGH)
    else:
            GPIO.output(27, GPIO.LOW)

# Add Event which runs the toggle function
GPIO.add_event_detect(23, GPIO.RISING, callback=toggle_turbo)
```


## 7 segment

https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf
https://pypi.org/project/spidev/
https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all


```
 sudo apt-get install python3-pip


import time, spidev
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 8000000

spi.xfer2([0x0C, 0x01]) # turn on
spi.xfer2([0x09, 0x00]) # decode mode none
spi.xfer2([0x0B, 0xFF]) # set intensity

spi.xfer2([0x0F, 0x00]) # turn off displaytest
spi.xfer2([0x0F, 0x01]) # turn on displaytest

# 0x30 left digit, 0x40 right digit, 0x60 both

def init():
    spi.xfer2([0x0C, 0x01]) # turn on
    spi.xfer2([0x09, 0x00]) # decode mode none
    spi.xfer2([0x0B, 0xFF]) # set intensity
    spi.xfer2([0x0F, 0x00]) # turn off displaytest


# 66
def d66():
    spi.xfer2([0x01, 0x60])
    spi.xfer2([0x02, 0x00])
    spi.xfer2([0x03, 0x60])
    spi.xfer2([0x04, 0x60])
    spi.xfer2([0x05, 0x60])
    spi.xfer2([0x06, 0x60])
    spi.xfer2([0x07, 0x60])
    spi.xfer2([0x08, 0x00])

# 33
def d33():
    spi.xfer2([0x01, 0xFF])
    spi.xfer2([0x02, 0xFF])
    spi.xfer2([0x03, 0xFF])
    spi.xfer2([0x04, 0xFF])
    spi.xfer2([0x05, 0x00])
    spi.xfer2([0x06, 0x00])
    spi.xfer2([0x07, 0xFF])
    spi.xfer2([0x08, 0x00])


# Blank
def Blank():
    spi.xfer2([0x01, 0x00])
    spi.xfer2([0x02, 0x00])
    spi.xfer2([0x03, 0x00])
    spi.xfer2([0x04, 0x00])
    spi.xfer2([0x05, 0x00])
    spi.xfer2([0x06, 0x00])
    spi.xfer2([0x07, 0x00])
    spi.xfer2([0x08, 0x00])


# Pi
def Pi():
    spi.xfer2([0x01, 0x30])
    spi.xfer2([0x02, 0x30])
    spi.xfer2([0x03, 0x00])
    spi.xfer2([0x04, 0x00])
    spi.xfer2([0x05, 0xFF])
    spi.xfer2([0x06, 0xFF])
    spi.xfer2([0x07, 0x30])
    spi.xfer2([0x08, 0x00])


# Hi
def Hi():
    spi.xfer2([0x01, 0x00])
    spi.xfer2([0x02, 0x30])
    spi.xfer2([0x03, 0x30])
    spi.xfer2([0x04, 0x00])
    spi.xfer2([0x05, 0x60])
    spi.xfer2([0x06, 0x60])
    spi.xfer2([0x07, 0x30])
    spi.xfer2([0x08, 0x00])


# Lo
def Lo():
    spi.xfer2([0x01, 0x00])
    spi.xfer2([0x02, 0x00])
    spi.xfer2([0x03, 0x40])
    spi.xfer2([0x04, 0x60])
    spi.xfer2([0x05, 0x60])
    spi.xfer2([0x06, 0x30])
    spi.xfer2([0x07, 0x40])
    spi.xfer2([0x08, 0x00])

```