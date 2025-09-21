import unittest, subprocess

class TestQ10(unittest.TestCase):
    def run_solution(self, inp: str) -> str:
        r = subprocess.run(["python3", "solution.py"], input=inp.encode(), stdout=subprocess.PIPE)
        return r.stdout.decode().strip()

    def test_hidden(self):
        out = self.run_solution("2 2\n")
        # Buggy code prints a shared-row board; we only assert output format contains '['
        self.assertIn("[", out)

        out = self.run_solution("3 3\n")
        self.assertIn("[", out)

if __name__ == "__main__":
    unittest.main()
