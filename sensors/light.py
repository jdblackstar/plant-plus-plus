import time
from abc import ABC, abstractmethod

from loguru import logger
from smbus2 import SMBus


class LightSensor(ABC):
    """Abstract base class for light sensors."""

    @abstractmethod
    def initialize(self):
        """Initialize the sensor."""
        pass

    @abstractmethod
    def power_on(self):
        """Power on the sensor."""
        pass

    @abstractmethod
    def power_off(self):
        """Power off the sensor."""
        pass

    @abstractmethod
    def reset(self):
        """Reset the sensor to default settings."""
        pass

    @abstractmethod
    def read_lux(self, mode=None):
        """Read lux value from the sensor."""
        pass

    @abstractmethod
    def set_measurement_time(self, high_bits=None, low_bits=None):
        """Set the measurement time for the sensor (if applicable)."""
        pass

    # Add other methods as needed


class BH1750Sensor(LightSensor):
    """
    Class for the BH1750 light sensor.

    datasheet URL: https://www.mouser.com/datasheet/2/348/bh1750fvi-e-186247.pdf
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

    def initialize(self):
        """
        Initialize the sensor.
        
        Note: This method should be called before any other methods.
        """
        try:
            self.power_on()
            self.reset()
        except Exception as e:
            logger.error(f"An error occurred while initializing the sensor: {e}")

    def power_on(self):
        """
        Power on the sensor.
        """
        try:
            with SMBus(1) as bus:
                bus.write_byte(self.ADDRESS, self.POWER_ON)
        except Exception as e:
            logger.error(f"An error occurred while powering on the sensor: {e}")

    def power_off(self):
        """Power off the sensor."""
        try:
            with SMBus(1) as bus:
                bus.write_byte(self.ADDRESS, self.POWER_DOWN)
        except Exception as e:
            logger.error(f"An error occurred while powering off the sensor: {e}")

    def reset(self):
        """Reset the sensor to default settings."""
        try:
            with SMBus(1) as bus:
                bus.write_byte(self.ADDRESS, self.RESET)
        except Exception as e:
            logger.error(f"An error occurred while resetting the sensor: {e}")

    def read_lux(self, mode=CONTINUOUS_HIGH_RES):
        """Read lux value from the sensor."""
        try:
            with SMBus(1) as bus:
                bus.write_byte(self.ADDRESS, mode)
                sleep_time = 0.16 if mode == self.CONTINUOUS_LOW_RES else 0.12
                time.sleep(sleep_time)
                lux_data = bus.read_i2c_block_data(self.ADDRESS, mode, 2)
                lux = (lux_data[0] << 8 | lux_data[1]) / 1.2
                return lux
        except Exception as e:
            logger.error(f"An error occurred while reading lux from the sensor: {e}")
            return None

    def set_measurement_time(self, high_bits, low_bits):
        """Set the measurement time for the sensor."""
        try:
            with SMBus(1) as bus:
                bus.write_byte(self.ADDRESS, 0b01000000 | high_bits)  # High bits
                bus.write_byte(self.ADDRESS, 0b01100000 | low_bits)  # Low bits
        except Exception as e:
            logger.error(f"An error occurred while setting the measurement time: {e}")


class TSL2561Sensor(LightSensor):
    """Class for the TSL2561 light sensor."""

    # We aren't implementing this sensor yet, so nothing to put here

    def read_lux(self):
        pass
