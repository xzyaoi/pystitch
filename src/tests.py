import unittest
from pystitch import warmUp

class TestWarmUpFunction(unittest.TestCase):
    def test_warmUp(self):
        warmUp()

if __name__ == '__main__':
    unittest.main()