import maproulette
import unittest
from tests.sample_data import test_geojson, test_overpassQL_query
from unittest.mock import patch


class TestChallengeAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.Challenge(config)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_by_id(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_by_id(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_statistics_by_id(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_statistics_by_id(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_tasks(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_tasks(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_create_challenge(self, mock_request, api_instance=api):
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        mock_request.return_value.status_code = '200'
        response = api_instance.create_challenge(test_challenge_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_add_tasks_to_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12978'
        mock_request.return_value.status_code = '200'
        response = api_instance.add_tasks_to_challenge(test_geojson, test_challenge_id)
        self.assertEqual(response['status'], '200')