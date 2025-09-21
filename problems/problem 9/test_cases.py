import unittest, subprocess

class TestQ9(unittest.TestCase):
    def run_solution(self, inp: str) -> str:
        r = subprocess.run(["python3", "solution.py"], input=inp.encode(), stdout=subprocess.PIPE)
        return r.stdout.decode().strip()

    def test_hidden(self):
        out = self.run_solution("alice\n")
        self.assertIn("alice", out)
        out = self.run_solution("bob\n")
        self.assertIn("bob", out)
        out = self.run_solution("' OR '1'='1\n")
        self.assertNotIn("alice", out)

if __name__ == "__main__":
    unittest.main()
