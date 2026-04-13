import json
import os
import unittest

"""
    TESTS
"""

class TestSearchCities(unittest.TestCase):
    """
    Kata 4 - Search functionality

    Implement a city search functionality. The function takes a string (search text) as input
    and returns the found cities which corresponds to the search text.

    Prerequisites:

    Create a collection of strings that will act as a database for the city names.
    City names: Paris, Budapest, Skopje, Rotterdam, Valencia, Vancouver, Amsterdam, Vienna, Sydney,
    New York City, London, Bangkok, Hong Kong, Dubai, Rome, Istanbul.

    Requirements:

    1. If the search text is fewer than 2 characters, then should return no results.
    (It is an optimization feature of the search functionality.)

    2. If the search text is equal to or more than 2 characters, then it should return all the city
    names starting with the exact search text.
    For example for search text "Va", the function should return Valencia and Vancouver.

    3. The search functionality should be case insensitive.

    4. The search functionality should work also when the search text is just a part of a city name
    For example "ape" should return "Budapest" city.

    5. If the search text is a "*" (asterisk), then it should return all the city names.
    """

    @classmethod
    def setUpClass(cls):
        # Load cities from JSON file
        cities_file_path = os.path.join(os.path.dirname(__file__), "cities.json")
        with open(cities_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            cities = data["cities"]

        cls.test_data = [
            # Requirement 1: < 2 characters should return no results
            {"input": "", "output": []},
            {"input": "a", "output": []},
            # Requirement 2: >= 2 characters should return cities starting with search text
            {"input": "Va", "output": ["Valencia", "Vancouver"]},
            {"input": "Pa", "output": ["Paris"]},
            # Requirement 3: Case insensitive search
            {"input": "va", "output": ["Valencia", "Vancouver"]},
            {"input": "PARIS", "output": ["Paris"]},
            {"input": "NeW", "output": ["New York City"]},
            # Requirement 4: Search text as part of city name (substring search)
            {"input": "ape", "output": ["Budapest"]},
            {"input": "ster", "output": ["Amsterdam"]},
            {"input": "kok", "output": ["Bangkok"]},
            {"input": "dam", "output": ["Rotterdam", "Amsterdam"]},
            # Requirement 5: Asterisk should return all cities
            {"input": "*", "output": cities},
            # Edge cases
            {"input": "xyz", "output": []},
        ]

    def test_search_cities(self):
        """
        Tests the search_cities function with various inputs and expected outputs.
        """
        for x in self.test_data:
            with self.subTest(input=x["input"], output=x["output"]):
                self.assertEqual(search_cities(x["input"]), x["output"])



"""
    METODO
"""

def search_cities(str_to_search):
    """
    Kata 4 - Search functionality

    Implement a city search functionality. The function takes a string (search text) as input
    and returns the found cities which corresponds to the search text.

    Prerequisites:

    Create a collection of strings that will act as a database for the city names.
    City names: Paris, Budapest, Skopje, Rotterdam, Valencia, Vancouver, Amsterdam, Vienna, Sydney,
    New York City, London, Bangkok, Hong Kong, Dubai, Rome, Istanbul.

    Requirements:

    1. If the search text is fewer than 2 characters, then should return no results.
    (It is an optimization feature of the search functionality.)

    2. If the search text is equal to or more than 2 characters, then it should return all the city
    names starting with the exact search text.
    For example for search text "Va", the function should return Valencia and Vancouver.

    3. The search functionality should be case insensitive.

    4. The search functionality should work also when the search text is just a part of a city name
    For example "ape" should return "Budapest" city.

    5. If the search text is a "*" (asterisk), then it should return all the city names.
    """
    # Load cities from JSON file
    cities_file_path = os.path.join(os.path.dirname(__file__), "cities.json")
    with open(cities_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        cities = data["cities"]

    cities_found = []

    # Requirement 5: If search text is "*", return all cities
    if str_to_search == "*":
        return cities

    # Requirement 1: If search text is fewer than 2 characters, return no results
    if len(str_to_search) < 2:
        return cities_found

    # Convert search text to lowercase for case-insensitive search (Requirement 3)
    search_lower = str_to_search.lower()

    for city in cities:
        city_lower = city.lower()
        # Requirement 2: Cities starting with search text
        # Requirement 4: Cities containing search text (substring search)
        if city_lower.startswith(search_lower) or search_lower in city_lower:
            cities_found.append(city)

    return cities_found
