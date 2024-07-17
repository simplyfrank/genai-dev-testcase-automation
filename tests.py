import unittest
from app import app
from database import get_historical_consumption

class TestAPI(unittest.TestCase):

    def test_predict_consumption(self):
        with app.test_client() as client:
            response = client.get('/predict/consumption/product-A')
            self.assertEqual(response.status_code, 200)
            # Add more assertions for the response data
    def test_get_historical_consumption(self):
        data = get_historical_consumption('product-B')
        self.assertIsInstance(data, list)
        # Add more assertions for the retrieved data


    def test_predict_consumption_json_response(self):
        with app.test_client() as client:
            response = client.get('/predict/consumption/product-A')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, dict)

if __name__ == '__main__':
    unittest.main()
