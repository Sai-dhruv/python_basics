import unittest

class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('Set up executted ...!')

    def test_method_1(self):
        print('Test method executted')

    def test_method_2(self):
        print('Test Method 2 executted..!')    

    def tearDown(self):
        print('tearDown Method executted ')

unittest.main()                