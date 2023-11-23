import unittest
import requests
from os import getenv

class Task1TestCase(unittest.TestCase):
    STAGING_URL = f"http://{getenv('STAGING_IP')}"

    # def setUp(self):
        # self.response = requests.get(url=self.STAGING_URL)

    def test_200_respons(self):
        response = requests.get(url=self.STAGING_URL)
        self.assertEqual(response.status_code, 200)
    
    def test_your_name_displayed(self):
        response = requests.get(url=self.STAGING_URL)
        self.assertIn(getenv('YOUR_NAME'), response.text)


if __name__ == "__main__":
	unittest.main()