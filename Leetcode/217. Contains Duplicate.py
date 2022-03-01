# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check=set()
        for i in nums:
            if i not in check:
                check.add(i)
            else: return True
        return False
        
        # 2nd Solution
        #dic = {}
        # for i in range(len(nums)) : 
        #     temp = dic.get(nums[i],2)
        #     if temp != 2 :
        #         return True
        #     dic[nums[i]] = 1
        # return False
            
        
