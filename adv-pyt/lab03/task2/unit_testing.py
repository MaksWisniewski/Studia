import unittest, solution


class Testing(unittest.TestCase):
    def test_imperative(self):
        self.assertEqual(solution.perfect_imper(5), [])
        self.assertEqual(solution.perfect_imper(6), [])
        self.assertEqual(solution.perfect_imper(7), [6])

    def test_listComprehension(self):
        self.assertEqual(solution.perfect(5), [])
        self.assertEqual(solution.perfect(6), [])
        self.assertEqual(solution.perfect(7), [6])

    def test_functionalApproach(self):
        self.assertEqual(solution.perfect_fun(5), [])
        self.assertEqual(solution.perfect_fun(6), [])
        self.assertEqual(solution.perfect_fun(7), [6])

    def test_small(self):
        for i in range(1, 101, 10):
            a = solution.perfect_imper(i)
            b = solution.perfect(i)
            c = solution.perfect_fun(i)
            self.assertEqual(a, b)
            self.assertEqual(b, c)
            self.assertEqual(a, c)

    def test_big(self):
        for i in range(100, 2000, 200):
            a = solution.perfect_imper(i)
            b = solution.perfect(i)
            c = solution.perfect_fun(i)
            self.assertEqual(a, b)
            self.assertEqual(b, c)
            self.assertEqual(a, c)


if __name__ == "__main__":
    unittest.main()
