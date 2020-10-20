from time import sleep
import RPi.GPIO as GPIO
from channel_conf import ChannelConfig

OFF = True
ON = False


# To test the value of a pin use the .input method
# channel_is_on = GPIO.input(channel)  # Returns 0 if OFF or 1 if ON

class Sprinkler:
    config = ChannelConfig()

    def __init__(self):
        channels = self.config.get_channels()
        for channel in channels:
            # log overall view
            print("channel " + str(channel.get('number'))
                  + " = " + str(self.config.get_pin_from_channel(channel.get('number'))))
            Sprinkler.setup_gpio(int(channel.get('gpio')))


    @staticmethod
    def setup_gpio(pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, True)

    def off(self, channel):
        pin = self.config.get_pin_from_channel(channel)
        sleep(2)
        GPIO.output(pin, True)

    def on(self, channel):
        pin = self.config.get_pin_from_channel(channel)
        sleep(2)
        GPIO.output(pin, False)

    @staticmethod
    def cleanup():
        GPIO.cleanup()

    @staticmethod
    def get_state(pin):
        return GPIO.input(int(pin))  # Returns 0 if ON or 1 if OFF


if __name__ == '__main__':
    sprinkler = Sprinkler()
