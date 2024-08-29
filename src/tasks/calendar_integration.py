from datetime import datetime

class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

if __name__ == "__main__":
    calendar = Calendar()
    event = Event('Meeting', datetime.now())
    calendar.add_event(event)
    print(calendar.get_events())
