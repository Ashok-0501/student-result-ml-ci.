import unittest

from fastapi.testclient import TestClient
from deployment.fastapi.app import app


class TestFastAPIService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")

    def test_prediction(self):
        response = self.client.post("/predict", json={
            "attendance": 90,
            "internal_marks": 85,
            "assignment_marks": 88,
            "previous_score": 80,
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json()["prediction"], ["PASS", "FAIL"])
        self.assertIn("X-Request-ID", response.headers)

    def test_invalid_input_is_rejected(self):
        response = self.client.post("/predict", json={
            "attendance": 150,
            "internal_marks": 85,
            "assignment_marks": 88,
            "previous_score": 80,
        })
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
