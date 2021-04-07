from algorithms.list_searches import binary_search

from tests.timed_tests import TimedTestCase


class BinarySearchTestCase(TimedTestCase):
    def setUp(self):
        return super().setUp()

    def test_binary_search_with_small_list(self):
        small_list = [number for number in range(10, 20)]

        tests = [(number, number - 10) for number in small_list]
        tests += [
            (0, -1),
            (1, -1),
            (9, -1),
            (20, -1),
        ]

        for number, expected_return in tests:
            with self.subTest(number=number, expected_return=expected_return):
                self.assertEqual(
                    binary_search(small_list, number),
                    expected_return,
                )

    def test_binary_search_with_huge_list(self):
        huge_list = [number for number in range(1_000_000, 2_000_000)]
        self.assertEqual(binary_search(huge_list, 1_937_500), 937_500)
