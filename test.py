import unittest
from main import list_flattener

class Test01(unittest.TestCase):
    def test_flattener(self):
        '''
        Here we'll test the list_flattener function with 2 equal elements
        '''
        data = [[1], [[1], [2]], [2]]
        result = list_flattener(data)
        self.assertEqual(result, [1, 1, 2, 2])

class Tes02(unittest.TestCase):
    def test_flattener(self):
        '''
        Here we'll test the list_flattener function with multiple different elements
        '''
        data = [[1], [[2], [3]], [[[[4], [5], [6]]]]]
        result = list_flattener(data)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])