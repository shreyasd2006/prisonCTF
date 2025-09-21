#Update this code. 

def is_palindrome(s):
  for i in range(len(s)):
    if s[i] != s[len(s)-i]:
     return False
  return True
if __name__ == "__main__":
    s = input().strip()
    print(is_palindrome(s))
