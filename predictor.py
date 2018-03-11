from functools import reduce

from generator import Generator
from math import gcd
import gmpy2


class Predictor:

    # predictor does not know generator's parameters (seed, a, c, m)
    def __init__(self, gen: Generator):
        self.gen = gen

    def predict_next(self):
        results = self.gen.next_N(10)

        diffs = list(self.get_diffs(results))

        # d2*d0 = a*d1 * d0 = a*a*d0*d0
        # d1*d1 = a*d0 * a*d0 = a*a*d0*d0
        # ...
        zeroes = list(self.get_zeros(diffs))

        # each number on the list mod m = 0
        # 0 = zeroes[0] mod m = k0 * m
        # 0 = zeroes[1] mod m = k1 * m
        # ...
        m = reduce(gcd, zeroes)

        # print(m)

        a = gmpy2.divm(diffs[1], diffs[0], m)

        b = (results[1] - results[0]* a) % m
        #
        # print(a)
        #
        # print(b)

        prediction = (a*results[len(results)-1] + b)%m

        return prediction

    def get_diffs(self, results):
        for i in range(1, len(results)):
            yield results[i] - results[i-1]


    def get_zeros(self, diffs):
        for i in range(2, len(diffs)):
            yield diffs[i]*diffs[i-2] - diffs[i-1]*diffs[i-1]

