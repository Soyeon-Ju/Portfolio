# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        if 'IV' in s: 
            answer += 4
            s = s.replace('IV', '00')        
        if 'IX' in s: 
            answer += 9
            s = s.replace('IX', '00')   
        if 'XL' in s: 
            answer += 40
            s = s.replace('XL', '00')   
        if 'XC' in s: 
            answer += 90
            s = s.replace('XC', '00')   
        if 'CD' in s: 
            answer += 400
            s = s.replace('CD', '00')   
        if 'CM' in s: 
            answer += 900
            s = s.replace('CM', '00')   
        
        a = []
        a[:0] = s
        for i in range(len(a)):
            if a[i] == 'I': answer +=1
            elif a[i] == 'V': answer +=5
            elif a[i] == 'X' : answer +=10
            elif a[i] == 'L': answer += 50
            elif a[i] == 'C' : answer +=100
            elif a[i] == 'D': answer +=500
            elif a[i] == 'M': answer +=1000

        return answer
            
