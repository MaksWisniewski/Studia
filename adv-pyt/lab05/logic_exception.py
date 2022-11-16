"""
Class ExceptionUnknownVariable
    throws an excetion when variable value is not set.
    (i.e not found in dictionary).
"""

class ExceptionUnknownVariable(Exception):
    def __init__(self, x):
        self.id = x

    def __str__(self):
        return f'Value of: {self.id} is not set'

