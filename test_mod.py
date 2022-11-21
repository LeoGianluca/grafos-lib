import unittest

import src.mod as module


class Testing(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(module.soma(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
