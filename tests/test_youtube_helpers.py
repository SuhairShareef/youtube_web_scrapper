import json
from unittest import TestCase

from helpers import transpose_comments


class TestYouTubeHelpers(TestCase):
    def setUp(self) -> None:
        with open("comments_examples.json") as json_mock_data_file:
            self.comment = json.load(json_mock_data_file)

    def test_transpose_comments(self):
        response = transpose_comments(self.comment)

        expected_response = {
           "comment_id": "UgzOpYaC4oojL5mdg0V4AaABAg",
           "text": "Is there a way to use the API Key to run the query?\nI would like to run this from an AWS Lambda "
                   "Function so a key would work best",
           "likes": 0,
           "replies": 1,
        }

        self.assertEqual(response, expected_response)
