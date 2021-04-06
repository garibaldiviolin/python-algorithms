from algorithms.list_searches import binary_search

from tests.timed_tests import TimedTestCase


class BinarySearchTestCase(TimedTestCase):
    def setUp(self):
        return super().setUp()

    def test_binary_search_with_small_list(self):
        small_list = [number for number in range(10, 20)]
        self.assertEqual(binary_search(small_list, 16), 6)

    def test_binary_search_with_huge_list(self):
        huge_list = [number for number in range(1_000_000, 2_000_000)]
        self.assertEqual(binary_search(huge_list, 1_937_500), 937_500)
