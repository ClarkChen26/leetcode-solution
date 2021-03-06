#
# [822] Unique Morse Code Words
#
# https://leetcode.com/problems/unique-morse-code-words/description/
#
# algorithms
# Easy (81.31%)
# Total Accepted:    4.2K
# Total Submissions: 5.2K
# Testcase Example:  '["gin", "zen", "gig", "msg"]'
#
# International Morse Code defines a standard encoding where each letter is
# mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps
# to "-...", "c" maps to "-.-.", and so on.
# 
# For convenience, the full table for the 26 letters of the English alphabet is
# given below:
# 
# 
# 
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# 
# Now, given a list of words, each word can be written as a concatenation of
# the Morse code of each letter. For example, "cab" can be written as
# "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call
# such a concatenation, the transformation of a word.
# 
# Return the number of different transformations among all words we have.
# 
# 
# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# 
# There are 2 different transformations, "--...-." and "--...--.".
# 
# 
# 
# 
# Note:
# 
# 
# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# ⁠   words[i] will only consist of lowercase letters.
# 
# 
#
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # letter = [0:"a", 1:"b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        s = set()
        # diff = 0
        for word in words:
            c = ""
            for l in word:
                c += morse[ord(l) - 97]
            s.add(c)
                
        return len(s)
# s = Solution()
# print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))