import unittest
import subprocess

class TestQ3(unittest.TestCase):
    def run_solution(self, inp: str):
        r = subprocess.run(["python3", "solution.py"], input=inp.encode(), stdout=subprocess.PIPE)
        lines = r.stdout.decode().strip().splitlines()
        if lines == ['']:
            return []
        return lines

    def assertListEqualIgnoreOrder(self, list1, list2):
        """Helper to assert two lists of strings are equal ignoring order"""
        self.assertEqual(set(list1), set(list2))

    def test_samples(self):
        inp = "5\n1 2 3 2 4\n4\n"
        self.assertListEqualIgnoreOrder(self.run_solution(inp), ["0 2", "1 3"])

    def test_hidden(self):
        inp = "6\n3 3 4 7 5 2\n10\n"
        self.assertListEqualIgnoreOrder(self.run_solution(inp), ["1 3", "2 4"])
        
        inp = "4\n0 0 0 0\n0\n"
        self.assertListEqualIgnoreOrder(self.run_solution(inp),
            ["0 1", "0 2", "0 3", "1 2", "1 3", "2 3"])
        
        inp = "5\n-1 -2 -3 -4 -5\n-8\n"
        self.assertListEqualIgnoreOrder(self.run_solution(inp), ["2 4"])

if __name__ == "__main__":
    unittest.main()
