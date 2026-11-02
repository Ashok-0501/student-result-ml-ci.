import json
import os
import unittest

import joblib
import pandas as pd

from train_model import FEATURES


class TestMLPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not os.path.exists("student_result_model.pkl") or not os.path.exists("metrics.json"):
            raise RuntimeError("Run train_model.py before the ML tests.")

    def test_dataset_created(self):
        self.assertTrue(os.path.exists("student_results.csv"))

    def test_model_created(self):
        self.assertTrue(os.path.exists("student_result_model.pkl"))

    def test_metrics_created(self):
        self.assertTrue(os.path.exists("metrics.json"))

    def test_accuracy_is_valid(self):
        with open("metrics.json", "r", encoding="utf-8") as file:
            accuracy = json.load(file)["accuracy"]
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

    def test_model_prediction(self):
        model = joblib.load("student_result_model.pkl")
        sample = pd.DataFrame([{
            "attendance": 85, "internal_marks": 75,
            "assignment_marks": 80, "previous_score": 78,
        }])[FEATURES]
        self.assertIn(int(model.predict(sample)[0]), [0, 1])

    def test_high_performance_student(self):
        model = joblib.load("student_result_model.pkl")
        sample = pd.DataFrame([{
            "attendance": 90, "internal_marks": 85,
            "assignment_marks": 88, "previous_score": 80,
        }])[FEATURES]
        self.assertEqual(int(model.predict(sample)[0]), 1)

    def test_low_performance_student(self):
        model = joblib.load("student_result_model.pkl")
        sample = pd.DataFrame([{
            "attendance": 55, "internal_marks": 30,
            "assignment_marks": 40, "previous_score": 35,
        }])[FEATURES]
        self.assertEqual(int(model.predict(sample)[0]), 0)


if __name__ == "__main__":
    unittest.main()
