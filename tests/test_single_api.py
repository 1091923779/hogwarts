import os

import unittest

from hogwarts_httprunner.loader import load_yaml

class TestSingleApi(unittest.TestCase):

    def test_loader_single_api(self):

        single_api_yaml = os.path.join(
            os.path.dirname(__file__), "api", "get_homepage.yml")
        result = run_yaml(single_api_yaml)
        self.assertEqual(result, True)