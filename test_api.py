import unittest
import requests

class TestDiceAPI(unittest.TestCase):
    def test_api_roll_success(self):
        url = "http://127.0.0.1:8081/roll_dice"
        payload = {
            "probabilities": [0.1, 0.1, 0.1, 0.1, 0.1, 0.5],
            "number_of_random": 3
        }
        response = requests.post(url, json=payload)
        
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(len(data["results"]), 3)

if __name__ == '__main__':
    unittest.main()