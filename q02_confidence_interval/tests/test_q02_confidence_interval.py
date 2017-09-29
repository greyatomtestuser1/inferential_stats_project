from unittest import TestCase
from q02_confidence_interval.build import confidence_interval

class TestConfidence_interval(TestCase):
    def test_confidence_interval(self):
        low, high = confidence_interval()
        self.assertAlmostEqual(low, 1487.2898780257296, 2)
        self.assertAlmostEqual(high, 1564.9341219742705, 2)
