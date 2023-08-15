import json
import time
from datetime import datetime, timedelta
from suntime import Sun
import RPi.GPIO as GPIO
from sensors.light import BH1750Sensor
from plants.plant import Plant
from utils.factory import create_sensor

# Constants
LATITUDE = 37.7749  # Example latitude (change to your location)
LONGITUDE = -122.4194  # Example longitude (change to your location)
LED_PIN = 18
CONFIG_FILE = "config/settings.json"
PLANT_CONFIG_FILE = "plants/plant_config.json"

# Function to load configuration
def load_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to load plant configuration
def load_plant_config(file_path, plant_type):
    with open(file_path, 'r') as file:
        plant_data = json.load(file)
        return plant_data[plant_type]

# Set up the LED pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Load general configuration
config = load_config(CONFIG_FILE)

# Create the light sensor object based on configuration
light_sensor = create_sensor(config["sensor_type"])

# Load plant configuration
plant = Plant(**load_plant_config(PLANT_CONFIG_FILE, config["plant_type"]))

# Calculate sunrise and sunset times
sun = Sun(LATITUDE, LONGITUDE)
sunrise = sun.get_sunrise_time()
sunset = sun.get_sunset_time()
mid_day = sunrise + (sunset - sunrise) / 2

# Main loop
accumulated_foot_candles = 0
while True:
    current_time = datetime.now()

    # If it's a new day, reset the accumulated foot-candles
    if current_time > sunrise and current_time < sunrise + timedelta(minutes=10):
        accumulated_foot_candles = 0

    # If it's mid-day, evaluate the need for supplemental light
    if current_time > mid_day and current_time < mid_day + timedelta(minutes=10):
        if accumulated_foot_candles < plant.foot_candle_hours * 0.3:
            GPIO.output(LED_PIN, True)
        else:
            GPIO.output(LED_PIN, False)
            accumulated_foot_candles = plant.foot_candle_hours

    # Record and accumulate the current foot-candles
    current_foot_candles = light_sensor.read_foot_candles()
    accumulated_foot_candles += current_foot_candles

    # Sleep for a minute (adjust as needed)
    time.sleep(60)

# Clean up the GPIO
GPIO.cleanup()
