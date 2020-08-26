class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        if int(str(x)[::-1]) == x:
            return True
        else:
            return False
