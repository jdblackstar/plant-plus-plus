import time

import board
import neopixel


class LED:
    def __init__(self, pin, num_leds):
        self.pin = pin
        self.num_leds = num_leds

    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def set_color(self, color):
        pass


class NeoPixelLED(LED):
    def __init__(self, pin, num_leds):
        super().__init__(pin, num_leds)
        self.pixels = neopixel.NeoPixel(pin, num_leds)

    def turn_on(self):
        for i in range(self.num_leds):
            self.pixels[i] = (255, 255, 255)  # White color

    def turn_off(self):
        for i in range(self.num_leds):
            self.pixels[i] = (0, 0, 0)  # Off

    def set_color(self, color):
        for i in range(self.num_leds):
            self.pixels[i] = color

    def transition_color(self, start_color, end_color, duration):
        steps = 100
        delay = duration / steps

        for step in range(steps + 1):
            ratio = step / steps
            color = (
                int(start_color[0] + (end_color[0] - start_color[0]) * ratio),
                int(start_color[1] + (end_color[1] - start_color[1]) * ratio),
                int(start_color[2] + (end_color[2] - start_color[2]) * ratio),
            )

            self.set_color(color)
            time.sleep(delay)
