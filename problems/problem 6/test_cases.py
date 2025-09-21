import unittest, subprocess

class TestQ6(unittest.TestCase):
    def run_solution(self, inp: str) -> str:
        r = subprocess.run(["python3", "solution.py"], input=inp.encode(), stdout=subprocess.PIPE)
        return r.stdout.decode().strip()

    def test_hidden(self):
        self.assertEqual(self.run_solution("madam\n"), "True")
        self.assertEqual(self.run_solution("abba\n"), "True")
        self.assertEqual(self.run_solution("abc\n"), "False")

if __name__ == "__main__":
    unittest.main()
