"""
Maksymilian Wiśniewskii. Lab 5, task 2

"""
import logic_exception as errs

if __name__ == "__main__":
    pass

class Formula:
    # function getVars reccursively checks the formula and 'pattern match' against all classses that inherit from the class formula.
    # returns set containing strings 
    def getVars(self, SET=set()):
        pass

    def isTautology(self):
        # brute force method, iterating all possible valuations of variables using bitmasks.

        variables = self.getVars()

        Upper_bitmask = int(2**len(variables))

        for current_bitmask in range(0, Upper_bitmask+1, 1):
            
            valuation = {}
            pos = 0
            for var in variables:
                valuation[var] = current_bitmask & (1<<pos)
                pos += 1
            
            if not self.eval(valuation):
                return False
        
        return True    

class Top(Formula):
    def __str__(self):
        return "\U00002ADF"

    def eval(self, valuation):
        return True

    # no new introduction to set
    def getVars(self, SET=set()):
        return SET

class Bot(Formula):
    def __str__(self):
        return "\U00002AE0"

    def eval(self, valuation):
        return False

    # no new introduction to set
    def getVars(self, SET=set()):
        return SET


class Variable(Formula):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id

    # if variable was not found, throw and exception
    def eval(self, valuation):
        if not self.id in valuation:
            raise errs.ExceptionUnknownVariable(self.id)
        return valuation[self.id]

    # introduce new variable
    def getVars(self, SET=set()):
        SET.add(self.id)
        return SET

class Negation(Formula):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return f"\U000000AC{self.expr}"

    def eval(self, valuation):
        return not self.expr.eval(valuation)
    
    # pretty much self explanatory, according to the structure of class add new variables
    def getVars(self, SET=set()):
        return self.expr.getVars(SET)

class Conjunction(Formula):
    def __init__(self, left, right):
        self.left  = left
        self.right = right
    
    def __str__(self):
        return f"({self.left}\U00002227{self.right})"

    def eval(self, valuation):
        return self.left.eval(valuation) and self.right.eval(valuation)
    
    def getVars(self, SET=set()):
        return self.left.getVars(SET).union(self.right.getVars(SET))

class Disjunction(Formula):
    def __init__(self, left, right):
        self.left  = left
        self.right = right
    
    def __str__(self):
        return f"({self.left}\U00002228{self.right})"

    def eval(self, valuation):
        return self.left.eval(valuation) or self.right.eval(valuation)

    def getVars(self, SET=set()):
        return self.left.getVars(SET).union(self.right.getVars(SET))

class Implication(Formula):
    def __init__(self, left, right):
        self.left  = left
        self.right = right

    def __str__(self):
        return f"({self.left} \U00002192 {self.right})"

    def eval(self, valuation):
        return not (self.left.eval(valuation) and not self.right.eval(valuation))

    def getVars(self, SET=set()):
        return self.left.getVars(SET).union(self.right.getVars(SET))

class Equivalence(Formula):
    def __init__(self, left, right):
        self.left  = left
        self.right = right

    def __str__(self):
        return f"({self.left}\U00002194{self.right})"

    def eval(self, valuation):
        return self.left.eval(valuation) == self.right.eval(valuation)

    def getVars(self, SET=set()):
        return self.left.getVars(SET).union(self.right.getVars(SET))