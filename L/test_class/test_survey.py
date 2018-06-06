import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """测试AnonymousSurvey类"""

    def setUp(self):
        question = 'What ...'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Japanese', 'Spanish']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])

        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()