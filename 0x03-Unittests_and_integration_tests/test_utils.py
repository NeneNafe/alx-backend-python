#!/usr/bin/env python3
"""A function that tests a function if it works accordingly"""


from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """a class that inherits from the unittest"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_outcome):
        """tests that the method returns what it's supposed to"""
        actual_outcome = access_nested_map(nested_map, path)
        self.assertEqual(actual_outcome, expected_outcome)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expctd_msg):
        """test that a KeyError is raised for the following inputs"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(expctd_msg, context.exception)


class TestGetJson(TestCase):
    """implement the TestGetJson.test_get_json method to test
    that utils.get_json returns the expected result"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """returns a Mock object with a json method that returns test_payload
        which you parametrize alongside the test_url"""

        # Mock the return value of requests.get
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            # Call the get_json function
            actual_response = get_json(test_url)
            # Assert that the actual_response is equal to test_payload
            self.assertEqual(actual_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    """implement test_memoize method"""

    def test_memoize(self):
        """ Tests the memoized function"""

        class TestClass:
            """ Test Class """

            def a_method(self):
                """ Returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ return a memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            actual_return = test_class.a_property
            actual_return = test_class.a_property

            self.assertEqual(actual_return, 42)
            patched.assert_called_once()
