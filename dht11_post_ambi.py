import RPi.GPIO as GPIO
import dht11
import time
import datetime
import ambient

# ご自分のチャネルID、ライトキーに置き換えてください
ambi = ambient.Ambient(2607, "fca0d37c61f9dc95")

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 4)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

        r = ambi.send({"d3": result.temperature, "d4": result.humidity})

    time.sleep(5)
