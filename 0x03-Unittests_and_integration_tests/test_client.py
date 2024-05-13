#!/usr/bin/env python3
""" Parameterize and patch as decorators """


import requests
from unittest import TestCase, mock
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import utils
import client


class TestGithubOrgClient(TestCase):
    """ Implements the test_org method """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, result, get_patch):
        """Test for the GithubOrgClient"""
        get_patch.return_value = result
        actual_output = GithubOrgClient(org)
        self.assertEqual(actual_output.org, result)
        get_patch.assert_called_once_with("https://api.github.com/orgs/"+org)

    def test_public_repos_url(self):
        """unit-test GithubOrgClient._public_repos_url"""
        output = "www.yes.com"
        payload = {"repos_url": output}
        get_mock = 'client.GithubOrgClient.org'
        with patch(get_mock, PropertyMock(return_value=payload)):
            client = GithubOrgClient("x")
            self.assertEqual(client._public_repos_url, output)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ unit-test GithubOrgClient.public_repos """
        nene = {"name": "Nene", "license": {"key": "a"}}
        hope = {"name": "Hope", "license": {"key": "b"}}
        vann = {"name": "Vann"}
        get_mock = 'client.GithubOrgClient._public_repos_url'
        mock_get_json.return_value = [nene, hope, vann]
        with patch(get_mock, PropertyMock(return_value="www.yes.com")) as i:
            actual = GithubOrgClient("x")
            self.assertEqual(actual.public_repos(), ['Nene', 'Hope', 'Vann'])
            self.assertEqual(actual.public_repos("a"), ['Nene'])
            self.assertEqual(actual.public_repos("c"), [])
            self.assertEqual(actual.public_repos(45), [])
            mock_get_json.assert_called_once_with("www.yes.com")
            i.assert_called_once_with()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expect_output):
        """ unit-test GithubOrgClient.has_license """
        self.assertEqual(GithubOrgClient.has_license(repo, license),
                         expect_output)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """ implement the setUpClass and tearDownClass """

    @classmethod
    def setUpClass(cls):
        """ mock requests.get to return example """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        mock_org = Mock()
        mock_org.json = Mock(return_value=org)
        cls.mock_org = mock_org
        mock_repos = Mock()
        mock_repos.json = Mock(return_value=repos)

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: mock_repos}
        cls.get.side_effect = lambda y: options.get(y, mock_org)

    @classmethod
    def tearDownClass(cls):
        """ Stop the patcher """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test the public repos """
        actual = GithubOrgClient("x")
        self.assertEqual(actual.org, self.org_payload)
        self.assertEqual(actual.repos_payload, self.repos_payload)
        self.assertEqual(actual.public_repos(), self.expected_repos)
        self.assertEqual(actual.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self):
        """ test the public_repos """

        actual = GithubOrgClient("x")
        self.assertEqual(actual.org, self.org_payload)
        self.assertEqual(actual.repos_payload, self.repos_payload)
        self.assertEqual(actual.public_repos(), self.expected_repos)
        self.assertEqual(actual.public_repos("NONEXISTENT"), [])
        self.assertEqual(actual.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])
