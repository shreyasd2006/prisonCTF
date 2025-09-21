Fix the following Python code so that it correctly checks if a string is a palindrome.

def is_palindrome(s):
  for i in range(len(s)):
    if s[i] != s[len(s)-i]:
    return False
  return True
print(is_palindrome("racecar")) # should return True
print(is_palindrome("hello'")) # should return False