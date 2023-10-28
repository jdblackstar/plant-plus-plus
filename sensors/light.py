import utime as time

try:
    from machine import I2C, Pin
except ImportError:
    from mock_machine import I2C, Pin


class LightSensor():
    """Abstract base class for light sensors."""

    def initialize(self):
        """Initialize the sensor."""
        pass

    def power_on(self):
        """Power on the sensor."""
        pass

    def power_off(self):
        """Power off the sensor."""
        pass

    def reset(self):
        """Reset the sensor to default settings."""
        pass

    def read_lux(self, mode=None):
        """Read lux value from the sensor."""
        pass

    def set_measurement_time(self, high_bits=None, low_bits=None):
        """Set the measurement time for the sensor (if applicable)."""
        pass

    # Add other methods as needed


class BH1750Sensor(LightSensor):
    """
    Class for the BH1750 light sensor.
    """

    ADDRESS = 0x23
    POWER_DOWN = 0x00
    POWER_ON = 0x01
    RESET = 0x07
    CONTINUOUS_HIGH_RES = 0x10
    CONTINUOUS_HIGH_RES_MODE2 = 0x11
    CONTINUOUS_LOW_RES = 0x13
    ONE_TIME_HIGH_RES = 0x20
    ONE_TIME_HIGH_RES_MODE2 = 0x21
    ONE_TIME_LOW_RES = 0x23

    def __init__(self):
        self.i2c = I2C(0, scl=Pin(21), sda=Pin(20))  # adjust to your I2C pins

    def initialize(self):
        self.power_on()
        self.reset()

    def power_on(self):
        self.i2c.writeto(self.ADDRESS, bytes([self.POWER_ON]))

    def power_off(self):
        self.i2c.writeto(self.ADDRESS, bytes([self.POWER_DOWN]))

    def reset(self):
        self.i2c.writeto(self.ADDRESS, bytes([self.RESET]))

    def read_lux(self, mode=CONTINUOUS_HIGH_RES):
        self.i2c.writeto(self.ADDRESS, bytes([mode]))
        time.sleep_ms(
            24 if mode in (self.CONTINUOUS_HIGH_RES, self.ONE_TIME_HIGH_RES) else 16
        )
        data = self.i2c.readfrom(self.ADDRESS, 2)
        return ((data[0] << 8) | data[1]) / 1.2

    def set_measurement_time(self, high_bits=None, low_bits=None):
        # This sensor does not support setting measurement time
        pass


class TSL2561Sensor(LightSensor):
    """
    Class for the TSL2561 light sensor.
    """

    # We aren't implementing this sensor yet, so nothing to put here

    def read_lux(self):
        pass
