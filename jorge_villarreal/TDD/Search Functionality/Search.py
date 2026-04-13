"""
    TESTS
"""
import json
import unittest
from ddt import ddt, data, unpack


@ddt
class TestCitySearch(unittest.TestCase):

    # Req 1: fewer than 2 chars → no results
    @data(
        ("",),
        ("V",),
        ("a",),
        ("1",),
    )
    @unpack
    def test_fewer_than_2_chars_returns_no_results(self, text):
        self.assertEqual(search_cities(text), [])

    # Req 2: 2+ chars → cities that contain the search text (prefix counts)
    @data(
        ("Va", ["Valencia", "Vancouver"]),
        ("Rom", ["Rome"]),
        ("Par", ["Paris"]),
        ("Xy",  []),
    )
    @unpack
    def test_prefix_match(self, text, expected):
        result = search_cities(text)
        self.assertEqual(sorted(result), sorted(expected))

    # Req 3: case insensitive
    @data(
        ("va",  ["Valencia", "Vancouver"]),
        ("VA",  ["Valencia", "Vancouver"]),
        ("Va",  ["Valencia", "Vancouver"]),
        ("par", ["Paris"]),
        ("PAR", ["Paris"]),
    )
    @unpack
    def test_case_insensitive(self, text, expected):
        result = search_cities(text)
        self.assertEqual(sorted(result), sorted(expected))

    # Req 4: partial match anywhere in the city name
    @data(
        ("ape", "Budapest"),
        ("ong", "Hong Kong"),
        ("kok", "Bangkok"),
        ("dam", "Amsterdam"),
        ("dam", "Rotterdam"),
    )
    @unpack
    def test_partial_match_contains_city(self, text, expected_city):
        self.assertIn(expected_city, search_cities(text))

    # Req 5: * returns all cities
    @data(
        ("*", 16),
    )
    @unpack
    def test_asterisk_returns_all_cities(self, text, expected_count):
        result = search_cities(text)
        self.assertEqual(len(result), expected_count)
        for city in CITIES:
            self.assertIn(city, result)


"""
    METODO
"""
import os

_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_dir, "cities.json"), encoding="utf-8") as _f:
    CITIES = json.load(_f)


def search_cities(text: str) -> list:
    if text == "*":
        return list(CITIES)

    if len(text) < 2:
        return []

    query = text.lower()
    return [city for city in CITIES if query in city.lower()]


if __name__ == "__main__":
    unittest.main()
