#!/usr/bin/env python3
"""A function that tests a function if it works accordingly"""


from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


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