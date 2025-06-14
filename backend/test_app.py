import unittest
from app import suma

class TestApp(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3, 4), 7)

if __name__ == '__main__':
    unittest.main()
