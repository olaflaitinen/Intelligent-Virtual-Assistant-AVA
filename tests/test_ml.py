import unittest
from src.ml.model_training import train_model
from src.ml.model_evaluation import evaluate_model
from src.ml.hyperparameter_tuning import tune_hyperparameters

class TestML(unittest.TestCase):
    def test_train_model(self):
        data = [[1, 2], [3, 4], [5, 6], [7, 8]]
        labels = [0, 1, 0, 1]
        model, accuracy = train_model(data, labels)
        self.assertIsNotNone(model)

    def test_evaluate_model(self):
        data = [[1, 2], [3, 4], [5, 6], [7, 8]]
        labels = [0, 1, 0, 1]
        model, _ = train_model(data, labels)
        report = evaluate_model(model, data, labels)
        self.assertIsNotNone(report)

    def test_tune_hyperparameters(self):
        data = [[1, 2], [3, 4], [5, 6], [7, 8]]
        labels = [0, 1, 0, 1]
        best_params = tune_hyperparameters(data, labels)
        self.assertIsNotNone(best_params)

if __name__ == '__main__':
    unittest.main()
