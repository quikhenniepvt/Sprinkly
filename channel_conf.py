import json


class ChannelConfig:
    data = []

    def __init__(self):
        self.load()

    def get_pin_from_channel(self, channel_num):
        for channel in self.data:
            if channel["number"] == str(channel_num):
                return int(channel.get('gpio'))
        return -1

    def load(self):
        print("loading...")
        with open('channel_conf.json') as json_file:
            jsn = json.load(json_file)
            self.data = jsn["channels"]

    def get_channel(self, channel_num):
        for channel in self.data:
            if channel["number"] == channel_num:
                return channel
        return {}

    def get_channels(self):
        return self.data

    def set_channel(self, channel_num, gpio_pin, description, def_minutes):
        found = False
        for channel in self.data:
            print("Comparing "+channel["number"] + " with " + channel_num)
            if channel["number"] == channel_num:
                channel["gpio"] = gpio_pin
                channel["description"] = description
                channel["def_minutes"] = def_minutes
                found = True
        if not found:
            print("setting channel " + channel_num)
            channel = {}
            if gpio_pin is not None:
                channel["number"] = channel_num
                channel["gpio"] = gpio_pin
                channel["description"] = description
                channel["def_minutes"] = def_minutes
                self.data.append(channel)

    def save(self):
        print(self.data)
        channels = {"channels": self.data}
        with open("channel_conf.json", "w") as outfile:
            json.dump(channels, outfile, indent=4)
