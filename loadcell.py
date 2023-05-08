import RPi.GPIO as GPIO
from hx711 import HX711
import time

GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=5, pd_sck_pin=6)

hx.zero()

input('Place known weight on scale & press Enter: ')
reading = hx.get_data_mean(readings=150)

known_weight_grams = input('Enter the known weight in grams and press Enter: ')
value = float(known_weight_grams)

threshold = input('Enter in weight threshold for Trash notifcation in grams and press Enter: ')
threshold = float(threshold)

ratio = reading/value
hx.set_scale_ratio(ratio)

while True:
    weight = hx.get_weight_mean()
    if weight >= 0:
        if weight >= threshold:
            print("Take out the Trash!!")
            time.sleep(2)
            input('Press Enter after replacing bag: ')
        elif weight > 1:
            print('There are {:.2f} grams amount of trash.'.format(weight))
        else:
            print('There is no trash in here')
            
    else:
        print('There is no trash in here.')