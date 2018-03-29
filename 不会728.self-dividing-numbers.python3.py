#
# [728] Self Dividing Numbers
#
# https://leetcode.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (66.83%)
# Total Accepted:    27.9K
# Total Submissions: 41.8K
# Testcase Example:  '1\n22'
#
# 
# A self-dividing number is a number that is divisible by every digit it
# contains.
# 
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 ==
# 0, and 128 % 8 == 0.
# 
# Also, a self-dividing number is not allowed to contain the digit zero.
# 
# Given a lower and upper number bound, output a list of every possible self
# dividing number, including the bounds if possible.
# 
# Example 1:
# 
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# 
# 
# 
# Note:
# The boundaries of each input argument are 1 .
# 
#
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        n = right - left
        x = 10
        y = 0
        num_list = []
        for _ in range(n):
            num_list.append(left)
            left += 1
        num_list.append(right)
        selfdividlist = []
        for num in num_list:
            while num != 0:
                (num//x^y) % 10
                y += 1
            selfdividlist.append(num)
        return selfdividlist



s = Solution()
print(s.selfDividingNumbers(1, 22))
            
