#Update this code.

def is_anagram(s1, s2):
  return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s = input().strip().split()
    if len(s) != 2:
        print("False")
    else:
        a, b = s
        print(is_anagram(a, b))