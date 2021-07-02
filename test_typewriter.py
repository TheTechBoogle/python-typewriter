from unittest import TestCase
from typewriter import typewriter

'''
   Unit test for the typewriter function
   No editing of this file or it would not function as normal. 
'''

class Test(TestCase):
    def test_typewriter(self):
        S = "1 2 4 - 4 + 5 - + 7 - DUP 7 - POP"
        assert typewriter(S) == 5

    def test_typewriter2(self):
        S = "1 3 2 3 4 - 6 DUP"
        assert typewriter(S) == 6
