import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from q01_cond_prob.build import cond_prob

class TestCond_prob(TestCase):
    def test_cond_prob(self):
        prob = cond_prob()
        self.assertAlmostEqual(prob, 0.00045232831351218984)
