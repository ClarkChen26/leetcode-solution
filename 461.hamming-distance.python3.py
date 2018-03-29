#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (69.58%)
# Total Accepted:    145.2K
# Total Submissions: 208.6K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 231.
# 
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are
# different.
# 
# 
#
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        A = bin(x).replace('b','')
        B = bin(y).replace('b','')

        while len(A) != len(B):
            if len(A) > len(B):
                B = ("0" + B)
            else:
                A = ("0" + A)

        # print(A)
        # print(B)

        result = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                result += 1
        return result
        
# s = Solution()
# print(s.hammingDistance(3,1))