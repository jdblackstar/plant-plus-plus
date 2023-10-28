class I2C:
    def __init__(self, scl, sda):
        pass

    def writeto(self, address, data):
        pass

    def readfrom(self, address, size):
        return bytes([0] * size)

class Pin:
    def __init__(self, pin):
        pass