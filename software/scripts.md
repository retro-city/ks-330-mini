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


