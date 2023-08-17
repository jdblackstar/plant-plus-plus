from smbus2 import SMBus


class LightSensor:
    """Abstract base class for light sensors."""

    def read_lux(self):
        raise NotImplementedError("This method should be overridden by a subclass")


class BH1750Sensor(LightSensor):
    """Class for the BH1750 light sensor."""

    ADDRESS = 0x23
    COMMAND = 0x10

    def read_lux(self):
        with SMBus(1) as bus:
            lux_data = bus.read_i2c_block_data(self.ADDRESS, self.COMMAND, 2)
            lux = (lux_data[0] << 8 | lux_data[1]) / 1.2
            return lux * 0.0929


class TSL2561Sensor(LightSensor):
    """Class for the TSL2561 light sensor."""

    # We aren't implementing this sensor yet, so nothing to put here

    def read_lux(self):
        pass
