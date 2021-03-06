#
# [762] Find Anagram Mappings
#
# https://leetcode.com/problems/find-anagram-mappings/description/
#
# algorithms
# Easy (75.52%)
# Total Accepted:    17K
# Total Submissions: 22.5K
# Testcase Example:  '[12,28,46,32,50]\n[50,12,32,46,28]'
#
# 
# Given two lists A and B, and B is an anagram of A. B is an anagram of A means
# B is made by randomizing the order of the elements in A.
# 
# We want to find an index mapping P, from A to B. A mapping P[i] = j means the
# ith element in A appears in B at index j.
# 
# These lists A and B may contain duplicates.  If there are multiple answers,
# output any of them.
# 
# 
# 
# For example, given
# 
# A = [12, 28, 46, 32, 50]
# B = [50, 12, 32, 46, 28]
# 
# 
# We should return
# 
# [1, 4, 3, 2, 0]
# 
# as P[0] = 1 because the 0th element of A appears at B[1],
# and P[1] = 4 because the 1st element of A appears at B[4],
# and so on.
# 
# 
# Note:
# A, B have equal lengths in range [1, 100].
# A[i], B[i] are integers in range [0, 10^5].
# 
#
class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        new_l = []
        
        for i in A:
            repeat = set()
            for j in range(len(B)):
                
                if B[j] in repeat:
                    continue 
                else:
                    repeat.add(B[j])
                if i == B[j]:
                    new_l.append(j)
        return new_l

        
        # P = []
        # length = len(A)
        # for i in range(length):
        #     P.append(B.index(A[i]))

        # return P

# s = Solution()
# print(s.anagramMappings([40,40],[40,40]))