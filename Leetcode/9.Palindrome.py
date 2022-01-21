# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):

        self.y = y = 0
        self.z = x
        
        while (x > 0):
            y = (y*10) + (x%10)
            x = x//10
        return self.z == y
        
        
# Second Solution by using converting
# return str(x)[::-1]==str(x)
