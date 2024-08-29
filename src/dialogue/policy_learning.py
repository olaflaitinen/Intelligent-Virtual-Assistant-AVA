import numpy as np

class PolicyLearning:
    def __init__(self, actions):
        self.actions = actions
        self.q_table = {}

    def choose_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(len(self.actions))
        self.q_table[state][action] += reward

if __name__ == "__main__":
    actions = ['greet', 'ask_question', 'provide_info']
    policy = PolicyLearning(actions)
    state = 'initial'
    action = policy.choose_action(state)
    print(f"Chosen action: {actions[action]}")
