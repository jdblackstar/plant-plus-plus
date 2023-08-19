import time

import board
import neopixel


class LED:
    def __init__(self, pin, num_leds):
        """
        Initialize the LED strip with the given parameters.

        Args:
            pin (board pin): Pin to which the LED strip is connected.
            num_leds (int): Number of LEDs in the strip.
        """
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
        """
        Initialize the NeoPixel LED strip with the given parameters.

        Args:
            pin (board pin): Pin to which the LED strip is connected.
            num_leds (int): Number of LEDs in the strip.
        """
        super().__init__(pin, num_leds)
        self.pixels = neopixel.NeoPixel(pin, num_leds)

    def turn_on(self, color=(255, 255, 255)):
        """
        Turn on the LED strip.

        Args:
            color (tuple): RGB color tuple.
        """
        for i in range(self.num_leds):
            self.pixels[i] = color  # White color

        # could also just do this, I think - gotta test it
        # self.pixels.fill((255, 255, 255))

    def turn_off(self):
        """
        Turn off the LED strip.

        Args:
            color (tuple): RGB color tuple.
        """
        for i in range(self.num_leds):
            self.pixels[i] = (0, 0, 0)  # Off

        # could also just do this, I think - gotta test it
        # self.pixels.fill((0, 0, 0))

    def set_color(self, color):
        """
        Set the color of the LED strip.

        Args:
            color (tuple): RGB color tuple.
        """
        for i in range(self.num_leds):
            self.pixels[i] = color

        # could also just do this, I think - gotta test it
        # self.pixels.fill(color)

    def transition_color(self, start_color, end_color, duration):
        """
        Transition the color of the LED strip from start_color to end_color over the given duration.

        Args:
            start_color (tuple): RGB color tuple.
            end_color (tuple): RGB color tuple.
            duration (float): Duration of the transition in seconds.
        """
        steps = 100
        delay = duration / steps

        for step in range(steps + 1):
            ratio = step / steps
            color = (
                int(start_color[0] + (end_color[0] - start_color[0]) * ratio),
                int(start_color[1] + (end_color[1] - start_color[1]) * ratio),
                int(start_color[2] + (end_color[2] - start_color[2]) * ratio),
            )

            start_time = time.time()
            self.set_color(color)
            elapsed_time = time.time() - start_time

            adjusted_delay = max(0, delay - elapsed_time)
            time.sleep(adjusted_delay)
