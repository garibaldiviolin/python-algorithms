from algorithms.workers_abilities import (
    calculate_minimum_days,
    calculate_minimum_days_optimized,
)

from tests.timed_tests import TimedTestCase


class CalculateMinimumDaysTestCase(TimedTestCase):
    def setUp(self):
        return super().setUp()

    def test_calculate_with_small_input_minimum_days(self):
        self.assertEquals(
            calculate_minimum_days([1, 1, 2, 3, 5], 12),
            4
        )

    def test_calculate_with_small_input_exhausted(self):
        self.assertEquals(
            calculate_minimum_days([1, 1, 2, 3, 5], 17),
            9
        )

    def test_calculate_with_medium_input_minimum_days(self):
        self.assertEquals(
            calculate_minimum_days(
                [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
                244
            ),
            44
        )

    def test_calculate_with_big_input_minimum_days(self):
        big_list = [number for number in range(0, 30_000, 2)]
        self.assertEquals(
            calculate_minimum_days(big_list, 2_989_900),
            100
        )

    def test_calculate_with_big_input_exhausted(self):
        big_list = [number for number in range(0, 30_000, 2)]
        self.assertEquals(
            calculate_minimum_days(
                big_list,
                449_867_748
            ),
            208_616
        )


class CalculateMinimumDaysOptimizedTestCase(TimedTestCase):
    def setUp(self):
        return super().setUp()

    def test_calculate_with_small_input_minimum_days(self):
        self.assertEquals(
            calculate_minimum_days_optimized([1, 1, 2, 3, 5], 12),
            4
        )

    def test_calculate_with_small_input_exhausted(self):
        self.assertEquals(
            calculate_minimum_days_optimized([1, 1, 2, 3, 5], 17),
            9
        )

    def test_calculate_with_medium_input_minimum_days(self):
        self.assertEquals(
            calculate_minimum_days_optimized(
                [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
                244
            ),
            44
        )

    def test_calculate_with_big_input_minimum_days(self):
        big_list = [number for number in range(0, 30_000, 2)]
        self.assertEquals(
            calculate_minimum_days_optimized(big_list, 2_989_900),
            100
        )

    def test_calculate_with_big_input_exhausted(self):
        big_list = [number for number in range(0, 30_000, 2)]
        self.assertEquals(
            calculate_minimum_days_optimized(
                big_list,
                449_867_748
            ),
            208_616
        )
