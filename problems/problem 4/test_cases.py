import unittest, subprocess

class TestQ4(unittest.TestCase):
    def run_solution(self, inp: str) -> str:
        r = subprocess.run(["python3", "solution.py"], input=inp.encode(), stdout=subprocess.PIPE)
        return r.stdout.decode().strip()

    def test_samples(self):
        inp = "3 3\n1 2 3\n4 5 6\n7 8 9\n"
        self.assertEqual(self.run_solution(inp), "29")

    def test_hidden(self):
        self.assertEqual(self.run_solution("2 2\n-1 2\n1 3\n"), "4")
        self.assertEqual(self.run_solution("3 4\n1 2 3 4\n2 2 1 1\n5 1 1 1\n"), "11")
        self.assertEqual(self.run_solution("4 4\n1 1 1 1\n1 1 1 1\n1 1 1 1\n1 1 1 9\n"), "15")

if __name__ == "__main__":
    unittest.main()
