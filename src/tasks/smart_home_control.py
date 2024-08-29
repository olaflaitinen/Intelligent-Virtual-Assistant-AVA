class SmartHomeDevice:
    def __init__(self, name):
        self.name = name
        self.state = 'off'

    def turn_on(self):
        self.state = 'on'
        print(f"{self.name} is turned on.")

    def turn_off(self):
        self.state = 'off'
        print(f"{self.name} is turned off.")

if __name__ == "__main__":
    device = SmartHomeDevice('Light')
    device.turn_on()
    device.turn_off()
