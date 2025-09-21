Description:
Fix the following Python code so that it correctly checks if two strings are anagrams.

def is_anagram(s1, s2):
  return sorted(s1) == sorted(s2)

print(is_anagram("listen","silent")) # True
print(is_anagram("listen","silentt")) # should be False, but returns True