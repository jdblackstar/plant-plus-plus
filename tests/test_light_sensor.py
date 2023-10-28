from sensors.light import BH1750Sensor


def test_bh1750():
    sensor = BH1750Sensor()

    print("Initializing the sensor...")
    sensor.initialize()

    print("Powering on the sensor...")
    sensor.power_on()

    print("Reading lux value...")
    lux = sensor.read_lux()
    print(f"Lux value: {lux}")

    print("Powering off the sensor...")
    sensor.power_off()


def main():
    test_bh1750()


if __name__ == "__main__":
    main()
