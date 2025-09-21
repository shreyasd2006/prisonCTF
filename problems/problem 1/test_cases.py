import unittest, subprocess

class TestQ1(unittest.TestCase):
    def run_solution(self, inp: str) -> str:
        r = subprocess.run(["python3", "solution.py"], input=inp.encode(), stdout=subprocess.PIPE)
        return r.stdout.decode().strip()

    def test_samples(self):
        self.assertEqual(self.run_solution("leetcode\n"), "l")
        self.assertEqual(self.run_solution("aabb\n"), "None")

    def test_hidden(self):
        self.assertEqual(self.run_solution("abcabcde\n"), "d")
        self.assertEqual(self.run_solution("aabbccddeeff\n"), "None")
        self.assertEqual(self.run_solution("swiss\n"), "w")

if __name__ == "__main__":
    unittest.main()
