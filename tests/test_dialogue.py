import unittest
from src.dialogue.state_tracking import DialogueStateTracker
from src.dialogue.policy_learning import PolicyLearning
from src.dialogue.response_generation import generate_response

class TestDialogue(unittest.TestCase):
    def test_dialogue_state_tracker(self):
        tracker = DialogueStateTracker()
        tracker.update_state('intent', 'greeting')
        state = tracker.get_state()
        self.assertIsNotNone(state)

    def test_policy_learning(self):
        actions = ['greet', 'ask_question', 'provide_info']
        policy = PolicyLearning(actions)
        state = 'initial'
        action = policy.choose_action(state)
        self.assertIsNotNone(action)

    def test_generate_response(self):
        input_text = "Hello, how are you?"
        response = generate_response(input_text)
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
