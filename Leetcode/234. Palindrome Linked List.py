# Given the head of a singly linked list, return true if it is a palindrome.
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        return True if a == a[::-1] else False
