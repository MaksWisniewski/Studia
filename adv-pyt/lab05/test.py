import unittest, logic



class Testing(unittest.TestCase):
    def test_top(self):
        self.assertEqual(str(logic.Top()), "\U00002ADF")
        self.assertTrue(logic.Top().isTautology())

    def test_bot(self):
        self.assertEqual(str(logic.Bot()), "\U00002AE0")
        self.assertFalse(logic.Bot().isTautology())

    def test_negation(self):
        self.assertEqual(str(logic.Negation(logic.Top())), "¬⫟")
        self.assertTrue(logic.Negation(logic.Bot()).isTautology())
        self.assertFalse(logic.Negation(logic.Top()).eval({}))

    def test_conjunction(self):
        self.assertEqual(str(logic.Conjunction(logic.Top(), logic.Bot())), "(⫟∧⫠)")
        self.assertTrue(logic.Conjunction(logic.Top(), logic.Top()).eval({}))
        self.assertFalse(logic.Conjunction(logic.Bot(), logic.Bot()).isTautology())

    def test_disjunction(self):
        self.assertEqual(str(logic.Disjunction(logic.Top(), logic.Bot())), "(⫟∨⫠)")
        self.assertFalse(logic.Disjunction(logic.Bot(), logic.Bot()).eval({}))
        self.assertTrue(logic.Disjunction(logic.Top(), logic.Bot()).isTautology())

    def test_variable(self):
        self.assertEqual(str(logic.Variable("a")), "a")

    def test_implication(self):
        #self.assertEqual(logic.Implication(logic.Variable("b"), logic.Top()), "(b → ⫟)")
        self.assertTrue(logic.Implication(logic.Bot(), logic.Top()).isTautology())
        self.assertFalse(logic.Implication(logic.Top(), logic.Bot()).eval({}))

    def test_equiv(self):
        self.assertTrue( logic.Equivalence(logic.Top(), logic.Top() ).eval({}))
        self.assertFalse(logic.Equivalence(logic.Top(), logic.Bot() ).eval({}))

    def test_tautologies(self):
        x = logic.Disjunction(logic.Variable("p"), logic.Negation(logic.Variable("p")))
        self.assertTrue(x.isTautology())

    def test_2(self):
        y = logic.Disjunction(
            logic.Conjunction(logic.Variable("A"), logic.Variable("B")), 
            logic.Conjunction(logic.Variable("B"), logic.Negation(logic.Variable("C"))))
        self.assertFalse(y.isTautology())
        self.assertTrue(logic.Disjunction(logic.Top(), y).isTautology())

    def test_3(self):
        x = logic.Top()
        for i in range(1, 15):
            x = logic.Disjunction(x, logic.Variable(str(i)))
        self.assertTrue(x.isTautology())

    def test_3(self):
        x = logic.Bot()
        for i in range(1, 17):
            x = logic.Conjunction(x, logic.Variable("x_"+str(i)))
        self.assertFalse(x.isTautology())



if __name__ == "__main__":
    unittest.main()