import unittest, subprocess

class TestQ2(unittest.TestCase):
    def run_solution(self, inp: str) -> str:
        r = subprocess.run(["python3", "solution.py"], input=inp.encode(), stdout=subprocess.PIPE)
        return r.stdout.decode().strip()

    def test_samples(self):
        inp = "3\nflower\nflow\nflight\n"
        self.assertEqual(self.run_solution(inp), "fl")
        inp = "3\ndog\nracecar\ncar\n"
        self.assertEqual(self.run_solution(inp), "")

    def test_hidden(self):
        inp = "4\ninterspecies\ninterstellar\ninterstate\ninternet\n"
        self.assertEqual(self.run_solution(inp), "inter")
        inp = "2\nabcd\nabc\n"
        self.assertEqual(self.run_solution(inp), "abc")

if __name__ == "__main__":
    unittest.main()
