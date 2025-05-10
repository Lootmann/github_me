import sys
import unittest

sys.path.append("../src")
from src import list_sum


class TestListSum(unittest.TestCase):
    def test_list_sum(self):
        lst = [1, 2, 3, 4, 5]
        want = sum(lst)
        got = list_sum.list_sum(lst)
        self.assertTrue(want, got)


if __name__ == "__main__":
    unittest.main()
