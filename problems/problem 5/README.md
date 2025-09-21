Description:
Encode a string using these rules:
• Vowels → shift forward by 3 in ASCII.
• Consonants → shift forward by 1.
• Digits → reverse the entire digit sequence.
• Other characters → remain unchanged.

Input Format:
• A single string s.

Output Format:
• The encoded string.

Constraints:
• 1 ≤ len(s) ≤ 10^5
• Contains letters, digits, and symbols.

Sample:
Input: hello123
Output: igopt321