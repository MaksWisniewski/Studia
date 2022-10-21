import unittest
import main, string, random

class TestCalc(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEqual(main.common_prefix(["", "", "", ""]), "")
        self.assertEqual(main.common_prefix(["r", "ro", "rob", "robert"]), "r")
        self.assertEqual(main.common_prefix(["aasfalt", "aarbitraż", "aaa", "aaaa"]), "aa")
        self.assertEqual(main.common_prefix(["max", "max2", "ma"]), "ma")
        self.assertEqual(main.common_prefix(["żołądż", "żołądż patryk"]), "żołądż")

    def test_find(self):
        self.assertEqual(main.Find(["", "", "", ""]), "")
        self.assertEqual(main.Find(["r", "ro", "rob", "robert"]), "r")
        self.assertEqual(main.Find(["aasfalt", "aarbitraż", "aaa", "aaaa"]), "aa")
        self.assertEqual(main.Find(["max", "max2", "ma"]), "ma")
        self.assertEqual(main.Find(["żołądż", "żołądż patryk"]), "żołądż")

    # i guess that test below works, but i havent't figured out the way how to invoke that method, and it also gives wild output
    """
    def huge_test(self);
        for i in range(5, 30):
            x = []
            for j in range(1, 30):
                x.append(''.join(random.choices(string.ascii_lowercase, k=i)))
                self.assertEqual(main.Find(x), main.common_prefix(x))
    """

if __name__ == '__main__':
    unittest.main()
    