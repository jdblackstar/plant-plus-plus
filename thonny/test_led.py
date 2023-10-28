from controllers.led import NeoPixelLED
import time


def test_neopixel():
    led = NeoPixelLED()

    # methods to test
    # turn_on(color)
    # turn_off()
    # set_color(color)
    # transition_color(start_color, end_color, duration)

    print("Testing the turn_on method...")
    try:
        led.turn_on()
        print("LED should be on.")
    except:
        print("LED failed to turn on.")
    time.sleep(5)

    print("Testing the turn_off method...")
    try:
        led.turn_off()
        print("LED should be off.")
    except:
        print("LED failed to turn off.")
    time.slee(5)

    print("Testing the set_color method...")
    try:
        led.set_color((255, 192, 203))
        print("The LED should transition to pink")
    except:
        print("LED failed to change color.")

    print("Testing the transition_color method...")
    try:
        led.transition_color((128, 0, 128), (255, 255, 0), 3)
        time.sleep(3)
        print("LED should transition from purple to yellow over 5 seconds")
    except:
        print("LED failed to transition colors")


def main():
    test_neopixel()


if __name__ == "__main__":
    main()
