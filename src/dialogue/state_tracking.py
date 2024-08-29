class DialogueStateTracker:
    def __init__(self):
        self.state = {}

    def update_state(self, key, value):
        self.state[key] = value

    def get_state(self):
        return self.state

if __name__ == "__main__":
    tracker = DialogueStateTracker()
    tracker.update_state('intent', 'greeting')
    print(tracker.get_state())
