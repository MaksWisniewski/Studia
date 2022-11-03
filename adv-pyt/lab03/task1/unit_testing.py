import unittest, solution


class Testing(unittest.TestCase):
    def test_primes_imperative(self):
        self.assertEqual(solution.primes_imperative(0), [])
        self.assertEqual(solution.primes_imperative(1), [])
        self.assertEqual(solution.primes_imperative(2), [2])
        self.assertEqual(solution.primes_imperative(5), [2, 3, 5])
        self.assertEqual(solution.primes_imperative(6), [2, 3, 5])
        self.assertEqual(solution.primes_imperative(7), [2, 3, 5, 7])

    def test_primes(self):
        self.assertEqual(solution.primes(0), [])
        self.assertEqual(solution.primes(1), [])
        self.assertEqual(solution.primes(2), [2])
        self.assertEqual(solution.primes(5), [2, 3, 5])
        self.assertEqual(solution.primes(6), [2, 3, 5])
        self.assertEqual(solution.primes(7), [2, 3, 5, 7])

    def test_fun(self):
        self.assertEqual(solution.filter_primes(0), [])
        self.assertEqual(solution.filter_primes(1), [])
        self.assertEqual(solution.filter_primes(2), [2])
        self.assertEqual(solution.filter_primes(5), [2, 3, 5])
        self.assertEqual(solution.filter_primes(6), [2, 3, 5])
        self.assertEqual(solution.filter_primes(7), [2, 3, 5, 7])

    def test_small(self):
        for i in range(1, 1000, 50):
            a = solution.primes_imperative(i)
            b = solution.primes(i)
            c = solution.filter_primes(i)
            self.assertEqual(a, b)
            self.assertEqual(b, c)

    def test_big(self):
        for i in range(100, 10000, 500):
            a = solution.primes_imperative(i)
            b = solution.primes(i)
            c = solution.filter_primes(i)
            self.assertEqual(a, b)
            self.assertEqual(b, c)


if __name__ == "__main__":
    unittest.main()
