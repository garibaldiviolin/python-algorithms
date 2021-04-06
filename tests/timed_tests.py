from unittest import TestCase

from time import monotonic


class TimedTestCase(TestCase):
    def setUp(self):
        self.start_time = monotonic()

    def tearDown(self):
        t = monotonic() - self.start_time
        print(f"{t:.10f}")
