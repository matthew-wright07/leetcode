class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_string = str(x)[::-1]
        if reverse_string==str(x):
            return True
        else:
            return False