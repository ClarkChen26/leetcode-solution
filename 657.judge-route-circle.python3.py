#
# [657] Judge Route Circle
#
# https://leetcode.com/problems/judge-route-circle/description/
#
# algorithms
# Easy (68.33%)
# Total Accepted:    68.2K
# Total Submissions: 99.9K
# Testcase Example:  '"UD"'
#
# 
# Initially, there is a Robot at position (0, 0). Given a sequence of its
# moves, judge if this robot makes a circle, which means it moves back to the
# original place. 
# 
# 
# 
# The move sequence is represented by a string. And each move is represent by a
# character. The valid robot moves are R (Right), L (Left), U (Up) and D
# (down). The output should be true or false representing whether the robot
# makes a circle.
# 
# 
# Example 1:
# 
# Input: "UD"
# Output: true
# 
# 
# 
# Example 2:
# 
# Input: "LL"
# Output: false
# 
# 
#
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        rcount = 0
        lcount = 0
        ucount = 0
        dcount = 0
        # result = 0
        for i in moves:
            if i == "R":
                rcount += 1
            elif i == "L":
                lcount += 1
            elif i == "U":
                ucount += 1
            elif i == "D":
                dcount +=1
        # result = rcount + lcount + ucount + dcount
        # if result % 2 == 0:
        if (rcount == lcount) and (ucount == dcount):
            return True
        return False
        
# s = Solution()
# print(s.judgeCircle('LL'))
