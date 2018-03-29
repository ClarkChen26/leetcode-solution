#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.36%)
# Total Accepted:    386.3K
# Total Submissions: 1.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# Input: 123
# Output:  321
# Example 2:
# 
# Input: -123
# Output: -321
# 
# 
# 
# Example 3:
# 
# Input: 120
# Output: 21
# 
# 
# 
# Note:
# Assume we are dealing with an environment which could only hold integers
# within the 32-bit signed integer range. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.
# 
#
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        num = list(str(x))

        if num[0] == "-":
            num.remove('-')
            num.reverse()
            num_s = ("-" + ''.join(num))
        else:
            num.reverse()
            num_s = ''.join(num)
        result = int(num_s)
        if result > 2147483647 or result < -2147483648:
            return 0
        return result

        #数学方法
        # curr = x
        # result = 0
        # if x < 0:
        #     curr *= -1
        # while curr != 0:
        #     a = curr % 10
        #     curr = curr // 10
        #     result = result * 10 + a
        
        # if x < 0:
        #     result *= -1
        # if result > 2147483647 or result < -2147483648:
        #     return 0
        # return result

# s = Solution()
# print(s.reverse(-123))
