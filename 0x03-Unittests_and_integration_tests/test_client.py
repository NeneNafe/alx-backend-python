#!/usr/bin/env python3
""" Parameterize and patch as decorators """


import requests
from unittest import TestCase, mock
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


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
