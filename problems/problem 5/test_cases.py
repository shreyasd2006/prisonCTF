import unittest, subprocess

class TestQ5(unittest.TestCase):
    def run_solution(self, inp: str) -> str:
        r = subprocess.run(["python3", "solution.py"], input=inp.encode(), stdout=subprocess.PIPE)
        return r.stdout.decode().strip()

    def test_samples(self):
        self.assertEqual(self.run_solution("hello123\n"), "igopt321")

    def test_hidden(self):
        self.assertEqual(self.run_solution("programming2025!\n"), "qsphsbnnjoh5202!")
        self.assertEqual(self.run_solution("AeiOu\n"), "DhpRx")
        self.assertEqual(self.run_solution("testCASE123\n"), "uftuDBTF321")

if __name__ == "__main__":
    unittest.main()
